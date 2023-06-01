# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 07:40:07 2022

@author: SONIA
"""

import json
import pandas as pd
import matplotlib.pyplot as plt

#how to read a json file (2ways)
json_file = open('loan_data_json.json')
#now to load the opened file
data= json.load(json_file)
#the second format is using a with statement ie; with open(loan_data_json.json') as json_file

#transform bogus list to data frame
loandata = pd.DataFrame(data)
 
#finding unique values for the purpose column
loandata['purpose'].unique()

#describing data
loandata.describe()
#describing data for a specific column
loandata['int.rate'].describe


import numpy as np

#how to use exp(exponent) function to get the actual anual income from the income log
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome']= income

#working with arrays as numpy works only with arrays
#1D array
arr= np.array([1,2,3,4])
#0D array
ar= np. array(43)
#2D arrays
arrr= np.array([[1,2,3], [4,5,6]])

#working with if statements
#example of an if statement
a = 40
b=500
c = 1000

if b > a and b < c:
    print('b is greater than a but less than c')
else:
    print('no conditions met')
    
#fico score

fico=250

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 600 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 780:
    ficocat = 'Good'
elif fico>= 780:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat) 

#for loops, how to use loops to apply a formul.a to an entire column or dataframe
fruits= ['apple', 'pear','banana']
for x in fruits:
    print(x)
    
y = x + ' fruits'
print(y)

#to apply loops to the loandata you neeed to definhe the value of x

    

length = len(loandata)
ficocat= []
for x in range(0,length):
    category= loandata['fico'] [x] 
    if category>= 300 and category < 400:
        cat = 'Very Poor'
    elif category>= 400 and category < 600:
        cat = 'Poor'
    elif category>= 601 and category < 660:
        cat= 'Fair'
    elif category>= 660 and category < 700:
        cat= 'Good'
    elif category>=700:
        cat='Excellent'
    else:
        cat= 'Unknown'
    ficocat.append(cat)
    
    

loandata['fico-category']= ficocat   

#df.loc as conditional statements 
#formula = dataframe.loc [df[columnname] condition, newcolumnname]= 'value if the condition is met'
# we need to do this to sort out our interest rate in a new column as >0.12 is high if not it is low

loandata.loc[loandata['int.rate']> 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate']<= 0.12, 'int.rate.type'] = 'Low'
  
#how to find out number of loans in the loandata
catplot = loandata.groupby(['fico-category']).size()

catplot.plot.bar(color='pink')
plt.show()

purposeplot = loandata.groupby(['purpose']).size()
purposeplot.plot.bar(color='pink', width = 0.2)
plt.show()

#scatter plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint,ypoint)
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index=True)

