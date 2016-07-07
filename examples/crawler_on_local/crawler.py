from __future__ import print_function

import sys
from operator import add

from pyspark import SparkContext
import requests
from bs4 import BeautifulSoup

Image_URL = "http://radiopaedia.org/cases/"

def flat_mapper(n):
    get_page_URL = Image_URL + ("?page=%d" % n)
    try:
        case_Webpage = requests.get(get_page_URL)
    except requests.exceptions.ConnectionError:
        print('Error')
        return

    b = BeautifulSoup(case_Webpage.content, "html.parser")
    case = b.find_all(attrs={"class":"search-result-case"})

    if len(case) == 0:
        return

    title_list = []
    for j in range(len(case)):
        #case_id = case[j].find_all('id')
        #case_link = case[j].find_all('a')
        
        #case_complete = case[j].find_all(attrs={"class": "completed"})
        case_title = case[j].find_all(attrs={"class": "search-result-title-text"})
        current = case_title[0].text.strip()
        title_list.append(current)
    
    return title_list


if __name__ == "__main__":

    sc = SparkContext(appName="Python Crawler")
    
    narray = range(1, 246)
    narray = sc.parallelize(narray)
    counts = narray.flatMap(flat_mapper).map(lambda x: (x, 1)).reduceByKey(add)
    
    output = counts.collect()
    total_count = 0
    for (word, count) in output:
        print("%s: %i" % (word.encode('utf-8'), count))
        total_count += count
    print (total_count)
    sc.stop()
