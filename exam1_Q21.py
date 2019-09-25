import pandas as pd
#Without using pandas, write a for loop that calculates the average salary of 2020 Public Safety per division of workers in the Cambridge Data Set#

import csv #adding csv library

total_salary = 0 #defining total salary across all employees 
emp_count = 0 #defining how many employees work at Cambridge

with open('Cambridge_Salaries.csv') as file:
    csv_reader_object = csv.reader(file)
    if csv.Sniffer().has_header:
        next(csv_reader_object) #checks for header and skips it in calculations
    for row in csv_reader_object: #iterating through csv to calculate total salary and number of employees
        float_salary = float(row[6])
        total_salary += float_salary
        emp_count += 1
        
#calculate average by dividing salary by employees
avg_salary = total_salary/emp_count
print("The average salary in the data set is")
print(avg_salary) 
