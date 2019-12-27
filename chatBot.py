import sqlite3
import random
import sys
from time import sleep


def interactive_print(input_string):
    for char in input_string:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()

def setup_database():
    con = sqlite3.Connection('ChatbotDB')
    cur = con.cursor()
    cur.execute('create table if not exists user_credentials(username varchar(30),password varchar(30))')


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
            interactive_print('Alexa: Here is your login credential, \nUsername: '+str(command)+'\nPassword: '+str(passcode_command))
            interactive_print('Alexa: Now, I\'m redirecting you to login window and within 3 second this window will be gone')

    def login():
        pass


    def register_login():
        statement = 'Alexa: Hey ! Are you a registered user or a new user'
        while True:
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