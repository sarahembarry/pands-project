# pands-project

## Table of Contents:
1. [Project Description](#project-description)
2. [Summary of the Iris Data Set](#Summary-of-the-Iris-Data-Set)
3. [How to get started](#how-to-get-started)
4. [Credits and References](#credits-and-references)


## Project Description
This repository contains my analysis of the Fisher's Iris dataset.<br/>

Running 'analysis.py' or 'analysisnotebook.ipynb' will perform the following tasks:<br/>

- Output a summary of each variable to a single text file.
- Generate histograms of each variable and save them as PNG files.
- Generate a bar chart of the `species` variable.
- Create box plots for each numeric variable by species of Iris.
- Generate a correlation matrix of all numeric variables.
- Create a scatter plot of each pair of variables by Iris species as a pairplot.
- Produce an interactive scatter plot of `petal_length` and `petal_width`.
- Train and test a linear regression model to predict Iris species.
- Train and test a k-nearest neighbors model to predict Iris species.

Please see below for a summary of the dataset and all credits and references.<br/>

## Fisher's Iris Dataset

The Fisher's Iris dataset was made famous by Ronald Fisher, a statistician and biologist, who used it in a paper published in 1936 titled 'The Use of Multiple Measurements in Taxonomic Problems'. Sometimes referred to as the 'Anderson's Iris dataset' because the data was collected by an American botanist by the name 'Edgar Anderson'. [Source: Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-5)<br/>

Comprised 150 iris flowers, the dataset consists of 50 samples from each of three species of Iris:

- Iris Setosa
- Iris Virginica
- Iris Versicolor

The Iris dataset is comprised of five variables:

- `sepal_length`
- `sepal_width`
- `petal_length`
- `petal_width`
- `species`
<br/>
[Source: Emine Bozkus](https://eminebozkus.medium.com/exploring-the-iris-flower-dataset-4e000bcc266c)

## How to Get Started

To begin using this repository, follow these steps:<br/>

1. Install Python.
2. Install Visual Studio Code or another code editor.
3. Clone this repository and open it in your code editor.
4. Run the Jupyter Notebook.

Alternatively, you can use Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sarahembarry/pands-project)

## Credits and References

**Description**: Fisher's Iris Data Set
- **Source**: [Fisher,R. A.. (1988). UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/53/iris)
- **Date Accessed**: 2024
- **Link**: [Fisher's Iris Data Set](https://archive.ics.uci.edu/dataset/690/palmer+penguins-3)
---
**Description**: Iris Data Set Information
- **Source**: [en.wikipedia.org](https://en.wikipedia.org/)
- **Date Accessed**: 2024
- **Link**: [Fisher's Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-5)
---
**Description**: Iris Data Set Analysis
- **Source**: [Emine Bozkus](https://eminebozkus.medium.com/)
- **Date Published**: 2022
- **Link**: [Exploring the Iris flower dataset](https://eminebozkus.medium.com/exploring-the-iris-flower-dataset-4e000bcc266c)
---
**Description**: Iris Data Set Analysis
- **Source**: [Daniel Lundy](https://medium.com/@daniel.lundy.analyst)
- **Date Published**: 2023
- **Link**: [Mastering Machine Learning: Exploring the IRIS Dataset for Predictive Analysis](https://medium.com/@daniel.lundy.analyst/mastering-machine-learning-exploring-the-iris-dataset-for-predictive-analysis-f52a76bd7075#:~:text=The%20iris%20dataset%20is%20popular,and%20evaluating%20machine%20learning%20algorithms.)
---
**Description**: Exceptions in Python
- **Source**: [geeksforgeeks.org](https://www.geeksforgeeks.org/)
- **Date Published**: 2023 hand
- **Link**: [Python Try Except](https://www.geeksforgeeks.org/python-try-except/)
---
**Description**: Pandas DataFrame describe() Method
- **Source**: [www.w3schools.com/](https://www.w3schools.com/)
- **Date Accessed**: 2024
- **Link**: [Pandas DataFrame describe() Method](https://www.w3schools.com/python/pandas/ref_df_describe.asp)
---
**Description**: Pandas DataFrame describe() Function
- **Source**: [www.w3resource.com](https://www.w3schools.com/)
- **Date Accessed**: 2024
- **Link**: [Pandas DataFrame: describe() function](https://www.w3resource.com/pandas/dataframe/dataframe-describe.php)
---
**Description**: Find missing columns in df in with Pandas
- **Source**: [cmdlinetips.com](https://cmdlinetips.com/)
- **Date Published**: 2020
- **Link**: [How To Get Number of Missing Values in Each Column in Pandas](https://cmdlinetips.com/2020/11/how-to-get-number-of-missing-values-in-each-column-in-pandas/)
---
**Description**: Write pandas dataframe to text file
- **Source**: [stackoverflow.com](https://stackoverflow.com/)
- **Date Accessed**: 2024
- **Link**: [Write multiple pandas dataframe to the same txt file](https://stackoverflow.com/questions/57800651/write-multiple-pandas-dataframe-to-the-same-txt-file)
---
**Description**: Save histogram as file
- **Source**: [stackoverflow.com](https://stackoverflow.com/)
- **Date Accessed**: 2024
- **Link**: [How can I save histogram plot in python?](https://stackoverflow.com/questions/46411533/how-can-i-save-histogram-plot-in-python)
---
**Description**: Create Histogram from csv file column
- **Source**: [mode.com](https://mode.com/example-gallery/python_histogram)
- **Date Accessed**: 2024
- **Link**: [Creating Histograms using Pandas](https://mode.com/example-gallery/python_histogram)
---
**Description**: Histograms
- **Source**: [www150.statcan.gc](https://www150.statcan.gc.ca/)
- **Date Accessed**: 2024
- **Link**: [Histograms](https://www150.statcan.gc.ca/n1/edu/power-pouvoir/ch9/histo/5214822-eng.htm)
—--
**Description**:Histogram shapes
- **Source**: [asq.org](https://asq.org/quality-resources/histogram)
- **Date Accessed**: 2024
- **Link**: [WHAT IS A HISTOGRAM?](https://asq.org/quality-resources/histogram)
—--
**Description**:Functions in Python
- **Source**: [realpython.com](https://realpython.com/)
- **Date Published**: 2020
- **Link**: [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
---
**Description**: Matplotlib Bar Charts
- **Source**: [pythonbasics.org ](https://pythonbasics.org/)
- **Date Accessed**: 2024
- **Link**: [Matplotlib Bar Chart](https://pythonbasics.org/matplotlib-bar-chart/)
---
**Description**: Bar Charts
- **Source**: [atlassian.com/](https://www.atlassian.com/)
- **Date Accessed**: 2024
- **Link**: [A complete guide to bar charts](https://www.atlassian.com/data/charts/bar-chart-complete-guide#:~:text=A%20bar%20chart%20is%20used,groups%20compare%20against%20the%20others.)
---
**Description**: Boxplots by species
- **Source**: [Hfahmida Data Science and Business Analytics:TRIDS](https://medium.com/@hfahmida)
- **Date Published**: 2023
- **Link**: [EDA for Iris dataset with Boxplots Violin Plots Heatmap & Pairwise Plots](https://medium.com/@hfahmida/eda-for-iris-dataset-with-boxplots-violin-plots-heatmap-pairwise-plots-535275b4c2a0)
---
**Description**: Boxplots by species
- **Source**: [Ben Hamner](https://www.kaggle.com/benhamner)
- **Date Accessed**: 2024
- **Link**: [Python Data Visualizations](https://www.kaggle.com/code/benhamner/python-data-visualizations)
—--
**Description**:Box Plots
- **Source**: [A complete guide to box plots](https://www.atlassian.com/)
- **Date Accessed**: 2024
- **Link**: [A complete guide to box plots](https://www.atlassian.com/data/charts/box-plot-complete-guide#:~:text=Box%20plots%20are%20used%20to,skew%2C%20variance%2C%20and%20outliers.)
---
**Description**:Correlation Matrix in Pandas
- **Source**: [www.geeksforgeeks.org](https://www.geeksforgeeks.org/how-to-create-a-correlation-matrix-using-pandas/)
- **Date Published**: 2021
- **Link**: [How to create a correlation matrix using Pandas](https://www.geeksforgeeks.org/how-to-create-a-correlation-matrix-using-pandas/)
---
**Description**:Select columns by dtype in dataframe
- **Source**: [note.nkmk.me](https://note.nkmk.me/en)
- **Date Published**: 2024
- **Link**: [pandas: Select columns by dtype with select_dtypes()](https://note.nkmk.me/en/python-pandas-select-dtypes/)
---
**Description**:Filterning python warnings by message
- **Source**: [python-forum](https://python-forum.io/)
- **Date Accessed**: 2024
- **Link**: [Filtering warnings by message](https://python-forum.io/thread-35299.html)
---
**Description**: Scatter Plots
- **Source**: [w3schools.com](https://www.w3schools.com/python/matplotlib_scatter.asp)
- **Date Accessed**: 2024
- **Link**: [Creating Scatter Plots](https://www.w3schools.com/python/matplotlib_scatter.asp)
---
**Description**: seaborn.pairplot() method
- **Source**: [geeksforgeeks.org](https://www.geeksforgeeks.org/)
- **Date Accessed**: 2024
- **Link**: [Python – seaborn.pairplot() method](https://www.geeksforgeeks.org/python-seaborn-pairplot-method/)
—--
**Description**:Scatter plots
- **Source**: [patlassian.com](https://www.atlassian.com/)
- **Date Accessed**: 2024
- **Link**: [A complete guide to scatter plots](https://www.atlassian.com/data/charts/what-is-a-scatter-plot#:~:text=Scatter%20plots'%20primary%20uses%20are,are%20common%20with%20scatter%20plots)
---
**Description**: Scatter plot using Plotly
- **Source**: [geeksforgeeks.org](https://www.geeksforgeeks.org/)
- **Date Published**: 2024
- **Link**: [Scatter plot using Plotly in Python](https://www.geeksforgeeks.org/scatter-plot-using-plotly-in-python/)
---
**Description**:Supervised ML
- **Source**: [ibm.com](https://www.ibm.com/)
- **Date Accessed**: 2024
- **Link**: [What is supervised learning?](https://www.ibm.com/topics/supervised-learning)
---
**Description**:Overfitting in ML
- **Source**: [AWS](https://aws.amazon.com/)
- **Date Accessed**: 2024
- **Link**: [What is Overfitting?](https://aws.amazon.com/what-is/overfitting/#:~:text=Overfitting%20occurs%20when%20the%20model,all%20possible%20input%20data%20values.)
---
**Description**: Predict Iris Species in Python
- **Source**: [Johar Khan](https://www.youtube.com/@joharkhan99)
- **Date Published**: 2023
- **Link**: [Predict Iris Species in Python with ML: A Step-by-Step Guide](https://www.youtube.com/watch?v=2HfJVdj3SpM)
---
**Description**: Logistic Regression on the Iris dataset
- **Source**: [Rahul Raj Pandey](https://www.kaggle.com/rahulrajpandey31)
- **Date Accessed**: 2024
- **Link**: [Logistic Regression From Scratch Iris Data-set](https://www.kaggle.com/code/rahulrajpandey31/logistic-regression-from-scratch-iris-data-set)
---
**Description**: Logistic Regression in Python
- **Source**: [Avinash Navlani via Datacamp](https://www.datacamp.com/)
- **Date Published**: 2019
- **Link**: [Understanding Logistic Regression in Python Tutorial](https://www.datacamp.com/tutorial/understanding-logistic-regression-python)
---
**Description**:Logistic Regression in Machine Learning
- **Source**: [geeksforgeeks.org](https://www.geeksforgeeks.org/understanding-logistic-regression/)
- **Date Published**: 2024
- **Link**: [Logistic Regression in Machine Learning](https://www.geeksforgeeks.org/understanding-logistic-regression/)
---
**Description**:K-nearest neighbors on Iris data set
- **Source**: [AI with AI](https://www.youtube.com/@AsifImmanad)
- **Date Accessed**: 2024
- **Link**: [Example of ML Classification Technique on iris Dataset using KNN Algorithm | AI with AI](https://www.youtube.com/watch?v=KvYGJt3cTj4)
---
**Description**:K-nearest neighbors on Iris data set
- **Source**: [S.Sreenivasulu](https://www.kaggle.com/susree64)
- **Date Accessed**: 2024
- **Link**: [K-Nearest Neighbor with Iris Data set](https://www.kaggle.com/code/susree64/k-nearest-neighbor-with-iris-data-set)
---
**Description**:What Is K-Nearest Neighbors?
- **Source**: [zilliz.com](https://zilliz.com/blog/k-nearest-neighbor-algorithm-for-machine-learning)
- **Date Published**: 2022
- **Link**: [What Is K-Nearest Neighbors (KNN) Algorithm in Machine Learning? An Essential Guide](https://zilliz.com/blog/k-nearest-neighbor-algorithm-for-machine-learning)
---
**Description**:K-Nearest Neighbors
- **Source**: [javatpoint.com](https://www.javatpoint.com/k-nearest-neighbor-algorithm-for-machine-learning)
- **Date Published**: 2024
- **Link**: [K-Nearest Neighbor(KNN) Algorithm for Machine Learning](https://www.javatpoint.com/k-nearest-neighbor-algorithm-for-machine-learning)
---







