import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('listings_cleaned.csv')
print(df.shape)
print(df.info())
print(df.head())
print(df.describe())
print(df.groupby('neighbourhood_group_cleansed')['price'].agg(['mean','median','count']).sort_values('mean', ascending=False))
print(df.groupby('room_type')['price'].agg(['mean','median','count']).sort_values('mean', ascending=False))
# Superhost impact
print(df.groupby('host_is_superhost')[['price','review_scores_rating','number_of_reviews']].mean().round(2))

# Availability distribution
print(df['availability_365'].describe())

# Price vs Review Score correlation
print(df[['price','review_scores_rating','number_of_reviews']].corr())

# Room type x Region pivot table
pivot = df.pivot_table(values='price', index='neighbourhood_group_cleansed', columns='room_type', aggfunc='mean')
print(pivot.round(1))