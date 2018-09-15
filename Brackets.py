#We can use the following code to print specific Data from th CVS File


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc[['JAP']])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
