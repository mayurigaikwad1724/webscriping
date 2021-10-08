from task1 import movies
import json
name= movies()

def group_of_year(movies):
    # print(movies)
    years = []
    for i in movies:
        year=i["movies year"]
        if year not in years:
            years.append(year)
        # print(year)
    movies_dict={i:[] for i in years}
    # print(movies_dict)
    for i in movies:
        year = i["movies year"]
        for x in movies_dict:
            if str (x) == str (year):
                movies_dict[x].append(i)
                with open ("movies_year.json","w") as file:
                    json.dump(movies_dict,file,indent=4)
    return movies_dict


group_of_year(name)