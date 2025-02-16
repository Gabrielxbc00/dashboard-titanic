# Nome do Grupo: Gabriel Ximenes Bezerra Carrazoni (gxbc@cesar.school)

import streamlit as st
import plotly.express as px
from data_processing import load_data
from filters import apply_filters

# Configuração da página
st.set_page_config(page_title='Dashboard Titanic', layout='wide')

df = load_data()
df_filtered = apply_filters(df)

# Título do dashboard
st.title('🚢 Dashboard - Titanic')

# Gráfico 1: Taxa de Sobrevivência por Classe
df_survival_pclass = df_filtered.groupby('Pclass')['Survived'].mean().reset_index()
df_survival_pclass['Survived'] *= 100
fig1 = px.bar(df_survival_pclass, x='Pclass', y='Survived', text=df_survival_pclass['Survived'].apply(lambda x: f'{x:.1f}%'), 
              title='🎟️ Taxa Média de Sobrevivência por Classe', labels={'Pclass': 'Classe', 'Survived': 'Taxa de Sobrevivência (%)'},
              color='Survived', color_continuous_scale='Blues')
st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Distribuição de Idade por Sobrevivência
fig2 = px.histogram(df_filtered, x='Age', color='Survived', nbins=30,
                    title='👶🧑👴 Distribuição de Idade por Sobrevivência',
                    labels={'Age': 'Idade', 'Survived': 'Sobrevivência'},
                    marginal='box', color_discrete_map={0: 'orange', 1: 'blue'})
st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Impacto do Sexo na Sobrevivência
df_survival_sex = df_filtered.groupby('Sex')['Survived'].mean().reset_index()
df_survival_sex['Survived'] *= 100
fig3 = px.bar(df_survival_sex, x='Sex', y='Survived', text=df_survival_sex['Survived'].apply(lambda x: f'{x:.1f}%'),
              title='🧑‍🤝‍🧑 Impacto do Sexo na Sobrevivência', labels={'Sex': 'Sexo', 'Survived': 'Taxa de Sobrevivência (%)'},
              color='Sex', color_discrete_sequence=['#ff8c00', '#4682b4'])
st.plotly_chart(fig3, use_container_width=True)

# Container de insights
with st.expander("📊 Insights sobre os dados"):
    st.markdown("- 🚀 Passageiros da **1ª classe** tiveram maior taxa de sobrevivência.")
    st.markdown("- 👩 Mulheres tiveram maior chance de sobrevivência do que homens.")
    st.markdown("- 👶 Crianças tiveram maior taxa de sobrevivência devido à política de evacuação.")
    st.markdown("- 🧑‍🤝‍🧑 **O sexo foi um fator determinante na sobrevivência, com mulheres tendo uma taxa muito superior à dos homens.**")

# Rodapé
st.markdown("---")
st.markdown("**Dashboard desenvolvido com Streamlit por Gabriel Ximenes Bezerra Carrazzoni** | Dados do Titanic 🚢")
