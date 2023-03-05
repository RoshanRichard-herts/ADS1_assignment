#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:50:56 2023

@author: roshanrichard
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests



# Function to convert USD to GBP
# An uniquie api key is required for this function to work
def usd_to_gbp():
    try:
        url = "https://api.apilayer.com/exchangerates_data/convert?to=GBP&from=USD&amount=1"
        payload = {}
        headers= {
            "apikey": "pc3eZL6gWv2WEjxr67qliqMPFYCLiShD"
            }
        response = requests.request("GET", url, headers=headers, data = payload)
        #status_code = response.status_code
        result = response.text
        index = result.find("result")
        #print("working")
        return float(result[index+9:index+15])
        
    except:
        #print("no  internet connection")
        return 0.8309


"""    
# Alternatively we can use url of the dataset but it requires an proper internet connection

url_CS = "https://pkgstore.datahub.io/8456d91866dd4ee0900d814a04acabdd/cloud-storage-prices/cloud-storage-prices-year_csv_csv/data/525e84005307615124052cec511f5a72/cloud-storage-prices-year_csv_csv.csv"
url_TCS = "https://pkgstore.datahub.io/8456d91866dd4ee0900d814a04acabdd/car-sales-world-annual/total_sales_world_annual_csv_csv/data/f0d0434666a792cb9b3f1c6f5b907bf7/total_sales_world_annual_csv_csv.csv"
url_bData = "https://pkgstore.datahub.io/world-bank/sp.dyn.cbrt.in/data_csv/data/366ebb9361dabf4ee5256d206b6ff349/data_csv.csv"
url_dData = "https://pkgstore.datahub.io/world-bank/sp.dyn.cdrt.in/data_csv/data/7b3e315805426a51e6a7b2f3544dceef/data_csv.csv"
"""

# PATH to the Cloud Storage Prices CSV file


url_CS = "CSP_csv.csv"

# PATH to Total Cars Sold Data CSV file
url_TCS =  "TCS_csv.csv"

# PATH to the Birth Rate Data CSV file
url_bData = "BD_csv.csv"

# PATH to the death rate Data CSV file
url_dData = "DD_csv.csv"



usd_val = usd_to_gbp()

 # Conveerting all csv files to DataFrame
df_CS = pd.read_csv(url_CS)
df_TCS = pd.read_csv(url_TCS, index_col=0)
df_BD = pd.read_csv(url_bData)
df_DD = pd.read_csv(url_dData)

# Multiplying all int values in df_CS with 100 to get get Price per 100GB

df_CS.iloc[:,1:] = df_CS.iloc[:,1:] * 100 * usd_val


# todo: USD to GBP conversion




df_TCS = df_TCS.loc[["INDIA","CHINA","UNITED STATES OF AMERICA","JAPAN"]]
df_TCS = df_TCS/1000000
df_TCS = df_TCS.T

x = np.arange(len(df_TCS["INDIA"]))
width = .20



df_BD_2016 = df_BD[df_BD["Year"] == 2016]
df_DD_2016 = df_DD[df_DD["Year"] == 2016]
df_BD_1960 = df_BD[df_BD["Year"] == 1960]
df_DD_1960 = df_DD[df_DD["Year"] == 1960]



# Plotting the cloud storage prices into an line plot

plt.rcParams['font.size'] = 20
plt.figure(figsize=(10, 6), layout='constrained')
plt.plot(df_CS["Year"],df_CS["Amazon"],marker='o',label= "Amazon")
plt.plot(df_CS["Year"],df_CS["Azure"],marker='o',label= "Azure")
plt.plot(df_CS["Year"],df_CS["Google"],marker='o',label= "Google")
plt.title("Clould Storage Prices from 2010 to 2019")
plt.ylabel("GBP per 100 Giga Bytes")
plt.xlabel("Years")
plt.grid(True)
plt.legend()
plt.show()
plt.close()

# Plotting the cars sold in each country

plt.figure(figsize = (9,6), layout = "constrained")
plt.title("Cars sold in each Country")
plt.bar(x - width / 2, df_TCS["INDIA"], width, label="INDIA")
plt.bar(x + width / 2, df_TCS["CHINA"], width, label="CHINA")
plt.bar(x - (width / 2) * 3, df_TCS["UNITED STATES OF AMERICA"],width, label = "UNITED STATES OF AMERICA")
plt.bar(x + (width / 2) * 3, df_TCS["JAPAN"],width ,label = "JAPAN")
plt.xlabel("YEARS")
plt.ylabel("Per one million")
plt.xticks(x,labels = df_TCS.index,rotation = 45)
plt.rcParams['font.size'] = 18
plt.legend()
plt.show()
plt.close()





plt.figure(figsize = (10,10), layout = "constrained")
plt.scatter(df_BD_2016["Value"], df_DD_2016["Value"], color = "red" )
plt.xlabel('Birth Rate',fontsize=30)
plt.ylabel('Death Rate',fontsize=30)
plt.title('Birth and Death rate analysis (2016)',fontsize=30)
plt.grid(color='r', linestyle='-', linewidth=.5 )
#plt.xticks([0,1], labels = [22,3])
plt.rcParams['font.size'] = 40
plt.xticks([10,20,30,40,50],fontsize=25)
plt.yticks([5,10,15,20,25,30,35],fontsize=25)
plt.show()
plt.close()

plt.figure(figsize = (10,10), layout = "constrained")
plt.scatter(df_BD_1960["Value"], df_DD_1960["Value"], color = "green" )
plt.xlabel('Birth Rate',fontsize=30)
plt.ylabel('Death Rate',fontsize=30)
plt.title('Birth and Death rate analysis (1960)',fontsize=30)
plt.grid(color='g', linestyle='-', linewidth=.5 )
#plt.xticks([0,1], labels = [22,3])
plt.rcParams['font.size'] = 10
plt.xticks([10,20,30,40,50], fontsize=25)
plt.yticks(fontsize=25)
plt.show()
plt.close()







