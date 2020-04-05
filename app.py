# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:19:49 2020

@author: margo
"""

import os
import pandas as pd
import numpy as np
import random
import folium
from folium.plugins import MarkerCluster
import unidecode

from flask import Flask, render_template

os.chdir('D:/Documents/1-ENSAE/3A/S2/Data_storytelling/data_storytelling/website')

df = pd.read_csv('../Data/df_sub_sirene.csv', ',')

df = df[df["montant"]>0]
df = df[df["Géolocalisation de l'établissement"].notna()]

df["nom_beneficiaire"] = df['nom_beneficiaire'].str.replace('[^\w\s]','')
df["nom_beneficiaire"] = df['nom_beneficiaire'].apply(unidecode.unidecode)

df[['latitude','longitude']]  = df["Géolocalisation de l'établissement"].str.split(',', expand=True)


#On tire 100 asso de manière aléatoire pour les projeter sur la carte
noms_random = random.sample(list(df["nom_beneficiaire"]), 100)

map_noms = folium.Map(location=[48.86, 2.34], zoom_start=12)
mc = folium.plugins.MarkerCluster()

#on retient les monuments pour lesquels il existe une latitude et une longitude
for nom in noms_random:
    lat = df['latitude'][df["nom_beneficiaire"]==nom].iloc[0]
    lon = df['longitude'][df["nom_beneficiaire"]==nom].iloc[0]
    mc.add_child(folium.Marker(location=[lat,lon], popup=(folium.Popup(nom, parse_html=True))))
                   
map_noms.add_child(mc)
map_noms


map_noms.save('map_noms.html')




app = Flask(__name__)

@app.route('/')
def index():
    map_noms = folium.Map(location=[48.86, 2.34], zoom_start=12)
    mc = folium.plugins.MarkerCluster()

    #on retient les monuments pour lesquels il existe une latitude et une longitude
    for nom in noms_random:
        lat = df['latitude'][df["nom_beneficiaire"]==nom].iloc[0]
        lon = df['longitude'][df["nom_beneficiaire"]==nom].iloc[0]
        mc.add_child(folium.Marker(location=[lat,lon], popup=(folium.Popup(nom, parse_html=True))))
                   
    map_noms.add_child(mc)
    map_noms.save('map.html')
    return render_template('index_new.html')

@app.route('/map')
def map():
    return render_template('7_map.html')

if __name__ == '__main__':
    app.run(debug=True)





