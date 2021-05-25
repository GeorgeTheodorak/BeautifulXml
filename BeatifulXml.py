from bs4 import BeautifulSoup
import platform

class Parsing_Failed(Exception):
    msg = 'Failed to parse xml'
    def print_e(self):
        print (self.msg)
        return
class Root_not_found(Exception):
    msg = 'Failed to find root'
    def print_e(self):
        print(self.msg)
        return



class BeautifulXml:
    DOCUMENT = ''
    VERSION = "0.0"
    INDEX_CHECKUP = False
    SOUP_CONST_OBJECT = ''
    
    PARSER = 'xml' if platform.system() == 'Windows' else 'lxml'
    INDEX_ROOT = ''
    def get_version(self)->str:
        # version checkup function
        print(f"BeautifulXml is currently on:{ self.version }")
        return self.version


    def update()->str:
        # check for updates
        pass


           
    def __init__(self, xml_file,root)->object:
        """
        This is the main constructor class returning an object
        """
        # Parse the xml document find the root element
        try:
            self.SOUP_CONST_OBJECT = BeautifulSoup(xml_file)
        except:
            raise(Parsing_Failed)
        if self.SOUP_CONST_OBJECT.find(root):
            INDEX_CHECKUP = True
        else:
            raise(Parsing_Failed)


    def format__(self, data) -> list:

        pass


    def fetchDict(self,data,arr=[]) -> dict:
        if platform.system() == 'Windows':
            soup = BeautifulSoup(data,'xml')
        
