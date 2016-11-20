# Code by Luke Wood Copyright 6/30/2016

import json
import getpass
import smtplib
import time
import urllib.request
import sys

CONFIG = None
try:
	with open("config.json") as f:
		CONFIG = json.load(f)
except:
	CONFIG = None

if(CONFIG == None):
	sys.exit("config.json does not exist.")

SENDER = CONFIG["sender"]
PASSWORD = CONFIG["password"]
APIKEY = CONFIG["msw"]

#loads all of the emails to send to from users.txt
def loadusers():
	users = []
	with open("rsc/users.txt") as f:
		for line in f:
			users.append(line)
	return users
#loads the location codes and name of the beach
def loadspots():
	spots = []
	with open("rsc/spots.txt") as f:
		for line in f:
			spots.append(line.split(" ",1))
	return spots
#downloads the json data
def getwavedata(url):
	data = urllib.request.urlopen(url)
	data = data.read().decode('utf-8')
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
		print(spot)
		swelldata = getwavedata("http://magicseaweed.com/api/%s/forecast/?spot_id=%s&fields=swell.*&units=us" % (APIKEY,spot[0]))
		for a in swelldata:
			print(a["swell"]["minBreakingHeight"])

		temp = spot[1]+" "+swelldata["minBreakingHeight"]+"-"+swelldata["maxBreakingHeight"]+" ft"
		swells.append(temp)
	sendmessage(user,pwd,users,"SD Surf","\n".join(swells))

#main function

def main():
	loop(SENDER,PASSWORD)
if __name__ == "__main__":
	main()
