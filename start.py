from utils import interactive_print
import os
from utils import (
    tell_joke,
    clear_screen,
    get_privious_date,
    get_next_date,
    get_date,
    who_is,
    word_meaning,
    send_mail
)


def match_command_with_function(command):
    if 'erase' in command or 'clear' in command:
        clear_screen()
    
    
    if 'stop' in command or 'exit' in command or 'quit' in command:
        exit()
    
    
    if 'hi' in command or 'Hello' in command or 'hello' in command or 'Hi' in command:
        interactive_print('Alexa: Hi, I can do various things for you, just type \'what you can do\' to know more.')
    
    if 'date' in command and 'yesterday' in command:
        get_privious_date()
    
    elif 'date' in command and 'tommorow' in command:
        get_next_date()
    
    elif 'date' in command:
        get_date()
    
    if 'what you can do' in command:
        interactive_print('I can do following task')
        print('1. Tell a joke\n2. Dates\n3. Word meaning')
    
    
    if 'joke' in command:
        tell_joke()
    
    if 'who is' in command:
        who_is()
    
    if 'mean' in command or 'meaning' in command:
        word_meaning(command.split(" ")[-1])
    
    if 'send' in command and 'mail' in command:
        send_mail()
    pass


def start_converstaion(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    interactive_print('Alexa: Welcome '+str(username))
    while True:
        command = input('You: ')
        match_command_with_function(command)
    pass