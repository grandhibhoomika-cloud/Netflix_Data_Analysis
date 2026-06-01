import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("Dataset loaded successfully")

# Clean data
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unknown')

sns.set(style="whitegrid")

# ===== GRAPH 1: Movies vs TV Shows =====
plt.figure(figsize=(6,4))
df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.show()

# ===== GRAPH 2: Top Countries =====
plt.figure(figsize=(10,5))
df['country'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Countries")
plt.show()

# ===== GRAPH 3: Ratings =====
plt.figure(figsize=(10,5))
df['rating'].value_counts().plot(kind='bar')
plt.title("Ratings Distribution")
plt.show()

print("ALL GRAPHS DONE 🚀")