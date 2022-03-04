# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 11:42:07 2022

@author: Student
"""

import sys
import requests
import json

print(sys.argv)
stock = sys.argv[1:]
for  ticker in stock:
    url = "https://yfapi.net/v6/finance/quote"
    querystring = {"symbols":ticker}

    headers = {
        'x-api-key': "CxPzo8KaBO9T51HkUAyn67Uf7GQphhHd6WBuwGXP"
            }

    response = requests.request("GET", url, headers=headers, params=querystring)

    stock_json = response.json()
    if (len(stock_json['quoteResponse']['result'])<1)or((stock_json['quoteResponse']['result'][0]['quoteType'])!="EQUITY") or ((stock_json['quoteResponse']['result'][0]['Region'])!="US"):
        print("Error, enter a new stock")
    else: print(str(stock_json['quoteResponse']['result'][0]['longName']) + ':' + str(stock_json['quoteResponse']['result'][0]['regularMarketPrice']))
    
