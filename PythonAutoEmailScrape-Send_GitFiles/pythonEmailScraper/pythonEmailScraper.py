# import urlparse
import bs4 as bs
import urllib2
import requests
import re
import time
from random import *
import wave 
import pyaudio
from threading import Thread

chunk = 1024  

#open a wav format music  
wav = wave.open(r"C:/Windows/media/Alarm01.wav","rb")  
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(wav.getsampwidth()),  
                channels = wav.getnchannels(),  
                rate = wav.getframerate(),  
                output = True)  
#read data  

userInput = None

def playsoundLoop():
	data = wav.readframes(chunk)
	while userInput is None:
		while data:
			stream.write(data)
			data = wav.readframes(chunk)
			if userInput != None:
				wav.rewind()
				data = wav.readframes(chunk)
				break
		wav.rewind()
		data = wav.readframes(chunk)

f = open("wordlist.txt", "r+")
emails = open("emails.txt", "r+")
temp = open("temp.txt", "r+")
userAgentFile = open("userAgents/userAgents.txt", "r")
x = 0


occupations = f.read().split('\n')
userAgent = userAgentFile.read().split('\n')

while True:
	occupation = occupations[randint(1, len(occupations))]
	print "Search #" + str(x) + " : " + occupation

	url = 'https://www.google.com/search?q=' + occupation.strip() + '+gmail.com+OR+yahoo.com+OR+ymail.com+OR+msn.com+OR+hotmail.com+OR+mac.com+OR+ovimail.com+OR+verizon.com+OR+aol.com+OR+mail.com&num=100'
	
	headers = userAgent[randint(0, len(userAgent))]
	response = requests.get(url, headers)
	# print headers
	source = response.content
	soup = bs.BeautifulSoup(source, 'lxml')

	line = str(soup)
	line = re.sub("<.*?>", " ", line)
	line = line.replace('@ ', '@')
	temp.write(line)
	match = re.findall(r'[\w\.-]+@[\w\.-]+', line)

	try:
		email = match[0]
		email = str(email) + "\n"
		emails.write(email)
	except:
		print "\n\nERROR ---- STOPPED ON! (" + occupation + ") WORD #" + str(x) + "\n"
		print "CHANGE YOUR IP WITH VPN OR PROXY THEN PRESS ENTER TO CONTINUE!!!\nPress Enter to Acknowledge..."
		# emails.write("STOPPED ON!!!!!!!!!! " + occupation + " WORD" + str(x) + "\n")
		
		t = Thread(target=playsoundLoop)
		t.start()
		userInput = raw_input(' ')
		userInput = raw_input('Press ENTER to continue scraping... \n\n')
		userInput = None

	i = 1
	while i < len(match):
		email = match[i]
		email = str(email) + "\n"
		prevEmail = str(match[i-1])
		if email.strip("\n") == prevEmail.strip("\n"):
			i = i + 1
			continue
		emails.write(email)
		i += 1

	# print "sleeping..."	
	# time.sleep(5)
	x += 1

	# source = urllib2.urlopen(url).read()
	# soup = bs.BeautifulSoup(source, 'lxml')


	# xml.write(soup)
