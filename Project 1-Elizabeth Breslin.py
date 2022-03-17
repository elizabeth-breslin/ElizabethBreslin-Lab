#!/usr/bin/env python
# coding: utf-8

# In[116]:


#This program imports a csv file that has data on the avocado sales from 2015 to 2021. The data includes columns for the 
#price and volume of three sizes of Hass avocados, small, large and extra large. 
#The python function deletes the columns for the extra large avocados, both the price and the volumn columns. I did 
#this because for many of the dates, no extra large avocados were bought and I thought this would make the averages 
#for volume and price skewed. I then renamed the column labels for the Hass avocados from the labels 'plu4046' and 
#'plu4225' to Hass Small and Hass Big respectively. I decided to do this because I was very confused on what the columns 
#were referring to since I was unaware what 'plu4225' meant and there was no units attatched to the numerical values 
#displayed in the columns. Once I realized that total volume was the column before the three 'plu' columns and the numbers
#given for each type of avocado added up to the total volume, I understood that those columns were the volumes sold for 
#each type of avocado. I thought that changing the name to a more descriptivet title would make it easier for me to 
#understand what data I was looking at. 
#In order to satisfy producing a brief summary of the data, I produced both a table summary, giving the amount of rows 
#and columns in the table, as well as the average price for conventional and organic avocados. Producing the average prices 
#took me a while to figure out since while splicing up the columns I created a list of a list instead of just a list of all
#the prices. Once I figured out how to break up the list I was able to calculate the average price for each type of avocado.
#I ran into the issue of ensuring that the path I have in my computer will allow anyone else to use this program even 
#though the csv file is on my computer. I have both the full path from computer named as path_to_file and the shortened path
#that Dylan recommended I use listed as path_to_file. The shorted path is commented out because I was not able to get this 
#shorted path to work and each time I would just get the output "The file {path_to_file} does not exist", which is the 
#output I have for my else statement. When I use the full path, my code works correctly. I have attatched my csv file in my 
#submission so it may work if you download the file to your computer. 


import pandas as pd
from pathlib import Path
from statistics import mean

#Retrieving local file
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
    

