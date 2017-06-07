#!/bin/env python2.7

import urllib2
from bs4 import BeautifulSoup
import lxml.html
import re
from  more_itertools import unique_everseen
from mailer import Mailer
from mailer import Message

def get_the_links(url, domain, word):
    f =  urllib2.urlopen(url)
    soup = BeautifulSoup(f,"lxml")
    for link in soup.find_all('a', href=True):
        if re.findall(word, link['href']):
         links.append(domain + link['href'])

def review_the_links():
     lines = [line.rstrip('\r\n') for line in open('test.txt')]
     for line in lines:
          oldlinks.append(line)
          
def check_the_links(old_list, new_list):
     s = list(set(new_list) - set(old_list))
     if s:
           addedlinks.extend(s)
     else:
          print 'Compared the list two lists. Found no new offers'
            
def write_the_links(mylist):
        for item in mylist:
            Html_file = open("test.txt", "ab")
            Html_file.write("%s\n" % item)
            Html_file.close()     
   
def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"



links = []
oldlinks = []
addedlinks = []
addeset = []

#for immobilienscout24
some_url = 'http://www.immobilienscout24.de/Suche/S-2/Wohnung-Miete/Hamburg/Hamburg/-/-/50,00-/EURO--800,00' #example url. just add your own filters
review_the_links()
get_the_links(url=some_url, domain='http://www.immobilienscout24.de', word='/expose/')
sorted = []
sorted = list(unique_everseen(links))  
check_the_links(old_list=oldlinks, new_list=sorted)   

#for immonet
review_the_links()
second_url = 'http://www.immonet.de/immobiliensuche/sel.do?pageoffset=1&listsize=25&objecttype=1&locationname=Hamburg&acid=&actype=&city=109447&ajaxIsRadiusActive=true&sortby=19&suchart=2&radius=0&pCatMTypeStoragefield=&pcatmtypes=1_2&parentcat=1&marketingtype=2&fromprice=&toprice=800&fromarea=50&toarea=&fromplotarea=&toplotarea=&fromrooms=2&torooms=&absenden=Ergebnisse+anzeigen&objectcat=-1&feature=57&wbs=-1&fromyear=&toyear=&fulltext='
get_the_links(url=second_url, domain='http://www.immonet.de', word='/angebot/')
immosorted = []
immosorted = list(unique_everseen(links))
check_the_links(old_list=oldlinks, new_list=immosorted)

#for ebay
review_the_links()
third_url = 'https://www.ebay-kleinanzeigen.de/s-wohnung-mieten/hamburg/preis::800/c203l9409+wohnung_mieten.qm_i:40,80+wohnung_mieten.zimmer_i:2,3' #example url. just add your own filters
get_the_links(url=third_url,domain='https://www.ebay-kleinanzeigen.de', word='/s-anzeige/')
ebysorted = []
ebysorted = list(unique_everseen(links))
check_the_links(old_list=oldlinks, new_list=ebysorted)

if addedlinks:
    print 'Adding new Links: %s' % addedlinks
    write_the_links(mylist=addedlinks)
    send_email(user='ADDEMAILHERE', pwd='EMAILPASSWORD', recipient='FORWARD_TO_ANOTHER_EMAIL',
    subject='neue wohnungen', body=addedlinks)
else:
    print 'Found no new offers to send'
                          