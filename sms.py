import time
import pyautogui
from colorama import Fore
print(Fore.RED + ''' 


 ██▓ ███▄    █  ▄▄▄▄    ▒█████  ▒██   ██▒ ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
▓██▒ ██ ▀█   █ ▓█████▄ ▒██▒  ██▒▒▒ █ █ ▒░▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██  ▀█ ██▒▒██▒ ▄██▒██░  ██▒░░  █   ░▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
░██░▓██▒  ▐▌██▒▒██░█▀  ▒██   ██░ ░ █ █ ▒ ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
░██░▒██░   ▓██░░▓█  ▀█▓░ ████▓▒░▒██▒ ▒██▒░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
░▓  ░ ▒░   ▒ ▒ ░▒▓███▀▒░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░ ░░   ░ ▒░▒░▒   ░   ░ ▒ ▒░ ░░   ░▒ ░▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
 ▒ ░   ░   ░ ░  ░    ░ ░ ░ ░ ▒   ░    ░   ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ 
 ░           ░  ░          ░ ░   ░    ░   ░          ░ ░         ░    ░         ░  ░   ░     
                     ░                         ░                           ░ ''' + Fore.WHITE + ''' Created by R00tDev1l 
        ''')
print("")
t = str(input(Fore.GREEN + "Please write your text sms here: "))
y = int(input(Fore.GREEN + "Enter how many messeages you wanna sent: "))
z = int(input(Fore.RED + "How much time do you want before set up: "))
print("")
print(Fore.WHITE + "All set and clear to go!!!")
print("")
input(Fore.GREEN + "Press enter to continue" + Fore.RED + "\nBut remember your time limit buddy!")
time.sleep(z)
i = 1
while i<=y:
    pyautogui.typewrite(t)
    pyautogui.press('enter')
    i = i + 1