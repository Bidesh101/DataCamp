#Calculating the search rate
#During a traffic stop, the police officer sometimes conducts a search of the vehicle. 
#In this exercise, you'll calculate the percentage of all stops that result in a vehicle search, also known as the search rate.

# Check the data type of 'search_conducted'
print(ri.search_conducted.dtypes)

# Calculate the search rate by counting the values
print(ri.search_conducted.value_counts(normalize=True))

# Calculate the search rate by taking the mean
print(ri.search_conducted.mean())

#Comparing search rates by gender
#In this exercise, you'll compare the rates at which female and male drivers are searched during a traffic stop. 
#Remember that the vehicle search rate across all stops is about 3.8%.

#First, you'll filter the DataFrame by gender and calculate the search rate for each group separately. 
#Then, you'll perform the same calculation for both genders at once using a .groupby().

# Calculate the search rate for female drivers
print(ri[ri.driver_gender=='F'].search_conducted.mean())

# Calculate the search rate for male drivers
print(ri[ri.driver_gender=='M'].search_conducted.mean())

# Calculate the search rate for male drivers
print(ri[ri.driver_gender=='M'].search_conducted.mean())

#Adding a second factor to the analysis
# Calculate the search rate for each combination of gender and violation
print(ri.groupby(['driver_gender', 'violation']).search_conducted.mean())

# Reverse the ordering to group by violation before gender
print(ri.groupby(['violation', 'driver_gender']).search_conducted.mean())


