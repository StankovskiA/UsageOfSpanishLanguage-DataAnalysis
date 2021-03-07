import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('contact_information.csv')
df.drop(columns=['Timestamp', 'Do have anything to add?'], inplace=True)
print(df.columns)
print(df.describe())
print(df.iloc[0])

plt.figure(figsize=(16,8))
plt.subplot2grid((2, 2), (0, 0))
df['Do you speak English?'].value_counts().plot(kind='bar', alpha=0.5)
plt.title('Do you speak English?')

plt.subplot2grid((2, 2), (0, 1))
df['Country'].value_counts().plot(kind='bar', alpha=0.5)
plt.title('Where are you from?')

plt.subplot2grid((2, 2), (1, 0))
df['Do you feel that you need to know another language except for the Spanish in order to communicate with people from Latin America?'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
plt.title('Do you need another language except Spanish to communicate with people from Latin America?')


plt.show()

plt.subplot2grid((3, 3), (0, 1))
df['Can you communicate in Spanish with people living in Brazil?'].value_counts().plot(kind='pie')
plt.ylabel('')
plt.xlabel('Can you communicate in Spanish with people living in Brazil?')


plt.subplot2grid((3, 3), (0, 0))
df['What is the share of people that speak the Spanish language in your country?'].value_counts().plot(kind='pie')
plt.ylabel('')
plt.xlabel('What is the share of people that speak the Spanish language in your country?')

plt.subplot2grid((3, 3), (0, 2))
df['Do you need to know the English language in order to have more work opportunities in Latin America? '].value_counts().plot(kind='pie')
plt.ylabel('')
plt.xlabel('Do you need to know English in order to have more work opportunities in Latin America? ')


plt.subplot2grid((3, 3), (1, 0))
df['Do you think that people living in Brazil have a full understanding of the Spanish language?'].value_counts().plot(kind='pie')
plt.ylabel('')
plt.xlabel('Do you think that people living in Brazil have a full understanding of the Spanish language?')


plt.subplot2grid((3, 3), (1, 2))
df['How much are you exposed to the U.S. culture in your everyday life?'].value_counts().plot(kind='pie')
plt.ylabel('')
plt.xlabel('How much are you exposed to the U.S. culture in your everyday life?')


plt.subplot2grid((3, 3), (2, 0))
df['How much did the globalization of the English language affected you?'].value_counts().plot(kind='pie')
plt.ylabel('')
plt.xlabel('How much did the globalization of the English language affected you?')


plt.subplot2grid((3, 3), (2,2))
df['How much is the Spanish language present in countries outside of Latin America ?'].value_counts().plot(kind='pie')
plt.ylabel('')
plt.xlabel('How much is the Spanish language present in countries outside of Latin America ?')

plt.show()