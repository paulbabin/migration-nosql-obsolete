import streamlit as st
import pandas as pd

# Définition de la fonction de la page d'accueil
def home_page():
    st.title("Bienvenue sur ma première application web moderne")
    st.write("Cette application est designée pour la plateforme Apple (Streamlit)")

# Définition de la fonction de la page de contact
def contact_page():
    st.title("Contact")
    st.write("Pour contacter nous, vous pouvez nous écrire à : contact@exemple.com")
    st.write("N'hésitez pas à nous écrire si vous avez des questions ou des suggestions!")

# Définition de la fonction principale de l'application
def main():
    # Définition des pages de l'application
    pages = {
        "Accueil": home_page,
        "Contact": contact_page
    }
    
    # Sélection de la page à afficher
    selected_page = st.sidebar.selectbox("Menu", pages.keys())
    pages[selected_page]()

# Execution de la fonction principale
if __name__ == "__main__":
    main()