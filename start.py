from utils import interactive_print
import os
from utils import (
    tell_joke,
    clear_screen
)


def match_command_with_function(command):
    if 'erase' in command or 'clear' in command:
        clear_screen()
    
    
    if 'stop' in command or 'exit' in command or 'quit' in command:
        exit()
    
    
    if 'hi' in command or 'Hello' in command or 'hello' in command or 'Hi' in command:
        interactive_print('Alexa: Hi, I can do various things for you, just type \'what you can do\' to know more.')
    
    
    if 'what you can do' in command:
        interactive_print('I can do following task')
        print('1. Tell a joke\n2. Dates\n3. Famous Personality Name')
    
    
    if 'joke' in command:
        tell_joke()
    pass


def start_converstaion(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    interactive_print('Alexa: Welcome '+str(username))
    while True:
        command = input('You: ')
        match_command_with_function(command)
    pass