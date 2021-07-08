import requests
import bs4
import os
import re

test= open("/home/kali/Downloads/scan_out.txt","a+") 
report = open("/home/kali/Downloads/report.txt","a+")


#file1.write("Sohamji is created")
read1 = test.read()
#print(read1)

#soup = bs4.BeautifulSoup(read1, 'html5lib')

report.write("HPE CTY REPORT")
report.write("\n")
report.write("Payload info:")
report.write("\n")
report.write("\n")
q = re.search(r"Parameter:",read1)
first = q.span()[0]
p = re.search(r"---.",read1)
last = p.span()[1]
#p=re.search("[.........]",read1)
print(q.span())
print(p.span())
#print(p.group())

read2 = ((read1[first:last]))
#print(read2)
#report.write((read2))

info = re.search(r"back-end.DBMS",read2)
print("info",info.span())
read3 = read2[0:info.span()[0]-22]
report.write((read3))


ending = re.search(r"ending.@",read1)
print("ending",ending.span())


while last<ending.span()[0]:
	table = re.search("Table:",read1[last:ending.span()[0]])
	first = table.span()[0]
	csv = re.search(".csv'",read1[last:ending.span()[0]])
	last = csv.span()[1]
	report.write((read1[first:last]))
	print("table start",table.span())
	print("csv end",csv.span())



'''
mylines = []
with open ('/home/kali/Downloads/test.txt', 'rt') as myfile:
	for myline in myfile:
		mylines.append(myline)
print(mylines)'''

test.close()
report.close()