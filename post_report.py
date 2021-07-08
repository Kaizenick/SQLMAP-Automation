import json
import requests
import bs4
import os
import re
scan_out= open("/home/kali/Desktop/scan_out.txt","a+") 
report = open("/home/kali/Desktop/report.txt","a+")

read1 = scan_out.read() 

report.write("HPE CTY REPORT")
report.write("\n")
report.write("Payload info:")
report.write("\n")
report.write("\n")

	    
###################### Payloads part below ###############################
Parameter = re.search(r"Parameter:",read1)
first = Parameter.span()[0]
dash = re.search(r"---.",read1)
last = dash.span()[1]
#print(Parameter.span())
#print(dash.span())
read2 = ((read1[first:last]))
#print(read2)
#report.write((read2))
      
info = re.search(r"back-end.DBMS",read2)
#print("info",info.span())
read3 = read2[0:info.span()[0]-22]
report.write((read3))
            
###################### Tables part below #################################
ending = re.search(r"ending.@",read1)
#print("ending",ending.span())

dump = re.search("Database:",read1)
#print("dump",dump.span())
	
read4 = read1[dump.span()[1]:ending.span()[0]]
report.write((read4))
	   