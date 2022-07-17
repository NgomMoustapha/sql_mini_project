import streamlit as st


title = "Introduction : Mini-Projet SQL"
sidebar_name = "Introduction"


def run():

    st.markdown("---")

    st.title(title)

    st.markdown("---")

    st.subheader('Language SQL')

    st.markdown(
        """
        **Ce streamlit a pour but de mettre en avant les bases que j'ai acquise au cours de ma certification SQL. 
        La page suivante montre une illustration des requêtes ,qui ont déja été faites en local, transformées en Data Frame, puis transportées sur Github.
        J'ai abordé des concepts fondamentaux de requêtages. 
        J'ai utilisé SQL Alchemy qui est une librairie Python très utilisée pour se connecter à un système de gestion de bases de données relationnelles. Il permet d'interpréter du code SQL.
        Le notebook Python est disponible sur Github.**

        """

    )
    st.header("La base de données")

    st.markdown(
        """
        J'utilise la base de données imdb disponible en Open Source: https://www.imdb.com/interfaces/. 

    
        """
    )
