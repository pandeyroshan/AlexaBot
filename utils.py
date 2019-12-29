from time import sleep
import sys
import requests
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')

def interactive_print(input_string):
    for char in input_string:
        sleep(0)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()


def get_date():
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
    print(res.text)
    pass

def ask_riddle():
    pass