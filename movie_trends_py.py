# -*- coding: utf-8 -*-
"""Movie trends.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16lYJ7IF6d83S4ziV9si1Oq3bUIBpwMe_
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# sample Bollywood Movie Data (replace with real data from imdb or other source)
data= {
    'movie_title':['Movie A','Movie c','Movie D','Movie c','Movie D','Movie E','Movie F','Movie G','Movie H','Movie I','Movie J'],
    'genre': ['Action','Romance','Comedy','Drama','Action','Comedy','Romance','Thriller','Drama','Action','Romance'], # Added 'Romance' to match length
    'release_year':[2023, 2022, 2023, 2021, 2022, 2023, 2020, 2022, 2021, 2023,2020], # Added 2020 to match length
    'box_office_crores': [150, 88, 120, 60, 200, 100, 90, 70, 50, 188,200], # Added 200 to match length
    'lead_actor':['Actor X','Actor Y','Actor Z','Actor X','Actor Y','Actor Z','Actor X','Actor Y','Actor Y','Actor X','Actor Z'], # Added 'Actor Z' to match length

}


bollywood_df = pd.DataFrame(data)

#1. Basic Data Exploration
print(bollywood_df.head())
print(bollywood_df.info())

#2.Genre Anatysis
genre_counts = bollywood_df['genre'].value_counts()
print("\nMovie count by Genre:\n", genre_counts)

#3. Box Office Collection by Genre
box_office_by_genre = bollywood_df.groupby('genre')['box_office_crores'].sum()
print("\n Total Box office collection by Genre:\n",box_office_by_genre)

#4. Lead actor Analysis
lead_actor_box_office = bollywood_df.groupby('lead_actor')['box_office_crores'].sum()
print("\n Total Box office collection by lead Actor:\n",lead_actor_box_office)

#1. Bar Chart of Movie Count by Genre
plt.figure(figsize=(10, 6))
sns.countplot(x='genre', data=bollywood_df)
plt.title('Number of Movie by Genre')
plt.xlabel('Genre')
plt.ylabel('Number of Movie')
plt.show()

#2. Pie Chart of Box Office Collection by Genre
plt.figure(figsize=(8, 8))
plt.pie(box_office_by_genre, labels=box_office_by_genre.index, autopct='%1.f%%', startangle=140) # Changed 'lables' to 'labels'
plt.title('Box office collection by Genre')
plt.show()