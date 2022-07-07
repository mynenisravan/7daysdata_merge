# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 13:41:03 2022

@author: H283847
"""

import pandas as pd

df = pd.DataFrame()

LL = 14
HH = 22
for x in range (LL,HH):
    if x==LL: 
        path = "C:\\Users\H283847\Documents\OMAN\short trends\Kero_Flash_"
        num = str(x)
        ext = ".txt"
        input_file = path+num+ext
        df_name1 = pd.read_csv(input_file, sep="\t",header=None)
        df = df.append(df_name1[:])
    else:
        path = "C:\\Users\H283847\Documents\OMAN\short trends\Kero_Flash_"
        num = str(x)
        ext = ".txt"
        input_file = path+num+ext
        df_name1 = pd.read_csv(input_file, sep="\t",header=None)
        df = df.append(df_name1[2:])
        
    
    
df.to_csv("C:\\Users\H283847\Documents\OMAN\short trends\merge.csv", header=None)
