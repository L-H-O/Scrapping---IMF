# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:14:07 2022

@author: lider
"""
import re
import pandas as pd
import requests as req
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup

#%% aux func

def has_numbers(string):
    return bool(re.search(r'\d', string))

#%%

def get_Dataflow():
    
    url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/DataFlow'    
    
    return req.get(url).json()['Structure']['Dataflows']['Dataflow']

Dataflow = get_Dataflow()

def get_Structure(Dataflow):
    
    Structure = [(i['Name']['#text'], i['KeyFamilyRef']['KeyFamilyID']) for i in Dataflow]

    return Structure
        
Structure = get_Structure(Dataflow)

def get_Ids(Structure):
    
    ids = []

    for i in Structure:
    
        if has_numbers(i[1]) == True:
       
            pass

        else:
       
           ids.append(i[1])

    return ids
    
ids = get_Ids(Structure)



#%%

soup = BeautifulSoup(test.content, 'html.parser')

def IMF_Scrap(key):

    url = f'http://dataservices.imf.org/REST/SDMX_JSON.svc/{key}'
    
    data = req.get(url.json()['CompactData']['DataSet']['Series'])
    
    
    