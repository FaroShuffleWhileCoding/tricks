
import pandas as pd
import streamlit as st


st.set_page_config(page_title="TRICKS", page_icon=":tophat:", layout="wide")

# ---- MAINPAGE ----
st.title(":tophat: TRICKS")

df_cat = pd.read_csv("tricks.csv").sort_values(by="CATEGORY", ascending=True)
df_magic = pd.read_csv("tricks.csv").sort_values(by="MAGICIAN", ascending=True)
df = pd.read_csv("tricks.csv")
# print(df)

# ---- SIDEBAR ----
st.sidebar.header("Filter Here:")

category = st.sidebar.multiselect("Select Category:", options=df_cat["CATEGORY"].unique(), key="cat")
magician = st.sidebar.multiselect("Select Magician:", options=df_magic["MAGICIAN"].unique(), key="magic")


if category is not None and magician == []:
    df_selection1 = df_cat.query("CATEGORY == @category")
    st.dataframe(df_selection1)

elif magician is not None and category == []:
    df_selection2 = df_magic.query("MAGICIAN == @magician")
    st.dataframe(df_selection2)

elif category is not None and magician is not None:
    df_selection3 = df.query("CATEGORY == @category & MAGICIAN == @magician")
    st.dataframe(df_selection3)


