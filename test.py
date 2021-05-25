from BeatifulXml import BeautifulXml


if __name__=="__main__":
    file = open('skroutzdata-all.xml','r',encoding='utf-8')
    soup=BeautifulXml(file,'product')
    items=soup.fetchDict('name')
    print(items)
    # print(soup.get_me())
    # print(soup.get_version())