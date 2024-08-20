from bs4 import BeautifulSoup
import platform
import json
from lib.BXLF import get_atribute_text

# Custom Exceptions
class ParsingFailed(Exception):
    def __init__(self, message="Failed to parse XML"):
        super().__init__(message)

class RootNotFound(Exception):
    def __init__(self, message="Failed to find root"):
        super().__init__(message)

class Bs4NotFound(Exception):
    def __init__(self, message="BeautifulSoup (bs4) not found. Consider running 'pip install bs4'"):
        super().__init__(message)

class ParserNotFound(Exception):
    def __init__(self, message="Specified parser not found. Consider using 'lxml' or 'xml'"):
        super().__init__(message)


VERSION = "0.0.1"

class BeautifulXml:
    def __init__(self, xml_file: str, root: str, parser: str = None):
        """
        Initialize the BeautifulXml class.

        :param xml_file: XML file content as string.
        :param root: Root element to find in the XML.
        :param parser: Optional parser to use. Defaults to 'xml' on Windows and 'lxml' otherwise.
        """
        self.DOCUMENT = xml_file
        self.ROOT_NAME = root
        self.ERROR_ARRAY = []
        self.r_dict = []
        
        # Determine the parser to use
        self.PARSER = parser if parser else ('xml' if platform.system() == 'Windows' else 'lxml')
        
        # Validate parser choice
        if self.PARSER not in ['lxml', 'lxml-xml', 'xml']:
            raise ParserNotFound()

        try:
            self.SOUP_CONST_OBJECT = BeautifulSoup(xml_file, self.PARSER)
        except ModuleNotFoundError:
            raise Bs4NotFound()
        except Exception as e:
            raise ParsingFailed(str(e))

        self.INDEX_ROOT = self.SOUP_CONST_OBJECT.find(root)
        if not self.INDEX_ROOT:
            raise RootNotFound(f"Root element '{root}' not found in the XML.")
        
        self.INDEX_CHECKUP = True

    @staticmethod
    def get_version() -> str:
        """
        Returns the current version of BeautifulXml.
        """
        return VERSION

    def set_parser(self, parser: str) -> None:
        """
        Change the parser used for parsing XML.

        :param parser: Parser name to be used. Must be one of 'lxml', 'lxml-xml', or 'xml'.
        """
        if parser not in ['lxml', 'lxml-xml', 'xml']:
            raise ParserNotFound()
        self.PARSER = parser

    def get_root(self) -> BeautifulSoup:
        """
        Returns the root element found in the XML.

        :return: BeautifulSoup object representing the root element.
        """
        return self.INDEX_ROOT

    def to_json(self, data: dict) -> str:
        """
        Converts the given dictionary to a JSON string.

        :param data: Data to be converted to JSON.
        :return: JSON string representation of the data.
        """
        return json.dumps(data, ensure_ascii=False, indent=4)

    def fetch_errors(self) -> str:
        """
        Fetches and returns the errors encountered during parsing.

        :return: String representation of errors.
        """
        return "\n".join(self.ERROR_ARRAY)

    def fetch_dict(self, *data) -> dict:
        """
        Fetches a dictionary representation of the XML elements matching ROOT_NAME.

        :param data: Additional data or parameters.
        :return: Dictionary with parsed XML data.
        """
        for entity in self.SOUP_CONST_OBJECT.find_all(self.ROOT_NAME):
            parsed_data, self.ERROR_ARRAY = get_atribute_text(entity, data, self.ERROR_ARRAY)
            self.r_dict.append({self.ROOT_NAME: parsed_data})
        return self.r_dict
