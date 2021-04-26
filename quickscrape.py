import requests
import re

#get url from user
custom_url = input("Enter URL:")

#get data from html
data = requests.get(custom_url)

#extract emails and phone numbers using regex

phone_numbers = re.findall(r'([\d]{3,4}[\-\.\s][\d]{3,4}[\-\.\s][\d]{3,4})', data.text)
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.[\w.]+)', data.text)

#print neatly

i = 0
for num in phone_numbers:

	print(num + " : " + emails[i])
	i += 1
