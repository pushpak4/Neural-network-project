import csv

time=[]
speed=[]

with open("Speed.csv",'r') as csvfile:
     Reader = csv.reader(csvfile,delimiter=",")
     
     for line in csvfile:
         time=line[11:19]
         speed=line[25:28]
         print(time, '\t', speed)