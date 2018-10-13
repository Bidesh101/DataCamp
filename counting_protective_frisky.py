#Counting protective frisks
#During a vehicle search, the police officer may pat down the driver to check if they have a weapon. 
#This is known as a "protective frisk."

#In this exercise, you'll first check to see how many times "Protective Frisk" was the only search type. 
#Then, you'll use a string method to locate all instances in which the driver was frisked.

# Count the 'search_type' values
print(ri.search_type.value_counts())

# Check if 'search_type' contains the string 'Protective Frisk'
ri['frisk'] = ri.search_type.str.contains('Protective Frisk', na=False)

# Check the data type of 'frisk'
print(ri.frisk.dtype)

# Take the sum of 'frisk'
print(ri.frisk.sum())

