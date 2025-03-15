import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt #GUI
from IPython.display import display

# Überprüfen, ob seaborn den diamonds-datensatz enthält
try:
    df = sns.load_dataset('diamonds')
except ValueError:
    print("Fehler: Der Datensatz Diamonds ist nicht in Seaborn verfügbar.")
    exit()

# Überblick über die Daten
display(df.head())
print(df.info())

# Grundlegende Statistiken
print(df.describe())

# Preisverteilung visualisieren
plt.figure(figsize=(10, 5))
sns.histplot(df['price'], bins=50, kde=True)
plt.title('Verteilung der Diamantenpreise')
plt.xlabel('Karat')
plt.ylabel('Preis in USD')
plt.show()

# Durchschnittspreise pro Reinheit
plt.figure(figsize=(10, 5))
sns.boxplot(x='clarity', y='price', data=df, order=sorted(df['clarity'].unique()))
plt.title('Diamantenpreis nach Reinheit')
plt.xlabel('Reinheit')
plt.ylabel('Preis in USD')
plt.show()

