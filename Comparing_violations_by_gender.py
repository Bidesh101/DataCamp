#Comparing violations by gender
#The question we're trying to answer is whether male and female drivers tend to commit different types of traffic violations.

#In this exercise, you'll first create a DataFrame for each gender, and then analyze the violations in each DataFrame separately.



# Create a DataFrame of male drivers
male = ri[ri.driver_gender=='M']

# Compute the violations by female drivers (as proportions)
print(female.violation.value_counts(normalize=True))

# Compute the violations by male drivers (as proportions)
print(male.violation.value_counts(normalize=True))

