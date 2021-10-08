from bs4 import BeautifulSoup
import json
import requests
import pprint

def e_commerce():
    url="https://webscraper.io/test-sites"
    site_page=requests.get(url)
    htmlcontent = site_page.content
    soup = BeautifulSoup(htmlcontent,"html.parser")
    main_div=soup.find_all("div",class_= "col-md-7 pull-right" )
    d=[]
    srno=1
    for i in main_div:
        name=i.find("h2",class_="site-heading").get_text()
        url=i.find("h2",class_="site-heading").a["href"]
        url_1="https://webscraper.io/test-sites"+url
        position={"title":name.strip(),"data":url_1}
        d.append(position)
        with open("commerce.json","w") as f:
            json.dump(d,f,indent=4)
e_commerce()