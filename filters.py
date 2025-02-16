import streamlit as st

def apply_filters(df):
    """Aplica filtros ao dataset."""
    st.sidebar.image('assets/titanic-image.jpg')
    st.sidebar.header("Filtros")
    pclass_filter = st.sidebar.multiselect("Selecione a Classe", options=df['Pclass'].unique(), default=df['Pclass'].unique())
    sex_filter = st.sidebar.radio("Selecione o Sexo", options=['Todos'] + list(df['Sex'].unique()), index=0)
    age_range = st.sidebar.slider("Selecione a Faixa Etária", int(df['Age'].min()), int(df['Age'].max()), (int(df['Age'].min()), int(df['Age'].max())))
    
    df_filtered = df[df['Pclass'].isin(pclass_filter)]
    if sex_filter != 'Todos':
        df_filtered = df_filtered[df_filtered['Sex'] == sex_filter]
    df_filtered = df_filtered[(df_filtered['Age'] >= age_range[0]) & (df_filtered['Age'] <= age_range[1])]
    
    return df_filtered