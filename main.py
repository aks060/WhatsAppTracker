#!/usr/bin/python3
import os
import datetime
import time
import sqlite3

db=sqlite3.connect('database.db')

name=input('Enter name of the person: ')
mob=input('Enter mobile number of person (Default set): ')
#mob='8630513308'
inter=int(input('Enter time interval to check'))
ready=input('All Ready? (y/n)')
pth=input('burp file id: ')
fpath='/tmp/burp'+pth+'.tmp/0'

pos=0
lastst=''
data=''
while 1:
	log=open('log.txt', 'a+')
	with open(fpath, 'r', encoding = "ISO-8859-1") as f:
		data=f.read()
	data=data.split('"')
	data.reverse()
	numlast=data.index('91'+mob+'@c.us')
	if data[numlast-4]=='available' and lastst!='a':
	    mssg=name+' is online at '+str(datetime.datetime.now().time())
	    os.popen('notify-send "'+mssg+'"')
	    lastst='a'
	    log.write(mssg+'\n')
	elif data[numlast-4]=='unavailable' and lastst!='u':
	    mssg=name+' is Offline at '+str(datetime.datetime.now().time())
	    os.popen('notify-send "'+mssg+'"')
	    lastst='u'
	    log.write(mssg+'\n')
	f.close()
	log.close()
	time.sleep(inter)

