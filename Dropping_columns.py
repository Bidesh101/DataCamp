#Dropping columns
#Often, a DataFrame will contain columns that are not useful to your analysis. 
#Such columns should be dropped from the DataFrame, to make it easier for you to focus on the remaining columns.

#In this exercise, you'll drop the county_name column because it only contains missing values, 
#and you'll drop the state column because all of the traffic stops took place in one state (Rhode Island). 
#Thus, these columns can be dropped because they contain no useful information.


# Count the number of missing values in each column
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)

# Drop the 'county_name' and 'state' columns
ri.drop(['county_name', 'state'], axis='columns', inplace=True)

# Examine the shape of the DataFrame (again)
print(ri.shape)

