# CodeAlpha Task 2: Unemployment Analysis with Python
# By Rakshitha R

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('Unemployment in India.csv')

# Data Cleaning
df.columns = df.columns.str.strip()
print(df.head())
df.dropna(inplace=True)

# Date conversion
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
df['Month'] = df['Date'].dt.month

# 1. Trend Over Time
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Estimated Unemployment Rate (%)'])
plt.title('Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.show()

# 2. Covid Impact
before = df[df['Date'] < '2020-03-01']['Estimated Unemployment Rate (%)'].mean()
after = df[df['Date'] >= '2020-03-01']['Estimated Unemployment Rate (%)'].mean()
print(f"Before Covid: {before:.2f}%")
print(f"After Covid: {after:.2f}%")

# 3. Region wise
plt.figure(figsize=(12,5))
sns.barplot(x='Region', y='Estimated Unemployment Rate (%)', data=df, estimator='mean')
plt.xticks(rotation=90)
plt.title('Region wise Unemployment')
plt.show()

# 4. Rural vs Urban
plt.figure(figsize=(6,4))
sns.barplot(x='Area', y='Estimated Unemployment Rate (%)', data=df)
plt.title('Rural vs Urban')
plt.show()

# 5. Seasonal Trends
plt.figure(figsize=(10,4))
sns.boxplot(x='Month', y='Estimated Unemployment Rate (%)', data=df)
plt.title('Monthly Trends')
plt.show()
