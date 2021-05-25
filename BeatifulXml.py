from bs4 import BeautifulSoup
import platform
from lib.BXLF import get_atribute_text


class Parsing_Failed(Exception):
    msg = 'Failed to parse xml'
    def __init__(self):
        super().__init__(self.msg)
        return


class Root_not_found(Exception):
    msg = 'Failed to find root'
    def __init__(self):
        super().__init__(self.msg)
        return



class BeautifulXml:
    DOCUMENT = ''
    VERSION = "0.0"
    INDEX_CHECKUP = False
    SOUP_CONST_OBJECT = ''
    test=''
    PARSER = 'xml' if platform.system() == 'Windows' else 'lxml'
    INDEX_ROOT = ''
    ROOT_NAME=''
    ERROR_ARRAY=[]
    r_dict=[]
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
        self.ROOT_NAME=root
        try:
            self.SOUP_CONST_OBJECT = BeautifulSoup(xml_file,self.PARSER)
        except:
            raise(Parsing_Failed)
        if self.SOUP_CONST_OBJECT.find(root):
            self.INDEX_CHECKUP = True
            self.INDEX_ROOT=self.SOUP_CONST_OBJECT.find(root)
        else:
            raise(Parsing_Failed)
    
    def get_me(self)-> BeautifulSoup:
        return self.INDEX_ROOT


    def format__(self, data) -> list:

        pass



    def fetchDict(*data) -> dict:
        data.pop[0]
        print (data)
        return
        for entity in self.SOUP_CONST_OBJECT.find_all(self.ROOT_NAME):
            dato_parsed , self.ERROR_ARRAY=get_atribute_text(entity,dato,self.ERROR_ARRAY)
            self.r_dict.append(dict(dato = dato_parsed))
        return self.r_dict
        
