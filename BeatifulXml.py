from os import stat
from bs4 import BeautifulSoup
import platform
from lib.BXLF import get_atribute_text
import json

# @Exception
class Parsing_Failed(Exception):
    msg = 'Failed to parse xml'
    def __init__(self):
        super().__init__(self.msg)
        return

# @Exception
class Root_not_found(Exception):
    msg = 'Failed to find root'
    def __init__(self):
        super().__init__(self.msg)
        return
# @Exception
class Bs4NotFound(Exception):
    msg = 'Python cant find bs4 in your modules!\n Considering running pip install bs4'
    def __init__(self):
        super().__init__(self.msg)
        return

class ParserNotFound(Exception):
    msg = 'Python cant find bs4 in your modules!\n Considering running pip install bs4'
    def __init__(self):
        super().__init__(self.msg)
        return


VERSION = "0.0"

class BeautifulXml:
    DOCUMENT = ''
    INDEX_CHECKUP = False
    SOUP_CONST_OBJECT = '' 
    PARSER = 'xml' if platform.system() == 'Windows' else 'lxml' # The default parser , can be changed using the parser changer
    INDEX_ROOT = '' # the root
    ROOT_NAME=''
    ERROR_ARRAY=[]
    r_dict=[]



    @staticmethod
    def get_version()->str:
        # version checkup function
        print(f"BeautifulXml is currently on:{VERSION}")
        return VERSION

    @staticmethod
    def update()->str:
        # check for updates
        pass

    def setup_parser(self,parser)-> None:
        if parser != 'lxml' or parser != 'lxml-xml' or parser != 'xml':
            raise ParserNotFound()
        else:   
            self.PARSER = parser

    def __init__(self, xml_file,root)->object:
        """
        This is the main constructor class returning an object
        """
        # Parse the xml document find the root element

        self.ROOT_NAME=root
        try:
            self.SOUP_CONST_OBJECT = BeautifulSoup(xml_file,self.PARSER)
        except ModuleNotFoundError:
            print('BS4 Not found')
        except:
            raise Parsing_Failed
        if self.SOUP_CONST_OBJECT.find(root):
            self.INDEX_CHECKUP = True
            self.INDEX_ROOT=self.SOUP_CONST_OBJECT.find(root)
            return __class__ == BeautifulXml 
        else:
            raise Parsing_Failed
    
    def get_me(self)-> BeautifulSoup:
        return self.INDEX_ROOT


    def json_(self, data) -> json.dump():
        pass

    def fetch_errors() -> str:

        pass

    def fetchDict(self,*data) -> dict:
        print(data[1])
        for entity in self.SOUP_CONST_OBJECT.find_all(self.ROOT_NAME):
            dato_parsed , self.ERROR_ARRAY=get_atribute_text(entity,dato,self.ERROR_ARRAY)
            self.r_dict.append(dict(dato = dato_parsed))
        return self.r_dict
        
