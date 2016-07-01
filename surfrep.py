# Code by Luke Wood Copyright 6/30/2016

import json
import getpass
import smtplib
import schedule
import time
import urllib.request

# MUST FILL IN YOURSELF
APIKEY = ""
SENDER = "surfreportlukewood@gmail.com"

#loads all of the emails to send to from users.txt
def loadusers():
	users = []
	with open("users.txt") as f:
		for line in f:
			users.append(line)
	return users
#loads the location codes and name of the beach
def loadspots():
	spots = []
	with open("spots.txt") as f:
		for line in f:
			spots.append(line).split(" ",1)
	return spots
#downloads the json data
def getwavedata(url):
	data = urllib.urlopen(url)
	data = data.read()
	data = 	json.loads(data)
	return data
#sends a message using these parameters through the gmail server
def sendmessage(user, pwd, recipient, subject, body):
	FROM = user
	TO = recipient if type(recipient) is list else [recipient]
	SUBJECT = subject
	TEXT = body
	message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO),SUBJECT,TEXT)
	try:
		server = smptlib.SMTP("smtp.gmail.com",587)
		server.ehlo()
		server.starttls()
		server.login(user,pwd)
		server.close()
	except:
		print("System Networking Error, Exiting, Press Enter.")
		g = input()

#this is what will run daily at 8 am
def loop(user, pwd):
	spots = loadspots()
	users = loadusers()
	swells = []
	for spot in spots:
		swelldata = getwavedata("http://magicseaweed.com/api/%s/forecast/?spot_id=%s&fields=swell&units=us" % (APIKEY,spot[0]))["swell"]
		temp = spot[1]+" "+swelldata["minBreakingHeight"]+"-"+swelldata["maxBreakingHeight"]+" ft"
		swells.append(temp)
	sendmessage(user,pwd,users,"SD Surf","\n".join(swells))

#main function

def main():
	password = getpass.getpass()
	schedule.every().day.at("08:00").do(loop,SENDER,password)

if __name__ == "__main__":
	main()