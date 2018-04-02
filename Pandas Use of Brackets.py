# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# The "index_col = 0" in the above line will not print the first coulmn of
# the cvs file.

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])
