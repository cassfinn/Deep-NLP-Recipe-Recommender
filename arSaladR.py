from bs4 import BeautifulSoup

import requests
import unicodedata

import re
from functools import wraps
import sys
import csv
import time


from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_recipe(sUrl, sClass, iPage):

    print("sUrl: ", sUrl)
    print("===")

    print("PAGE: ", iPage)

    #try:
        #req = requests.get(sUrlPage)
    req = requests.get(sUrl)
    #except ValueError:
    if req.status_code != 200:
        return

    #req = requests.get(sUrl)
    soup = BeautifulSoup(req.text,'html.parser')

    rec = soup.find_all('li', {'class': sClass})
    #print("rec: ",rec)
    recs = []
    for recipe in rec:

        recipe2 = recipe.find('a', {'class': sClass}).get("href")    
        #rec2 = recipe2.get("href")
        #rec2 = recipe.get("href")
        print(recipe2)
        #print(rec2)
        recs.append(recipe2)
        #print("recLink: ", rec2)
    print("===")


    print("===")
    urlItem =  soup.find('li', {'class': 'trending-story primary'})
    print("urlItem: ", urlItem)
    print("===")



    print("title")
    title = ""
    if soup.find('h1', {'itemprop': 'name'}) is not None:
	    title = soup.find('h1', {'itemprop': 'name'}).get_text()


    print("===")
    linkRef = ""
    if soup.find(itemprop="url") is not None:
	    linkRef = soup.find(itemprop="url").get("href")
    print("linkRef: ", linkRef)
    print("===")


    print("===")
    if soup.find(itemprop="prepTime") is not None:
    	prep_time = soup.find(itemprop="prepTime").get("datetime")
		#print("prepTime: ", prep_time)
    else:
    	prep_time = ""
    print("===")


    print("===")
    if soup.find(itemprop="cookTime") is not None:
        cook_time = soup.find(itemprop="cookTime").get("datetime")
        print("cookTime: ", cook_time)
    else:
        cook_time = " "
    print("===")


    print("===")
    total_time = ""
    if soup.find(itemprop="totalTime") is not None:
	    total_time = soup.find(itemprop="totalTime").get("datetime")
    print("totalTime: ", total_time)
    print("===")


    print("===")
    yield2 = ""
    if soup.find(itemprop="recipeYield") is not None:
	    yield2 = soup.find(itemprop="recipeYield").get("content")
    print("yield: ", yield2)
    print("===")


    print("===")
    rating = ""
    if soup.find(itemprop="ratingValue") is not None:
	    rating = soup.find(itemprop="ratingValue").get("content")
    print("rating: ", rating)
    print("===")


    print("===")
    reviewCount = ""
    if soup.find(itemprop="reviewCount") is not None:
	    reviewCount = soup.find(itemprop="reviewCount").get("content")
    print("reviewCount: ", reviewCount)
    print("===")


    print("===")
    cat2 = ""
    if soup.find_all(itemprop="recipeCategory") is not None:
	    category = soup.find_all(itemprop="recipeCategory")
	    cats = []
	    for cat in category:
	        cat2 = cat.get("content")
	        cats.append(cat2)
	        print("category: ", cat2)
	    print("===")


    print("===")
    author = ""
    author2 = ""
    if soup.find('span', {'class': 'submitter__name'}) is not None:
	    author = soup.find('span', {'class': 'submitter__name'})
	    author2 = author.text.strip()
	    print("author: ", author2)
	    print("===")


    print("===")
    ingredients = soup.find_all('span', {'class': 'recipe-ingred_txt added'})
    ingreds = []
    for ingred in ingredients:
        ingred2 = ingred.text.strip()
        ingreds.append(ingred2)
        print("ingred: ", ingred2)
    print("===")

    print("===")
    instructions = soup.find_all('span', {'class': 'recipe-directions__list--item'})
    instructs = []
    for instruct in instructions:
        instruct2 = instruct.text.strip()
        instructs.append(instruct2)
        print("instruct: ", instruct2)
    print("===")


    print("===")
    reviews = soup.find_all('p', attrs={'itemprop': 'reviewBody'})
    reviews2 = []
    for review in reviews:
        review3 = review.text.strip()
        reviews2.append(review3)
        print("reviews2: ", reviews2)
    print("===")


    name2 = " "
    name = soup.find('h1', attrs={'itemprop': 'name'})
    if name is not None:
	    name2 = name.text.strip()
    print("name_name: ", name2)


    fat2 = ""
    fat = soup.find('span', attrs={'itemprop': 'fatContent'})
    if fat is not None:
	    fat2 = fat.text.strip()
    print("fat_name: ", fat2)


    cal = ""
    calories = soup.find('span', attrs={'itemprop': 'calories'})
    if calories is not None:
	    cal = calories.text.strip()
    print("calories: ", cal)


    carb2 = ""
    carb = soup.find('span', attrs={'itemprop': 'carbohydrateContent'})
    if carb is not None:
	    carb2 = carb.text.strip()
    print("carbs: ", carb2)

    protein2 = ""
    protein = soup.find('span', attrs={'itemprop': 'proteinContent'})
    if protein is not None:
	    protein2 = protein.text.strip()
    print("protein: ", protein2)


    sugar_name = ""
    sugar = soup.find('span', attrs={'itemprop': 'sugarContent'})
    if sugar is not None:
	    sugar_name = sugar.text.strip()
    print("sugar: ", sugar_name)


    chol2 = ""
    chol = soup.find('span', attrs={'itemprop': 'cholesterolContent'})
    if chol is not None:
	    chol2 = chol.text.strip()
    print("cholesterol: ", chol2)

    sodium2 = ""
    sodium = soup.find('span', attrs={'itemprop': 'sodiumContent'})
    if sodium is not None:
	    sodium2 = sodium.text.strip()
    print("sodium: ", sodium2)

    sPage = str(iPage)

    csv_row = [name2, linkRef, cat2, prep_time, cook_time, total_time, yield2, rating, reviewCount, cats, author2, ingreds, instructs, fat2, cal, carb2, protein2,chol2, sodium2, sPage, reviews2]

    return csv_row


