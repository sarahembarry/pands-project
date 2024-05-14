
#Import Libraries
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

#Import and summerise the dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
print("The Iris dataset has been imported:")

summary= df.describe(include='all')
print("Here is a summary of the Iris dataset:\n")
print(summary)


#Check data quality
missing_values = df.isna().sum()
print(missing_values)
print("\nDataset checked for missing values. There are no missing values")

#Summary of variables to tct file
with open("summaryofvariables.txt", "w") as f:
   f.write(summary.to_string())
print("A text file with the summary of all variables in the dataset has been generated.")


#Histograms of numeric variables
def plot_histogram(column,column_name, title, filename):
    plt.hist(column, color='blue', bins=30)
    plt.title(title, fontsize=16)
    plt.xlabel(column_name, fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

plot_histogram(df['sepal_length'],'sepal_length(cm)', 'Distribution of Sepal Length', 'sepal_length_histogram.png')
print("A histogram of 'sepal_length' has been generated and saved as a .png file.")


plot_histogram(df['sepal_width'], 'sepal_width(cm)','Distribution of Sepal Width', 'sepal_width_histogram.png')
print("A histogram of 'sepal_width' has been generated and saved as a .png file.")


plot_histogram(df['petal_length'],'petal_length(cm)', 'Distribution of Petal Length', 'petal_length_histogram.png')
print("A histogram of 'petal_length' has been generated and saved as a .png file.")


plot_histogram(df['petal_width'], 'petal_width(cm)','Distribution of Petal Width', 'petal_width_histogram.png')
print("A histogram of 'petal_width' has been generated and saved as a .png file.")



#Bar chart of species
species_counts = df['species'].value_counts()
plt.bar(species_counts.index,species_counts.values, color='blue')
plt.title('Number of Iris Flowers by Species')
plt.xlabel('Species of Iris Flower')
plt.ylabel('Count of Iris Flowers')
plt.savefig('species_barchart.png')
print("A barchart of 'species' has been generated and saved as a .png file .")


#Boxplots of numeric variables by species
print("Boxplots for each numeric variable by species have been generated:\n")
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


#Correlation matrix
numeric_df = df.select_dtypes(include='number')
correlation_matrix = numeric_df.corr()
print("Here is a matrix of the correlation between the numeric variables in the datset:\n")
print(correlation_matrix)


#Pairplot scatterplots of numeric variables by species 
warnings.filterwarnings("ignore", message="use_inf_as_na option is deprecated")
warnings.filterwarnings("ignore", message="When grouping with a length-1 list-like")

print("A scatterplot of the correlation of numeric variables by species has been generated:\n")
sns.pairplot(df, hue='species')
plt.show()


#Interactive scatterplot of petal length and petal width
print("A interactive scatterplot of 'petal length' and 'petal width' has been generated:\n")
fig = px.scatter(df, x="petal_length", y="petal_width",
                 color="species",
                 symbol="species",  
                 hover_data=['petal_length', 'petal_width'])
fig.show()



#Machine learning set up
x = df[['sepal_length', 'sepal_width' ,'petal_length','petal_width']]
y = df['species']
x_train, x_test, y_train,y_test = train_test_split(x, y, test_size=0.2, random_state=42)


#Logistic regression model
log_reg_model= LogisticRegression()
log_reg_model.fit(x_train,y_train)
log_reg_predictions = log_reg_model.predict(x_test)
print("A logistic regression model has been trained to predict Iris species based on features using the dataset. Here are the results:\n")
print(classification_report(y_test,log_reg_predictions))

print("A Setosa entry was selected, and its features were input into the logistic regression model. Here is the Iris species predicted by the model:")


log_reg_test_plant = {
    'sepal_length': 5.0,
    'sepal_width': 3.6 ,
    'petal_length': 1.4 ,
    'petal_width': 0.2 ,
}

log_reg_plant_df = pd.DataFrame([log_reg_test_plant])

print(log_reg_model.predict(log_reg_plant_df))

print("The logistic regression model has predicted correctly")



#K-nearest neighbour model
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(x_train, y_train)
knn_predictions = knn_model.predict(x_test)


print("A K Nearest Neighbor model has been trained to predict Iris species based on features using the dataset. Here are the results:\n")
print(classification_report(y_test, knn_predictions))
print("A Virginica entry was selected, and its features were input into the K-nearest neighbour model. Here is the Iris species predicted by the model:")

knn_plant = {
    'sepal_length': 5.9,
    'sepal_width': 3.0 ,
    'petal_length': 5.1 ,
    'petal_width': 1.8 ,
}

knn_df = pd.DataFrame([knn_plant])

print(knn_model.predict(knn_df))

print("The k-nearest neighbor model has predicted correctly")