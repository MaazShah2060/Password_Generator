import random
import string
import os
import time
size = 0
def pw_gen():
    size=int(input('How many characters Do you want in your password(not minimum than 6)?'))

    def pw_char(chars=string.ascii_letters):
        return ''.join(random.choice(chars))

    def pw_digits(chars=string.digits):
        return ''.join(random.choice(chars))

    def pw_symbols(chars=string.punctuation):
        return ''.join(random.choice(chars))

    if(size>=6):
        num = int(input('how much numbers you want in your password?'))
        alpha = int(input('how many alphabets you want in your password?'))
        if(size>=num+alpha):
            for i in range (num):
                print(pw_digits(),end="")
            for i in range (alpha):
                print(pw_char(),end="")
            for i in range (size-alpha-num):
                print(pw_symbols(),end="")
        else:
            print("Invalid Range!!! Kindly correct")
            input("Press Enter to continue...")
            
            os.system('cls')
            pw_gen()
    else:
        print("Invalid Range!!! Kindly correct")
        input("Press Enter to continue...")
        os.system('cls')
        pw_gen()
    input("\nPress Enter to Exit...")
pw_gen()
