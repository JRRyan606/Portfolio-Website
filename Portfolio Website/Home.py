import streamlit as st
import pandas


st.set_page_config(page_title="Home", layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/image-3.png")

with col2:
    st.title("Justin Ryan")
    content = """
   Hi, I'm Justin! I'm 15 years old. I'm well-versed in Python. I have experience troubleshooting and debugging code. I've had the opportunity to work on a variety of Python projects, totaling 20 in all, which showcase my Python skills. On Aug 25, 2023, I took the Pearson Python Entry Level Test (PCEP 30-02) and I'm eagerly waiting for the results, hoping I did well. Below are my 20 Python Projects.
    """
    st.info(content)

content2 = """
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
