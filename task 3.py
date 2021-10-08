from requests import models
from task1 import movies

import json 

scrapped = movies()


def group_by_decade(movies):
    # mod_dict={}
    list=[]
    for i in movies:
        mode  = i["movies year"]%10
        decade = i["movies year"]-mode
        # print(decade)
        if decade not in list:
            list.append(decade)
    list.sort()
    mod_dict={}
    for i in list:
        list1=[]
        for x in movies:
            if x["movies year"]>=i and x["movies year"]<=i+10:
                # for k in movies(j):
                    list1.append(x)
                    mod_dict[i]=list1
                    with open ("decade.json","w") as file:
                        json.dump(mod_dict,file,indent=4)
    return mod_dict

group_by_decade(scrapped)