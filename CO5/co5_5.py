import csv
cars=[{'no.':1,'company':'ferrari','model':'488GTB'},{'no.':2,'company':'BMW','model':'BMWX7'},{'no.':3,'company':'porsche','model':'KK'}]
csvfile=open('name.csv','w')
field_name=list(cars[0].keys())
writer=csv.DictWriter(csvfile,fieldnames=field_name)
writer.writeheader()
writer.writerows(cars)
csvfile.close()
csv_file=open('name.csv','r')
csv_reader=csv.reader(csv_file)
#print(csv_reader)
for line in csv_file:
    print(line,end="")