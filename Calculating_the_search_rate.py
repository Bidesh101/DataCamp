#Calculating the search rate
#During a traffic stop, the police officer sometimes conducts a search of the vehicle. 
#In this exercise, you'll calculate the percentage of all stops that result in a vehicle search, also known as the search rate.

# Check the data type of 'search_conducted'
print(ri.search_conducted.dtypes)

# Calculate the search rate by counting the values
print(ri.search_conducted.value_counts(normalize=True))

# Calculate the search rate by taking the mean
print(ri.search_conducted.mean())

