#Setting the index
#The last step that you'll take in this chapter is to set the stop_datetime column as the DataFrame's index. 
#By replacing the default index with a DatetimeIndex, you'll make it easier to analyze the dataset by date and time, 
#which will come in handy later in the course!

# Set 'stop_datetime' as the index
ri.set_index('stop_datetime', inplace=True)

# Examine the index
print(ri.index)

# Examine the columns
print(ri.columns)

