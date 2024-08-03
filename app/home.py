import streamlit as st
import sys
from pathlib import Path
path = str(Path(__file__).parent.parent.absolute()) + "/src/"
sys.path.append(path)


st.set_page_config(
    page_title="bg",
    page_icon="🩸",
    layout="wide",
)

st.header("BLOODGLUCOSE")
st.write(
    "**A template library to demonstrate good practice for a scientific python library.**"
)
st.write(
    """
    This is written as a project in collaboration with my dual self, between:
    - A PhD at Birkbeck College, London University :copyright: 2024
    - As a Research Software Engineer at the Inctitute of Cancer Research :copyright: 2024
    """
)
st.write("---")
st.write(
    """
Acknowledgement goes to my supervisor [Dr Mark Williams](https://www.bbk.ac.uk/our-staff/#overview)
for unwaiveringly positive support despite my meandering.
"""
)
st.write("---")
