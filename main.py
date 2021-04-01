from tkinter import *
import tkinter
from discord_webhook import *
import requests
import time

embed = DiscordEmbed()

root = Tk()
root.geometry('500x500')
root.winfo_toplevel().title("get spammed lol")
mywebhookurl = Entry(root)
mywebhookurl.insert(0, "Webhook URL")
mywebhookurl.grid(row=1, column=0)

def checkurl():
    try:        
        r = requests.get(mywebhookurl.get(), auth=('user', 'pass'))
        print(r.status_code)
    except:
        print("not a webhook url")
        exit(1)

    if r.status_code == 200:
        print('ok')
        pol = Label(text="ok", )
        pol.grid(row=1, column=3)
        #print(mywebhookurl.get())
        global webhookurl123
        webhookurl123 = mywebhookurl.get()
        global webhook
        webhook = DiscordWebhook(url=webhookurl123)

    else:
        print("invalid webhook url")
        exit(1)

var = tkinter.IntVar()
check_button = Button(root, text="check url", padx=1, pady=1, command=lambda:[checkurl(), var.set(1)])
check_button.grid(row= 1, column=1)
check_button.wait_variable(var)

def sendembed():
    embed.set_title('get spammed lol')
    #embed.set_color("GREEN")
    webhook.add_embed(embed)
    webhook.execute()

def spamwebhook():
    while True:
        sendembed()
        time.sleep(1)

send_button = Button(root, text="spam webhook", command=spamwebhook)
send_button.grid(row=15, column=0)

root.mainloop()
