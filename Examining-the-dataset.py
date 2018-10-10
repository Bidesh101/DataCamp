#Examining the dataset
#Throughout this course, you'll be analyzing a dataset of traffic stops in Rhode Island that was 
#collected by the Stanford Open Policing Project.

#Before beginning your analysis, it's important that you familiarize yourself with the dataset. 
#In this exercise, you'll read the dataset into 
#pandas, examine the first few rows, and then count the number of missing values.


# Import the pandas library as pd
import pandas as pd

# Read 'police.csv' into a DataFrame named ri
ri = pd.read_csv('police.csv')

# Examine the head of the DataFrame
print(ri.head())

# Count the number of missing values in each column
print(ri.isnull().sum())

