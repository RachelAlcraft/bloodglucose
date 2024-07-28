import streamlit as st
from bloodglucose import ClassCurves as cc
import random

st.set_page_config(
    page_title="bg",
    page_icon="🩸",
    layout="wide",
)

st.title("Exampled hooked up to pypi lib")

tabEg, tabCode = st.tabs(["Example", "Code"])


with tabEg:
    if st.button("Press to randomly make a curve"):
        inta = int(random.random() * 100)
        intb = int(random.random() * 100)
        intc = int(random.random() * 100)
        sq = cc.Quadratic(inta, intb, intc)
        ys = sq.get_ys([0, 1, 2, 3])
        st.write(f"y={inta}x^2 + {intb}x + {intc}")
        st.write(f"0,1,2,3={ys}")


with tabCode:
    st.code("pip install bloodglucose")
    st.code(
        """
        from bloodglucose import ClassCurves as cc
        import random
        inta = int(random.random() * 100)
        intb = int(random.random() * 100)
        intc = int(random.random() * 100)
        sq = cc.Quadratic(inta, intb, intc)
        ys = sq.get_ys([0, 1, 2, 3])
        print(f"y={inta}x^2 + {intb}x + {intc}")
        print(f"0,1,2,3={ys}")

        """
    )
