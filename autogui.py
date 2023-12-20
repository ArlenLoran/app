import streamlit as st
import pandas as pd
import datetime
import sqlite3

conn = sqlite3.connect('usuarios.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, usuario TEXT, senha TEXT, status TEXT)")

st.set_page_config(page_title="Teste Arlen")

st.write("testeee")

entrada = st.date_input("input data", datetime.date(2019, 7, 6))

entrada2 = st.text_input("testeeee")

conn = sqlite3.connect('usuarios.db')
c = conn.cursor()
c.execute("SELECT * FROM users")
tr = c.fetchall()

def printing():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("INSERT INTO users ('email', 'usuario', 'senha', 'status') VALUES (?,?,?,?)",
              (entrada, entrada, entrada, entrada))
    conn.commit()

def printing2():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    entrada2 = c.fetchall()


st.button("ok", on_click=printing)

st.button("pegar", on_click=printing2)

st.table(tr)
