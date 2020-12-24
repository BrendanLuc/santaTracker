import time
import requests
from bs4 import BeautifulSoup
from lxml import html
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os
import config

phoneNumbers = []

def getSantaInfo():
    proxy = webdriver.Safari()
    proxy.get("https://www.noradsanta.org/overlay/tracking/map/index.html")
    time.sleep(5)
    html = proxy.page_source
    #print(html)
    soup = BeautifulSoup(html, 'html.parser')
    lastSpotted = soup.find('span', attrs={'class':"lastSpotted"})
    #print(lastSpotted.text)
    headedFor = soup.find('span', attrs={'class':"headedFor"})
    #print(headedFor.text)
    timeRemaing = soup.find('span', attrs={'class':"remainingTime"})
    #print(timeRemaing.text)
    giftsDelivered = soup.find('div', attrs={'class':"giftCounter"})
    #print(giftsDelivered.text)

    message = "Santa was last spotted in " + lastSpotted.text
    message = message + "! He will be in " + headedFor.text + " in " + timeRemaing.text + "!"
    message = message + " He has already delivered " + giftsDelivered.text + " gifts!!!"
    #print(message)
    proxy.close()
    return(message)

#if not imessage.check_compatibility(phone):
#    print("Not an Iphone")
def sendMessage(phoneNumber, message):
    os.system('osascript send.scpt {} "{}"'.format(phoneNumber, message))

if __name__ == '__main__':
    while True:
        message = getSantaInfo()
        for phoneNumber in phoneNumbers:
            sendMessage(phoneNumber, message)
        time.sleep(3600)

# guid = imessage.send(phone, message)
# print(imessage.status(guid))
exit(0)
