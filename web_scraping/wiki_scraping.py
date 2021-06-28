import requests , pprint
from bs4 import BeautifulSoup



def get_citations_needed_count(URL): 
    page= requests.get(URL)
    soup = BeautifulSoup(page.content , 'html.parser')
    result=soup.find_all('a' , title="Wikipedia:Citation needed")

    return int(len(result))



def get_citations_needed_report(URL): 
    array=[]
    page= requests.get(URL)
    soup = BeautifulSoup(page.content , 'html.parser')
    text=soup.find_all( 'p') 

    for p in text : 
        citations=p.find_all('a' , title="Wikipedia:Citation needed")
        if len(citations) >0 : 
            for i in citations : 
                array.append(p.text.strip())
    return ('\n'*2).join(array)



if __name__ == "__main__"  :
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    print (get_citations_needed_count(URL))
    print (get_citations_needed_report(URL))