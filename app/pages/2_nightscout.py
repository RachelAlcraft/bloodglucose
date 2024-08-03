import streamlit as st
import sys
from pathlib import Path
path = str(Path(__file__).parent.parent.absolute()) + "/src/"
sys.path.append(path)
import bloodglucose.Sources.NightScout as ns

st.set_page_config(
    page_title="bg",
    page_icon="🩸",
    layout="wide",
)

st.write(
    """
    # Retrive From NightScout
Retrieve data for analalysis and prediction from NightScount.
    """
)

my_url = st.text_input("Enter your nightscout url","https://truebell.herokuapp.com/")

tbCarbs, tbInsulin, tbRatio = st.tabs(["Carb Impact", "Insulin Impact", "Carb:Insulin Ratio"])

with tbCarbs:
    st.write("Create test data for carb impact")
    with st.expander("Carb Impact Test Instructions", expanded=False):
        st.write("""
        At this stage we are looking only at carbs, and the time of day and amount of carbs.  
        This will show how accelration of carbs and absorption time depends on amount and time.  
        In future: add time of month, temperature, protein fat etc

        The carb testing is as follows:  
        - carbs you had when IOB was 0 and COB was 0 (eg first thing in the morning)
        - time of day
        - how long you went without any more carbs or insulin.

        These are tests to build up a picture of carb absorption. 
        They may happen naturally if you have a hypo treatment at night.
        You can retrieve the blood glocse record from nightscout 
        and store the tests on your computer.  
        These tests can be hand done form other sources.
        """)
        
    cols = st.columns([2,2,2,2,2])
    with cols[0]:
        carbs = st.number_input("Carbs", 10)
    with cols[1]: 
        carb_date = st.date_input("Date")
    with cols[2]:
        carb_time = st.time_input("Time")
    with cols[3]:
        carb_length = st.number_input("Length (min)", 120)
    if st.button("Retrieve nightscout data"):
        print(")")
        bgs = ns.get_blood_glucose_date_time_length(my_url,carb_date,carb_time,carb_length)
        st.write(bgs)
    



with tbInsulin:
    st.write("Create test data for insulin impact")

with tbRatio:
    st.write("Create test data for carb:insulin ratio")
