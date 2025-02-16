import pandas as pd

def load_data():
    """Carrega e trata os dados do Titanic."""
    df = pd.read_csv('assets/titanic.csv')
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    df.drop(columns=['Cabin'], inplace=True)
    df.drop_duplicates(inplace=True)
    return df