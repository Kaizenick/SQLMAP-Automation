import json
import requests
import bs4
import os
import re

#import simplejson as json
#from urllib.parse import urlparse, urlunsplit, urldefrag, parse_qs
import logging


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

har_json = har_import('post1.har')
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

#print(list1)
#print(list2)
print(req_data)
print(dict1)


new_post = open("/home/kali/Downloads/new_post.txt","a+")

new_post.write(method + " ")
new_post.write(url + " ")
new_post.write(HttpVer + " " + "\n")

for i in range(len(list1)):
	#print(list1[i],list2[i])
	new_post.write(list1[i] + ":" + list2[i] + "\n")

new_post.write(req_data + " " + "\n")

