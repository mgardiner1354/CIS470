import pandas as pd
import numpy as np

cars = pd.read_csv('cars.csv')
car_countries = pd.read_csv('car_countries.csv')

combined_cars = pd.merge(cars,car_countries, on='Make') #the merged tables
car_MPG = combined_cars['MPG'] #a variable for each car by mpg
car_origin = combined_cars.groupby('Origin')#a variable for each car by origin

avg_mpg = car_MPG/car_origin #divides the MPG for each car by the number of cars manufactured from that country
print(combined_cars)
print(avg_mpg)
