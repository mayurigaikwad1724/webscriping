from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint
from os import path
import os

def scrap_pickle():
    if os.path.isfile("pickel.json"):
        with open ("pickel.json","r") as file:
            data = json.load(file)
            return data

    else:
        url = "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
        page = requests.get(url)
            # print(page)
        htmlcontent = page.content
                # print(htmlcontent)
        soup = BeautifulSoup(htmlcontent,"html.parser")
                # print(soup)
        div = soup.find("div",class_="_1gX7")
                # print(div)
        products= div.span.get_text()
                # print(products)
        split_list=products.split(" ")
                # print(split_list)    
        a=int(split_list[1])
        b=a//32+1
                # print(b)
        pickle=[]
        number = 0
        pickle_index = 1
        while pickle_index<=b:
            pickles_api="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(pickle_index)
            pickles_url = requests.get(pickles_api)
            pickles_soup= BeautifulSoup(pickles_url.text,"html.parser")
                    # print(pickles_soup)
            pickles_div=pickles_soup.find("div",class_="_3RA-")
            pickle_name= pickles_div.find_all("div",class_= "UGUy")
                    # print(pickle_name)
            pickles_rate=pickles_div.find_all("div",class_="_1kMS")
            pickles_link=pickles_div.find_all("div",class_="_3WhJ")
                    # print(pickles_link)
            i=0
            while i<len(pickle_name):
                number+=1
                pickle2_name= pickle_name[i].get_text()
                pickle_link = pickles_link[i].a["href"]
                        # print(pickle_link)
                pickle_rate=pickles_rate[1].get_text()
                        # print(pickle_rate)
                pickel_url="https://paytmmall.com"+pickle_link
                pickles_details={"position":number,"name":pickle2_name,"price":pickle_rate,"url":pickel_url}
                pickle.append(pickles_details.copy())
                i=i+1
            pickle_index+=1
        with open ("pickel.json","w") as file:
            json.dump(pickle,file,indent=4)
        return pickle
    # print(pickle)
pprint(scrap_pickle())