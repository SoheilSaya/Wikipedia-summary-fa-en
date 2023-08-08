import requests
import easygui
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
from urllib.parse import unquote
from tkinter import *
import tkinter.messagebox
import time 
from langdetect import detect

urlname=input("Whom do u want to know about? ")
starttime=time.time()

#determines whether we call persian or english wikipedia
if detect(urlname)=='fa' or detect(urlname)=='ar':
    language='fa'
else:
    language='en'
    
    
#embedding input in wikipedia search
"""I wrote all this code instead of a simple python.wikipedia.summary
for 3 reasons:
1. wikipedia module needs exact inputs and cant guess based on any name
try "rafsenjani" or "ahmadi nejad"
2. wikipedia module may get confused about some names idk why
try "ali daei", even tho its an exact id of a page, we get an error
3. i feel its a bit slow
"""


res=requests.get(f"https://{language}.wikipedia.org/w/index.php?search="+quote(urlname)+"&title=Special:Search&profile=advanced&fulltext=1&ns0=1")
soup=BeautifulSoup(res.text, 'html.parser')

#to select the first search resault
first_resault=str(soup.select('.mw-search-result-heading')[0])


print(first_resault)
print(first_resault.find("/wiki/"))
url_id=(first_resault[65:first_resault.find("\" title")])

print(f"u meant: {unquote(url_id)}\n")

# Given URL
url = f"https://{language}.wikipedia.org"+(url_id)
print(url)
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser').select('body')[0]

#to extract paragraphs
paragraphs = []

# Iterate through all tags to find paragraphs
for tag in soup.find_all():
    if tag.name=="p":
        paragraphs.append(tag.text)
      
#outputting resualts  
with open("Output.txt", "w", encoding="utf-8") as text_file:
    #number of paragraphs included in output
    counter=0
    for i in range(len(paragraphs)):
        #some wikipedia essays start with 
        #we dont want them as a whole paragraph
        if len(temp:=paragraphs[i])>30:
            print(temp)
            endtime=time.time()
            
            easygui.msgbox(temp, title=urlname)
            #tkinter.messagebox.showinfo(title=urlname,message=temp).lift()
            text_file.write(temp)
            counter+=1
        #how many paragraphs u want (usually 1)
        if counter==1:
            break
print(f"it took {endtime-starttime} seconds to run")