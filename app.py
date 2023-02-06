import streamlit as st

import streamlit as st
from streamlit_option_menu import option_menu

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
               height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
            """

def read(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        return lines

with st.sidebar:
    selection_screen = option_menu("Food in the UK", ["Home", "Shakshuka", "Harcha", "Mint Tea"],
                                   icons=["house", "egg-fried", "mouse3", "cup"],
                                   menu_icon="basket")

if selection_screen == "Home":
    st.title("Home")
    st.image("./text/mint.jpg")


elif selection_screen == "About":
    st.title("About")

elif selection_screen == "Shakshuka":
    st.title("Shakshuka")
    st.markdown("#### Shakshuka is a popular Mediterranean dish that consists of eggs cooked in a flavorful tomato sauce with spices and vegetables. Originating from North Africa, it is now a staple in many Middle Eastern and Mediterranean households. The dish is typically served for breakfast or brunch and can be customized with various ingredients such as bell peppers, onions, and feta cheese. It's a simple, yet satisfying meal that is easy to make and can be enjoyed by people of all ages. Whether you're looking for a healthy, protein-packed breakfast or a flavorful and hearty lunch, shakshuka is the perfect dish for you.")
    
    col_1, col_2 = st.columns(2)
    with col_1:
        st.image("./text/shak_1.jpg", width=360)
    with col_2:
        st.image("./text/shak#.jpg", width=360)
    

elif selection_screen == "Harcha":
    st.title("Harcha")
    st.markdown("#### Harcha is a traditional Moroccan dish made from semolina flour, butter, and milk or water. It is a type of flatbread that is crispy on the outside and soft on the inside, with a unique texture that sets it apart from other breads. Harcha is often enjoyed for breakfast or as a snack and is typically served with honey, jam, or cheese. The bread can be cooked on a griddle or in a pan, making it an easy and accessible dish for anyone to prepare. Its versatility and delicious flavor have made it a staple in Moroccan cuisine, and it is now enjoyed by people all over the world. Whether you're looking for a simple, tasty bread to accompany your meal or an exotic twist on your breakfast routine, harcha is the perfect dish to try.")
    col_1, col_2 = st.columns(2)
    with col_1:
        st.image("./text/har_1.jpg", width=360)
    with col_2:
        st.image("./text/harch.jpg", width=360)

elif selection_screen == "Mint Tea":
    st.title("Mint Tea")
    st.markdown("#### Moroccan mint tea is a traditional beverage that is loved for its refreshing flavor and cultural significance. Made from green tea leaves, sugar, and fresh mint leaves, it is the most popular drink in Morocco and is commonly served to guests as a sign of hospitality. The preparation of Moroccan mint tea is an intricate and ceremonial process that involves pouring the tea from a height to aerate it and create a frothy texture. This not only adds to the taste of the tea but also serves as a symbol of generosity and good will. Whether you're looking to beat the heat on a hot day or experience a taste of Moroccan culture, Moroccan mint tea is a must-try. Its refreshing and invigorating flavor makes it a perfect drink for any time of day.")
    col_1, col_2 = st.columns(2)
    with col_1:
        st.image("./text/mint_1.jpg", width=360)
    with col_2:
        st.image("./text/mint_2.jpg", width=360)
