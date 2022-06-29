from os import system
from sys import platform

if platform.startswith() == 'win32':
    system('cls')
else:
    system('clear')

while True:
    system('python bot.py')