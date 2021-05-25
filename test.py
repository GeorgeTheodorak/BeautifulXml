from BeatifulXml import BeautifulXml


if __name__=="__main__":

    soup=BeautifulXml('data')

    print(soup.get_version())