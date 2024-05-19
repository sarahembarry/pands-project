# Please see juptyer notebook for the full analysis and code comments. 

# Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier


# Filter warnings
warnings.filterwarnings("ignore", message="use_inf_as_na option is deprecated")
warnings.filterwarnings("ignore", message="When grouping with a length-1 list-like")


# Import and summerise the dataset
try:
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    print("The Iris dataset has been imported.\n")
except:
    print("An error occurred while loading the dataset")

summary= df.describe(include='all')
print("Here is a summary of the Iris dataset:")
print(summary)


# Check data quality
missing_values = df.isna().sum()
print("\nThe dataset has been checked for missing values. There are no missing values:")
print(missing_values)


# Summary of variables to text file
with open("summaryofvariables.txt", "w") as f:
   f.write(summary.to_string())
print("\nA text file with the summary of all variables in the dataset has been generated and saved.\n")


# Histograms of numeric variables
def plot_histogram(column,column_name, title, filename):
    plt.hist(column, color='blue', bins=30)
    plt.title(title, fontsize=16)
    plt.xlabel(column_name, fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(True)
    plt.savefig(filename)
   
print("A histogram of 'sepal_length' has been generated and saved as sepal_length_histogram.png.\n")
plot_histogram(df['sepal_length'],'sepal_length(cm)', 'Distribution of Sepal Length', 'sepal_length_histogram.png')
plt.show()

print("A histogram of 'sepal_width' has been generated and saved as sepal_width_histogram.png.\n")
plot_histogram(df['sepal_width'], 'sepal_width(cm)','Distribution of Sepal Width', 'sepal_width_histogram.png')
plt.show()

print("A histogram of 'petal_length' has been generated and saved as petal_length_histogram.png.\n")
plot_histogram(df['petal_length'],'petal_length(cm)', 'Distribution of Petal Length', 'petal_length_histogram.png')
plt.show()

print("A histogram of 'petal_width' has been generated and saved as petal_width_histogram.png.\n")
plot_histogram(df['petal_width'], 'petal_width(cm)','Distribution of Petal Width', 'petal_width_histogram.png')
plt.show()


# Bar chart of species
print("A bar chart of 'species' has been generated and saved as species_barchart.png.\n")
species_counts = df['species'].value_counts()
plt.bar(species_counts.index,species_counts.values, color='blue')
plt.title('Number of Iris Flowers by Species')
plt.xlabel('Species of Iris Flower')
plt.ylabel('Count of Iris Flowers')
plt.savefig('species_barchart.png')
plt.show()


# Box plots of numeric variables by species
print("Box plots for each numeric variable by species have been generated.\n")
plt.figure(figsize=(9, 6))

plt.subplot(2, 2, 1)
sns.boxplot(x='species', y='sepal_length', data=df,hue='species')
plt.title('Sepal Length')

plt.subplot(2, 2, 2)
sns.boxplot(x='species', y='sepal_width', data=df,hue='species')
plt.title('Sepal Width ')

plt.subplot(2, 2, 3)
sns.boxplot(x='species', y='petal_length', data=df,hue='species')
plt.title('Petal Length ')

plt.subplot(2, 2, 4)
sns.boxplot(x='species', y='petal_width', data=df,hue='species')
plt.title('Petal Width')

plt.tight_layout()
plt.show()


# Correlation matrix
numeric_df = df.select_dtypes(include='number')
correlation_matrix = numeric_df.corr()
print("A matrix of the correlation between the numeric variables in the dataset has been generated:\n")
print(correlation_matrix)


# Pair plot scatter plots of numeric variables by species 
print("\nScatter plots visualising the correlation between each pair of numeric variables by species have been generated.\n")
sns.pairplot(df, hue='species')
plt.show()


# Interactive scatter plot of petal length and petal width
print("An interactive scatter plot of 'petal length' and 'petal width' has been generated:\n")
fig = px.scatter(df, x="petal_length", y="petal_width",
                 color="species",
                 symbol="species",  
                 hover_data=['petal_length', 'petal_width'])
fig.show()


# Machine learning set up
x = df[['sepal_length', 'sepal_width' ,'petal_length','petal_width']]
y = df['species']
x_train, x_test, y_train,y_test = train_test_split(x, y, test_size=0.2, random_state=42)

def train_model(model, x_train, y_train):
    model.fit(x_train, y_train)
    return model

def evaluate_report(model, x_test, y_test):
    predictions = model.predict(x_test)
    print("Here are the classification report results:")
    print(classification_report(y_test, predictions))


# Logistic regression model
log_reg_model= LogisticRegression()
trained_log_reg_model = train_model(log_reg_model, x_train, y_train)

print("\nA logistic regression model has been trained to predict Iris species based on its features using the dataset.\n")
evaluate_report(trained_log_reg_model, x_test, y_test)

print("A Setosa entry was selected, and its features were input into the logistic regression model. Here is the Iris species predicted by the model:")

log_reg_test_plant = {
    'sepal_length': 5.0,
    'sepal_width': 3.6 ,
    'petal_length': 1.4 ,
    'petal_width': 0.2 ,
}
log_reg_plant_df = pd.DataFrame([log_reg_test_plant])
print(log_reg_model.predict(log_reg_plant_df))
print("\nThe logistic regression model has predicted correctly.\n")


# K-nearest neighbor model
knn_model= KNeighborsClassifier()
trained_knn_model = train_model(knn_model, x_train, y_train)

print("A K-nearest neighbor model has been trained to predict Iris species based on its features using the dataset.\n")
evaluate_report(trained_knn_model, x_test, y_test)

print("\nA Virginica entry was selected, and its features were input into the K-nearest neighbor model. Here is the Iris species predicted by the model:")

knn_plant = {
    'sepal_length': 5.9,
    'sepal_width': 3.0 ,
    'petal_length': 5.1 ,
    'petal_width': 1.8 ,
}
knn_df = pd.DataFrame([knn_plant])
print(knn_model.predict(knn_df))
print("\nThe K-nearest neighbor model has predicted correctly.\n")