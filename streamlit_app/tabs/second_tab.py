import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sqlite3,sqlalchemy
from sqlalchemy import inspect,create_engine,table,text

con = sqlite3.connect('/home/moustapha/Desktop/ProjetPerso/projetsql/mini_sql_project/data/imdb.db', check_same_thread=False)
engine=create_engine('sqlite:////home/moustapha/Desktop/ProjetPerso/projetsql/mini_sql_project/data/imdb.db',echo=True)
conn=engine.connect() 
cur = con.cursor()
inspector=inspect(engine)
Liste = inspector.get_table_names()

title = "Requêtes et Dataviz"
sidebar_name = "Requêtes et Dataviz"

def run():

    st.title(title)

    

    st.markdown(
        """
        **Analyse des tables et de leurs attributs.**
        """
    )

    choice = st.selectbox(label="Choisissez une table pour afficher ses attributs",options =Liste)
    if st.button("Afficher les attributs de la table"):
        st.write(inspector.get_columns(table_name=choice))

    

    st.markdown(
        """
        **Les 50 titres les mieux notés parmis ceux qui ont au mois 5000 votants**

        """
    )
    meilleurs_titres=pd.read_csv('/home/moustapha/Desktop/ProjetPerso/projetsql/mini_sql_project/data/50_meilleurs_titres.csv')
    


    st.dataframe(meilleurs_titres)

    
    
    st.markdown("""
     **Liste des films dans lequel une personne a travaillé en tant que actrice ou membre de la production.**
     """
    )
    nom=st.text_input('Choisissez le nom de la personne')
    prenom=st.text_input('Choisissez le prénom de la personne')
    nom=str(nom)
    prenom=str(prenom)

    stmt1= "SELECT primary_title FROM ((SELECT *  FROM 'titles' WHERE type like '%movie%') AS A INNER JOIN (SELECT * FROM 'crew' ) AS B ON A.title_Id=B.title_Id) AS C INNER JOIN (SELECT * FROM 'people' WHERE name LIKE '%"+nom+"%' AND name LIKE '%"+prenom+"%') AS D ON D.person_Id=C.person_Id"
    cur.execute(stmt1)
    Liste_titre = cur.fetchall()
    Liste_titre= pd.DataFrame(Liste_titre, columns = ['Titre'])
    if st.button("Afficher les films"):
        st.write(Liste_titre)


    st.markdown(
        """
        **Nombre de titres par type**

        """
    )
    
    titres_par_type=pd.read_csv('/home/moustapha/Desktop/ProjetPerso/projetsql/mini_sql_project/data/nombre_de_titre_par_type.csv',index_col='type')
    


    

    st.bar_chart(titres_par_type['nombre de titres'])
    st.markdown(
        """
        On a logiquement plus de titres pour les séries, chaque épisode d'une serie avec son titre.
        """
    )
    st.markdown(
        """
        **Les dix genres ayant obtenus une meilleure note moyenne**
        """
    )
    notes_par_genre=pd.read_csv('/home/moustapha/Desktop/ProjetPerso/projetsql/mini_sql_project/data/note_moyenne_par_genre.csv')
    st.dataframe(notes_par_genre)


    

