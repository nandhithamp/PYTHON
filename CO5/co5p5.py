import csv
cars=[{'No.':1,'company':'Ferrari','Model':'488GTB'},{'No.':2,'company':'BMW','Model':'BMWX7'},{'No.':3,'company':'porsche','Model':'PM123'}]
csvfile=open('Name.csv','w')
field_name=list(cars[0].keys())
writer=csv.DictWriter(csvfile,fieldnames=field_name)
writer.writeheader()
writer.writerows(cars)
csvfile.close()

csv_file=open('Name.csv','r')
csv_reader=csv.reader(csv_file)

for line in csv_file:
    print(line,end="")