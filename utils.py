from time import sleep
import sys
import requests
import os
from datetime import date
from datetime import datetime, timedelta
import json
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')

def interactive_print(input_string):
    for char in input_string:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()


def get_date():
    today = date.today()
    interactive_print('Alexa: Today\'s Date - '+str(today))
    pass

def get_privious_date():
    interactive_print((datetime.now() - timedelta(1)).strftime('%Y-%m-%d'))
    pass

def get_next_date():
    interactive_print((datetime.now() + timedelta(1)).strftime('%Y-%m-%d'))
    pass


def get_time():
    pass


def get_task_list():
    pass

def get_list():
    pass

def delete_list():
    pass

def tell_joke():
    res = requests.get("https://geek-jokes.sameerkumar.website/api")
    interactive_print(res.text)
    pass

def ask_riddle():
    pass

def who_is():
    pass

def word_meaning(word):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    querystring = {"term":word}
    headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "03487d8506msh9846417c3bc421cp1cf83cjsndb11b228b3d8"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    final_dictionary = json.loads(response.text)
    meaning = str(final_dictionary['list'][0]['definition']).replace("[","").replace("]","")
    interactive_print('Alexa: Meaning of word '+str(word)+' is '+meaning)
    pass

def send_mail():
    interactive_print('Alexa: What is the receiver\'s email address ?')
    email_id_str = input('You: ')
    for data in email_id_str.split(" "):
        if '@' in data:
            email_id = data
    interactive_print('Alexa: What will be the subject of email ?')
    subject = input('You: ')
    interactive_print('Alexa: What will be the body of email ?')
    body = input('You: ')
    sender_id = os.environ['gmail_address']
    sender_password = os.environ['gmail_password']
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(sender_id, sender_password)
    message = 'Subject: {}\n\n{}'.format(subject, body)
    server.sendmail(sender_id, email_id, message)
    server.quit()
    pass