# titulo: Sistema de vendas
# Seção de cadastrar vendas
    #campo data
    #campo Vendedor
    #campo Produto
    #campo Valor
    #botão cadastrar venda
#Seção de vendas cadastradas
    #tabela com as vendas
#Seção dashboard
    #Card/Metricas -> faturamento total
    #Grafico de barras -> vendas por vendedor
    #Grafico de pizza -> vendas por produto

#pip install streamlit pandas plotly


#======================
#  Começo do projeto
#======================

import plotly.express as px
import streamlit as st
import pandas as pd

# carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")


#Título
st.title("Sistema de Vendas")
st.write("## Sistema de Vendas")


#seção de cadastro de vendas
st.sidebar.write("### Cadastro de Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["---Selecionar Vendedor---","Carla", "Bruno", "Ana"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

#logica de cadastro
if botao_cadastrar:
    if valor <= 0 or quantidade <= 0 or  vendedor == "---Selecionar Vendedor---" or produto == "":
        st.error("Todos os campos devem ser preenchidos.")
    else:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda Cadastrada com Sucesso")


#seção de visualização de vendas
st.write("### Vendas Cadastradas")
st.dataframe(tabela_vendas)


#seção de dashboard
st.write("### Dashboard")


#Card/Metricas -> faturamento total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")


#Grafico de barras -> vendas por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto", text_auto=True)
st.plotly_chart(grafico1)
#Grafico de pizza -> vendas por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole= 0.3)
st.plotly_chart(grafico2)
