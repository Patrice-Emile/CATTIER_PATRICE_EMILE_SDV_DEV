#!/usr/bin/env python
# coding: utf-8

# In[209]:


import pandas as pd
import numpy as np

# Exo 1
def csvReaderPlusPlus():
    return pd.read_csv("mower_market_snapshot.csv", delimiter=";")
rd = csvReaderPlusPlus()
rd


# In[210]:


# Exo 3
def prodCostHead(df,column):
    return df.loc[:,column].head()
    
display(prodCostHead(rd,'prod_cost'))


# In[192]:


# Exo 4

def sumIsNull(df):
    return df.isnull().sum()
sumIsNull(rd)


# In[193]:


# Exo 5
def mettreMoyInNanCase(df):
    somme = 0.0
    tableau = pd.to_numeric(df.loc[:,'prod_cost'], errors='coerce')
    tableau = tableau.replace(np.nan, 0, regex=True)
    for i in tableau :
        somme += i

    moy = somme/1400
    print(moy)

    df.loc[:,'prod_cost'] = df.loc[:,'prod_cost'].replace(np.nan, moy, regex=True)

    #for i in rd.loc[:,'prod_cost']:
    #    print(i)
    return df.isnull().sum()
    
mettreMoyInNanCase(rd)


# In[199]:


# Exo 6
def grouByWarranty(df):
    print(df['warranty'].unique())
    print(type(df['warranty'].unique()))

grouByWarranty(rd)


# In[200]:


# Exo 7 & 8

def replaceWarranty(df):
    tab = df['warranty'].unique()

    for i in tab:
        if i[0] == '1':
            df.loc[:,'warranty'] = df.loc[:,'warranty'].replace(i, 1, regex=True)
        if i[0] == '2':
            df.loc[:,'warranty'] = df.loc[:,'warranty'].replace(i, 2, regex=True)
        if i[0] == '3':
            df.loc[:,'warranty'] = df.loc[:,'warranty'].replace(i, 3, regex=True)

    print(df['warranty'].unique())

replaceWarranty(rd)


# In[201]:


# Exo 9

def replaceCategoriePrice(df):
    for i in df['price']:
        if i > 0 and i <= 300:
            df.loc[:,'price'] = df.loc[:,'price'].replace(i, "0-300", regex=True) 
        if i > 300 and i <= 500:
            df.loc[:,'price'] = df.loc[:,'price'].replace(i, "301-500", regex=True)   
        if i > 500:
            df.loc[:,'price'] = df.loc[:,'price'].replace(i, "501-++", regex=True)

    return df.loc[:,'price']

display(replaceCategoriePrice(rd))


# In[207]:


# Exo 10

def replaceProductTypeValue(df):
    tab = df['product_type'].unique()

    for i in range(len(tab)):
        df.loc[:,'product_type'] = df.loc[:,'product_type'].replace(tab[i], (i+1), regex=True)

    print(df['product_type'].unique())

replaceProductTypeValue(rd)


# In[208]:


# Exo 11

def Add3Colonnes(df):
    df.insert(11, "auto-portee",0, allow_duplicates=False)
    df.insert(12, "electrique", 0, allow_duplicates=False)
    df.insert(13, "essence", 0, allow_duplicates=False)

    for i in range(len(df.loc[:,'product_type'])):
        if df.loc[:,'product_type'][i] == 1:
            df.loc[:,'auto-portee'][i] = 1
        elif df.loc[:,'product_type'][i] == 2:
            df.loc[:,'electrique'][i] = 1
        elif df.loc[:,'product_type'][i] == 3:
            df.loc[:,'essence'][i] = 1


    return df.loc[:,('product_type','auto-portee','electrique','essence')]

display(Add3Colonnes(rd))


# In[ ]:




