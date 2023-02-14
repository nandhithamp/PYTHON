import csv
csv_f=open('studentdetails.csv','r')
csv_r=csv.reader(csv_f)
for line in csv_r:
# print(csv_r)
    print(line[2])