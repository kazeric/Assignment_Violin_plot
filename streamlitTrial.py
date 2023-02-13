import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('gapminder_with_codes.csv')

data_2007=data[data['year']==2007]

fig = plt.figure(figsize=(9,7))
plt.title("LIFE EXPECTANCY")
sns.violinplot(data=data_2007,x='lifeExp',scale='count')
st.pyplot(fig)

fig = plt.figure(figsize=(9,7))
plt.title("POPULATION")
sns.violinplot(data=data_2007,x='pop',scale='count')
st.pyplot(fig)

fig = plt.figure(figsize=(9,7))
plt.title("hello again")
sns.violinplot(data=data_2007,x='gdpPercap',scale='count')
st.pyplot(fig)

fig = plt.figure(figsize=(9,7))
plt.title("hello again")
sns.violinplot(data=data_2007,x='lifeExp', y='continent',scale='count')
st.pyplot(fig)

fig = plt.figure(figsize=(9,7))
plt.title("hello again")
sns.violinplot(data=data_2007,x='pop',y='continent',scale='count')
st.pyplot(fig)

fig = plt.figure(figsize=(9,7))
plt.title("hello again")
sns.violinplot(data=data_2007,x='gdpPercap',y='continent',scale='count')
st.pyplot(fig)