import pandas as pd #importing pandas library

cambridge = pd.read_csv("Cambridge_Salaries.csv")

summary = cambridge['Total Salary'].describe() #gives a summary of the salaries in the dataset
print(summary)

total_salary = cambridge['Total Salary'].sum()
print('The total salary of all Cambridge divisions is:',total_salary)
