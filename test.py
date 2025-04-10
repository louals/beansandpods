import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix

def load_data():
    df = pd.read_csv("BeansDataSet.csv") 
    return df

df = load_data()



df.rename(columns={"Région": "Region"}, inplace=True)

st.title("Analyse des Ventes - Beans & Pods")


st.subheader("Aperçu des données")
st.dataframe(df.head())


st.subheader("Statistiques descriptives")
st.write(df.describe())


st.subheader("Comparaison des ventes par canal")
fig, ax = plt.subplots()
sns.boxplot(x="Channel", y="Robusta", data=df, ax=ax)
st.pyplot(fig)


st.subheader("Répartition des ventes par région")
fig, ax = plt.subplots()
sns.countplot(x="Region", data=df, ax=ax)
st.pyplot(fig)


st.subheader("Ventes des différents types de café")
fig, ax = plt.subplots(figsize=(10,5))
df[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].sum().plot(kind='bar', ax=ax)
plt.ylabel("Total des ventes")
st.pyplot(fig)


st.subheader("Corrélation entre les ventes de produits")
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(df[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)


st.subheader("Histogrammes des ventes de produits")
fig, ax = plt.subplots(figsize=(10,6))
df[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].hist(bins=15, figsize=(15,10), ax=ax)
st.pyplot(fig)


st.subheader("Graphiques de densité des ventes")
fig, ax = plt.subplots(figsize=(10,6))
df[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].plot(kind='density', ax=ax)
st.pyplot(fig)

st.subheader("Matrice de dispersion des ventes")
fig, ax = plt.subplots(figsize=(25, 25))
scatter_matrix(df[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']], figsize=(25, 25), c='g', ax=ax)
plt.suptitle("Matrice de Dispersion des Ventes des Produits", fontsize=16)
st.pyplot(fig)


st.subheader("Recommandations Marketing")
st.write("- Investir dans les ventes en ligne car elles montrent une meilleure rentabilité pour optimiser les ventes ")
st.write("- Cibler les régions avec les ventes les plus faibles dans le sud et le centre avec des promotions spécifiques.")
st.write("- Augmenter la publicité sur les produits les plus populaires. Comme Robusta , Arabica et eEsspresso ")



st.subheader("Données supplémentaires recommandées")
st.write("- Collecter des données sur la fidélité des clients.")
st.write("- Suivre les tendances de prix et leur impact sur les ventes.")
st.write("- Enregistrer les données démographiques des clients pour un meilleur ciblage marketing.")