#for sUrlPage in sUrlPages:
    
i = 0
while True:

    time.sleep(1.2)
    i = i + 1
    sUrlPage = "https://www.allrecipes.com/recipes/96/salad/"

    sUrlPage = sUrlPage + "?page=" + str(i)
    print(" ")
    print("********************************************************")
    print("*********************")
    print("sUrlPage: ", sUrlPage)
    print("*********************")
    print("********************************************************")
    print(" ")

    req = requests.get(sUrlPage)
    if req.status_code != 200:
        break

    soup = BeautifulSoup(req.text,'html.parser')

    #Bread
    #sClass = "fixed-recipe-card__info"
    sClass = "fixed-recipe-card__h3"
    links = soup.find_all(class_ = sClass)

    for link in links:
        if link.a is not None:
            print("link.link: ", link.a.get("href"))
            sUrl = link.a.get("href")
            if sUrl is not None:
                if "https://www.allrecipes.com/" not in sUrl:
                    str1 = "https://www.allrecipes.com/"
                    str1 += sUrl
                    sUrl = str1

                csv_row = get_recipe(sUrl, sClass, i)
                if csv_row is not None:
                    csvfile = "dataARsaladR.csv"
                    with open(csvfile, "a") as fp:
                        wr = csv.writer(fp, dialect='excel')
                        wr.writerow(csv_row)


    #links = soup.find_all(class_ = "slider-card__recipes")
    links = soup.find_all(class_ = "list-recipes__recipe")
    sClass = "list-recipes__recipe"


    for link in links:
        print("link.text: ", link.get_text(strip=True))
        if link.a is not None:
            print("link.link: ", link.a.get("href"))
            sUrl = link.a.get("href")
            if sUrl is not None:
                if "https://www.allrecipes.com/" not in sUrl:
                    str1 = "https://www.allrecipes.com/"
                    str1 += sUrl
                    sUrl = str1

                csv_row = get_recipe(sUrl,sClass, i)
                if csv_row is not None:
                    csvfile = "dataARsaladBR.csv"
                    with open(csvfile, "a") as fp:
                        wr = csv.writer(fp, dialect='excel')
                        wr.writerow(csv_row)
