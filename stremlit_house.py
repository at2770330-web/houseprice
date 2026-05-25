from pyexpat import features

from altair import Predicate
import streamlit as st
import pandas as pd
import numpy as np
import pickle

from streamlit import button
model=pickle.load(open("house_model.pkl","rb"))
st.title("house  price predictor ")
size=st.number_input("enter the house price Sq.ft",min_value=50,max_value=5000)
bedrooms=st.slider("number of bedrooms:",1,6)
if button("Predict"):
    features=np.array([[size,bedrooms]])
    prediction=model.predict(features)[0]
    st.success(f"Predict price:{prediction:,.2f}")
    