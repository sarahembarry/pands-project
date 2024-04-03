

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np



df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

summary= df.describe(include='all')

with open("summaryofvariables.txt", "w") as f:
    f.write(summary.to_string())



df.hist(column='sepal_length', color='blue')
plt.savefig('sepal_length_histogram.png')

df.hist(column='sepal_width', color='blue')
plt.savefig('sepal_width_histogram.png')

df.hist(column='petal_length', color='blue')
plt.savefig('petal_length_histogram.png')


df.hist(column='petal_width', color='blue')
plt.savefig('petal_width_histogram.png')


species_counts = df['species'].value_counts()

plt.bar(species_counts.index,species_counts.values, color='blue')
plt.title('Number of Iris Flowers by Species')
plt.xlabel('Species of Iris Flower')
plt.ylabel('Count of Iris Flowers')

plt.savefig('species_barchart.png')

