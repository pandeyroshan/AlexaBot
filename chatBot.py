import sqlite3
import random

def get_database_cursor():
    con=sqlite3.Connection('ChatbotDB')
    cur=con.cursor()
    return cur



def start_bot():
    statement = 'Hey ! Are you a registered user or a new user'


    def new_user_setup():
        statement = 'Hello User, What should I call you from next time?'
        print('Alexa: ',statement)
        command = input('You: ')
        if len(command.split(" "))<=2:
            statement = 'I will simply call you, '+str(command.split(" ")[0])+'. Is this ok for you ?'
            print(statement)
            bool_command = input('You: ')
            if bool_command.find('yes') or bool_command.find('ok') or  bool_command.find('good'):
                print('Alexa: OK, '+str(command.split(" ")[0]))
                passcode = str(random.randint(1000,9999))
                print('Alexa: Here is your auto generated PIN',passcode,' would you like to keep this?')
                passcode_bool_command = input('You: ')
                if passcode_bool_command.find('yes') or passcode_bool_command.find('ok') or  passcode_bool_command.find('good'):
                    pass
                else:
                    print('Alexa: What PIN I should keep for you ?')
                    command = input('You: ')
                    con = sqlite3.Connection('ChatbotDB')
                    cur = con.cursor()
                    cur.execute('create table if not exists user_credentials(username varchar(30),password varchar(30))')
                    con.commit()
            else:
                statement = 'What I should call you then ?'
                command = input('You: ')
                print('Alexa: OK',command)


    def login():
        pass


    def register_login():
        statement = 'Hey ! Are you a registered user or a new user'
        while True:
            print('Alexa: ',statement)
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
    start_bot()