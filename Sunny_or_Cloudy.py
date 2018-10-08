#Sunny or cloudy
#On average, how much hotter is it when the sun is shining? In this exercise, 
#you will compare temperatures on sunny days against temperatures on overcast days.

#Your job is to use Boolean selection to filter out sunny and overcast days, 
#and then compute the difference of the mean daily maximum temperatures between each type of day.

#The DataFrame df_clean from previous exercises has been provided for you. 
#The column 'sky_condition' provides information about whether the day was sunny ('CLR') or overcast ('OVC').

# Select days that are sunny: sunny
sunny = df_clean.loc[df_clean['sky_condition']=='CLR']

# Select days that are overcast: overcast
overcast = df_clean.loc[df_clean['sky_condition'].str.contains('OVC')]


# Resample sunny and overcast, aggregating by maximum daily temperature
sunny_daily_max= sunny.resample('D').max()
overcast_daily_max= overcast.resample('D').max()

# Print the difference between the mean of sunny_daily_max and overcast_daily_max
print(sunny_daily_max.mean() - overcast_daily_max.mean())


