# SQLMAP-Automation

## Installation
Since sqlmap is written in python, the first thing you need is the python interpreter. Download the python interpreter from https://www.python.org/.

There are two series of python, 2.7.x and 3.3.x. Sqlmap should run fine with either.
So download and install it.

## Download and install Sqlmap

Next download the sqlmap zip file from sqlmap.org.
Extract the zip files in any directory.

Launch the dos prompt and navigate to the directory of sqlmap. Now run the sqlmap.py script with the python interpreter.
```
C:\sqlmapproject-sqlmap>python ./sqlmap.py
Usage: ./sqlmap.py [options]
sqlmap.py: error: missing a mandatory option (-d, -u, -l, -m, -r, -g, -c, --wiza
rd, --update, --purge-output or --dependencies), use -h for basic or -hh for adv
anced help
Press Enter to continue...
```
Now that you have finished installing sqlmap and are ready to run it.

# Automation

* The drafts are the chekpoints of the automation with addition of new features in each new Draft.
* The Final_Draft contains the latest changes which contains the GET and POST methods both
* JSON PARSER is a short code used to parse the data from the json file to the main file so that the needed parameters can be extracted.
  * Needed parameters or sample parameters for POST Method are:
    *  POST http://192.168.1.106/dvwa/vulnerabilities/exec/# HTTP/1.1
    *  Host: 192.168.1.106
    *  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
    *  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    *  Accept-Language: en-US,en;q=0.5
    *  Accept-Encoding: gzip, deflate
    *  Content-Type: application/x-www-form-urlencoded
    *  Content-Length: 18
    *  Origin: http://192.168.1.106
    *  Connection: keep-alive
    *  Referer: http://192.168.1.106/dvwa/vulnerabilities/exec/
    *  Cookie: security=low; PHPSESSID=ef8dde95c1f3a1ede3e5e62cc4c3985b
    *  Upgrade-Insecure-Requests: 1
* All These can be extracted using the JSON Parser

## Running the automation
To Run the Automation simply run the python script Final_Draft.py using
```
kali@kali:~/Downloads$ python Final_Draft.py
```
If this gives error try
```
kali@kali:~/Downloads$ python3 Final_Draft.py
```
