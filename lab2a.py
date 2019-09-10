# asdf
import csv
with open("cars.csv","r") as cars:
    reader = csv.reader(cars)
    for row in reader:  
        print (row)