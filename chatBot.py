import sqlite3
import random
import sys
from time import sleep
import os


def interactive_print(input_string):
    for char in input_string:
        sleep(0)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()

def setup_database():
    global con
    global cur
    con = sqlite3.Connection('ChatbotDB')
    cur = con.cursor()
    cur.execute('create table if not exists user_credential(id INTEGER PRIMARY KEY AUTOINCREMENT,username varchar(30),password varchar(30))')


def start_bot():


    def new_user_setup():
        statement = 'Alexa: Hello User, What should I call you from next time?'
        interactive_print(statement)
        command = input('You: ')
        if len(command.split(" "))<=2:
            statement = 'Alexa: I will simply call you, '+str(command.split(" ")[0])+'.'
            interactive_print(statement)
            passcode_command = str(random.randint(1000,9999))
            statement = 'Alexa: Here is your auto generated PIN '+str(passcode_command)+' would you like to keep this or set a new one?'
            interactive_print(statement)
            passcode_bool_command = input('You: ')
            if 'new' in passcode_bool_command.split(" "):
                interactive_print('Alexa: What should be your password then ?')
                passcode_command = input('You: ')
            interactive_print('Alexa: Here is your login credential, \nUsername: '+str(command.split(" ")[0].lower())+'\nPassword: '+str(passcode_command))
            interactive_print('Alexa: Now, I\'m redirecting you to login window and within 3 second this window will be gone')
            cur.execute('insert into user_credential(username, password) values(?,?)',(str(command.split(" ")[0].lower()),str(passcode_command)))
            con.commit()
            sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('cls' if os.name == 'nt' else 'clear')
            login()

    def login():
        interactive_print('Alexa: Welcome user, Kindly provide your credentials\nUsername:')
        username = input('You: ')
        interactive_print('Alexa: Passcode: ')
        passcode = input('You: ')
        # cur.execute('delete from user_credentials')
        con.commit()
        cur.execute('select * from user_credential')
        result_set = cur.fetchall()
        print(result_set)
        pass


    def register_login():
        statement = 'Alexa: Hey ! Are you a registered user or a new user'
        interactive_print(statement)
        command = input('You: ')
        if str(command).find('new') or str(command).find('first') or str(command).find('before'):
            new_user_setup()
        elif str(command).find('old') or str(command).find('registered'):
            login()
        else:
            statement = 'Sorry, I can\'t understand that'
    
    # Alexa start here
    register_login()


if __name__=="__main__":
    setup_database()
    start_bot()