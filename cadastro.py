import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, data, tipo):
    if nome and data <= date.today():
        st.session_state["Sucesso"] = True

        with open("clientes.csv", "a", encoding="UTF-8") as file:
            file.write(f"{nome}, {data}, {tipo} \n")
    else:
        st.session_state["Sucesso"] = False

st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="📟"
)

st.title("Cadastro de clientes")

st.divider()

nome = st.text_input("Digite o nome do cliente", 
                     key="nome_cliente")
data = st.date_input("Data de nascimento", 
                     format="DD/MM/YYYY")

tipo = st.selectbox("Tipo cliente",
                    options=["Física", "Juridica"])

btn_cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[nome, data, tipo])

if btn_cadastrar:
    if st.session_state["Sucesso"]:
        st.success("Cliente Cadastrado com sucesso")
    else:
        st.error("Falha ao cadastrar o cliente")