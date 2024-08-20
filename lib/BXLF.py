from bs4 import BeautifulSoup



def a_not_found_elements(e_array,e)->list:
    """
        returns the not found elemnts either with blank values
    """
    e_array.append(dict(e='not_found'))
    return e_array

def get_atribute_text(soup,tag,e_array)->list:
    try:
        item=soup.find(tag).text
    except:
        e_array=a_not_found_elements(e_array,tag)
    return item , e_array