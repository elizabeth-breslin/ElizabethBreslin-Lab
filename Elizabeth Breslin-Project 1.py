#!/usr/bin/env python
# coding: utf-8

# In[114]:


#Retrieving local file 
import pandas as pd

from pathlib import Path
from statistics import mean
path_to_file = r'C:\Users\Student\Downloads\UVA\Third Year\Spring\DS3002\Project 1\avocado cleaned.csv'
#path_to_file = r'./avocado cleaned.csv'
path = Path(path_to_file)

if path.is_file():
    print(f'The file {path_to_file} exists')
    dropped_avo = avocado.drop(["XLargeBags","plu4770"],1)
    named_avo = dropped_avo.rename({'plu4046':'Hass Small','plu4225': 'Hass Big'},axis=1)
    result = named_avo.shape
    
    #Conventional Average Price 
    avo_conven = named_avo.loc[avocado.type == "conventional",["AveragePrice"]]
    conventional_list_of_list = avo_conven.values.tolist()
    conventional_list  = [val for sublist in conventional_list_of_list for val in sublist]
    def Average_C(conventional_list):
        return sum(conventional_list) / len(conventional_list)
    average_C = Average_C(conventional_list)
    
    #Organic Average Price 
    avo_organ = named_avo.loc[avocado.type == "organic",["AveragePrice"]]
    organic_list_of_list = avo_organ.values.tolist()
    organic_list  = [val for sublist in organic_list_of_list for val in sublist]
    def Average_O(organic_list):
        return sum(organic_list) / len(organic_list)
    average_O = Average_O(organic_list)

    print("Average price of conventional avocados =","$", round(average_C, 2))
    print("Average price of organic avocados =","$", round(average_O, 2))
    print("Table Characteristics:")
    print("Rows:",result[0])
    print("Columns:",result[1]) 
    
else:
    print(f'The file {path_to_file} does not exist')
    

