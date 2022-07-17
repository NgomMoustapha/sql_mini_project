import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image



title = "Requêtes et Dataviz"
sidebar_name = "Requêtes et Dataviz"

def run():

    st.title(title)

    

    st.markdown(
        """
        ***Analyse des tables et de leurs attributs.***
        """
    )

    choice = st.selectbox(label="Choisissez une table pour afficher ses attributs",options =['akas','crew','episodes','people','ratings','titles'])

    if st.button("Afficher les attributs de la table"):
        table_affiche=pd.read_csv(""+choice+".csv")
        st.dataframe(table_affiche)

    st.markdown(
        """
        ***-------------------------------------------------------------------------------------------------------------------------------------------***
        """
    )

    st.markdown(
        """
        **Les 50 titres les mieux notés parmis ceux qui ont au mois 5000 votants**

        """
    )
    meilleurs_titres=pd.read_csv('50_meilleurs_titres.csv')
    


    st.dataframe(meilleurs_titres)

    st.markdown(
        """
        ***-------------------------------------------------------------------------------------------------------------------------------------------***
        """
    )
    
    st.markdown("""
     **Liste des films dans lequel ces 3 personnes ont participé.**
     """
    )


    choice2 = st.selectbox(label="Choisissez une table pour afficher ses attributs",options =['Denzel_Washington','Quentin_Tarantino','George_Clooney'])

    if st.button("Afficher les films"):
        table_affiche2=pd.read_csv(""+choice2+".csv")
        st.dataframe(table_affiche2)
    
    st.markdown(
        """
        ***-------------------------------------------------------------------------------------------------------------------------------------------***
        """
    )
    st.markdown(
        """
        **Nombre de titres par type**

        """
    )
    
    titres_par_type=pd.read_csv('nombre_de_titre_par_type.csv',index_col='type')
    


    

    st.bar_chart(titres_par_type['nombre de titres'])
    st.markdown(
        """
        On a logiquement plus de titres pour les séries, chaque épisode d'une serie avec son titre.
        """
    )

    st.markdown(
        """
        ***-------------------------------------------------------------------------------------------------------------------------------------------***
        """
    )
    
    st.markdown(
        """
        **Les dix genres ayant obtenus une meilleure note moyenne**
        """
    )
    notes_par_genre=pd.read_csv('note_moyenne_par_genre.csv')
    st.dataframe(notes_par_genre)


    

