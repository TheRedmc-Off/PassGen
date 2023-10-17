import random
import time
import os
import sys

documentsdir = os.path.normpath(os.path.expanduser("~/Documents"))

#fini

Bl='\033[30m'
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

def fast_type(x):
    for y in x + "\n":
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(0.020)

def end():
   print('\n')
   fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Task successfully ended')
   fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Do you want to do something else?')
   print('\n')
   retry = input(f'{Wh}[ {Gr}? {Wh}] {Gr}y{Wh} to restart / {Gr}n{Wh} to exit: ')
   if retry == 'y':
        main()
   elif retry == 'n':
        exitprogram()
   else:
        error()

def exitprogram():
    fast_type(f'{Wh}[ {Gr}X {Wh}] {Gr}Stopping program{Wh}...')
    exit()

def error():
    fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Error: Something unexpected happened...')
    fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Please make sure that you type something correct the next time!')
    fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Restarting in PasswordGen section in 3 seconds...')
    time.sleep(1)
    print(f'{Wh}[ {Gr}+ {Wh}] #')
    time.sleep(1)
    print(f'{Wh}[ {Gr}+ {Wh}] #')
    time.sleep(1)
    print(f'{Wh}[ {Gr}+ {Wh}] #')
    fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Restarting{Wh}...')
    time.sleep(1)
    main()


def banner():
    os.system('cls')
    print(f"""{Gr}
        _____                                                                        _____                       
     __|__   |__  ____    ______  ______  __  __  __  _____  _____   _____        __|___  |__  ______  ____   _  
    |     |     ||    \  |   ___||   ___||  \/  \|  |/     \|     | |     \  ___ |   ___|    ||   ___||    \ | | 
    |    _|     ||     \  `-.`-.  `-.`-. |     /\   ||     ||     \ |      \|___||   |  |    ||   ___||     \| | 
    |___|     __||__|\__\|______||______||____/  \__|\_____/|__|\__\|______/     |______|  __||______||__/\____| 
       |_____|                       {Wh}<-Code by Theo Herbst->        {Gr}                |_____|             
                      {Wh}Very strong and secure password generator --- V1.3.5
    """)
                      



def main():
    banner()
    print('\n\n')
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*()-_+=<>?/.,'"

    all = uppercase + lowercase + numbers + symbols
    length = int(input(f'{Wh}[ {Gr}+ {Wh}] {Gr}Enter the length of the password: {Wh}'))
    numberpasswrd = int(input(f'{Wh}[ {Gr}+ {Wh}] {Gr}Number of passwords to generate: {Wh}'))
    print('\n')
    fast_type(f'{Wh}[ {Gr}+ {Wh}] {Gr}Do you want to save your passwords in "{Wh}{documentsdir}\passwords.txt{Gr}" directory?{Wh}')
    save = input(f'{Wh}[ {Gr}? {Wh}] {Gr}y{Wh} for saving file / {Gr}n{Wh} to not save: {Wh}')
    if save == 'y':
        print(f'\n{Wh}---------------------------------------------\n')
        count = 0
        with open(f'{documentsdir}\passwords.txt', 'w') as f:
            f.write(f'Your freshly-generated passwords:\n')
        fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}File "{Wh}{documentsdir}\passwords.txt{Gr}" has been created or reset for its current use!{Wh}')
        print(f'\n{Wh}---------------------------------------------\n')
        for _ in range(numberpasswrd):
            count = count + 1
            password = ''.join(random.choice(all) for _ in range(length))
            with open(f'{documentsdir}\passwords.txt', 'a') as f:
                f.write(f'{count}: {password}\n')
            fast_type(f'{count}: {password}')
        print(f'\n{Wh}---------------------------------------------\n')
        fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}all your passwords have been saved to: "{Wh}{documentsdir}\passwords.txt{Gr}"!{Wh}')
        fast_type(f"{Wh}[ {Gr}! {Wh}] {Gr}Please don't forget to move the {Wh}file{Gr} to\n      any other directory to avoid its data replacement!{Wh}")
        end()
    elif save == 'n':
        print(f'\n{Wh}---------------------------------------------\n')
        count = 0
        for _ in range(numberpasswrd):
            count = count + 1
            password = ''.join(random.choice(all) for _ in range(length))
            fast_type(f'{count}: {password}{Wh}')
        print(f'\n{Wh}---------------------------------------------\n')
        end()
    else:
        error()

banner()
print('\n\n')
fast_type(f'{Wh}[ {Gr}1 {Wh}] {Gr}Start PasswordGen tool')
fast_type(f'{Wh}[ {Gr}0 {Wh}] {Gr}Exit')
print('\n\n')
menu = input(f'{Wh}[ {Gr}+ {Wh}] {Gr}Password@Gen~# {Wh}')

if menu == '1':
   main()
elif menu == '0':
   exitprogram()
else:
   error()


