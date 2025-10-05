import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Flipply",
    page_icon="📦",
    layout="wide",
)

st.markdown("""
<div style="text-align:center;">
    <h1 style="color:#1f77b4;"> 📦 Flipply</h1>
    <h3>Snap the picture, get the right info, & start selling smarter!</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


st.markdown("<h3 style='text-align:center;'> What Flipply Solves</h3>", unsafe_allow_html=True)
col1a, col2a, col3a = st.columns(3)

with col1a:
    st.markdown("<h4 style='text-align:center;'>🗑️ Home Clutter</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align:center;'>54% of Americans are overwhelmed by the amount of clutter they have, and 78% have no idea what to do with it. Flipply simplifies the long process of researching the right price and description by just snapping a pic.</h6>", unsafe_allow_html=True)

with col2a:
    st.markdown("<h4 style='text-align:center;'>📱 E-Commerce</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align:center;'>E-Bay is considerbly the most important e-commerce platform for second-hand products. Important to consider that $27 trillion USD  sales in 2022E-bay: Considerably the most important second-hand e-commerce company.</h6>", unsafe_allow_html=True)

with col3a:
    st.markdown("<h4 style='text-align:center;'>♻️ Sustainability</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align:center;'>Giving a second-use to all those items laying in the garage not only extends its lifecycle, but empowers a more sustainable future</h6>", unsafe_allow_html=True)



st.markdown("---")
st.markdown("<h3 style='text-align:center;'> How Flippy Works</h3>", unsafe_allow_html=True)
st.markdown("""
1. Take a picture or upload an image of the item you want to sell  
2. Flipply sends the image to Gemini to analyze it and give a description about it, such as brand and condition
4. E-Bay API is used to predict its best selling price  
5. The Gemini-given information can still be edited by the user to prevent unchangable errors
3. Post the item on eBay and other e-commerce platfroms to start selling faster and easier
""")
st.markdown("[View our GitHub Repository](https://github.com/m3l0x42/HackHarvard/tree/main) 🔗")

images = [
    "assets/hh1.jpg",
    "assets/hh2.jpg",
    "assets/hh3.jpg",
    "assets/hh4.jpg",
    "assets/hh5.jpg",
]

st.write("")
cols = st.columns(len(images))
for i, col in enumerate(cols):
    col.image(images[i], width=280)
st.markdown("---")

st.markdown("<h3 style='text-align:center;'> Watch Flipply in Action</h3>", unsafe_allow_html=True)
st.video("https://youtube.com/shorts/Uk-AElb4aac")

st.markdown("---")


st.markdown("<h3 style='text-align:center;'> Features</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h4 style='text-align:center;'>📸 Image Recognition</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align:center;'>Snap or upload a picture - Gemini recognizes item</h6>", unsafe_allow_html=True)

with col2:
    st.markdown("<h4 style='text-align:center;'>💵 Price Prediction</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align:center;'>The most balanced eBay price is predicted</h6>", unsafe_allow_html=True)

with col3:
    st.markdown("<h4 style='text-align:center;'>⚡Fast & Easy</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align:center;'>Upload, predict, and sell in a matter of a quick pic</h6>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style="text-align:center; margin-top:20px;">
    <h2>Want to start flipping?</h2>
    <a href="https://github.com/m3l0x42/HackHarvard/tree/main" target="_blank">
        <button style="
            background-color:#1f77b4;
            color:white;
            padding:10px 20px;
            font-size:20px;
            border:none;
            border-radius:6px;
            cursor:pointer;">Coming Soon</button>
    </a>
</div>
""", unsafe_allow_html=True)
