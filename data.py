import pandas as pd
import plotly.figure_factory as ff
import csv

dataFrames = pd.read_csv("data.csv")

#Calculating mean
with open('data.csv', newline = '') as fileObject:
    reader = csv.reader(fileObject)
    fileData = list(reader)

fileData.pop(0)    

newData = []
for i in range(len(fileData)):
    nNum = fileData[i][2]
    newData.append(float(nNum))

n = len(newData)    
total = 0
for y in newData:
    total += y

mean = total/n

print("Mean of the ratings is: " + str(mean))

#Creating a distribution plot
figure = ff.create_distplot([dataFrames["Avg Rating"].tolist()], ["Avg Rating"], show_hist = True)
figure.show()