from itertools import *
from random import *
import string

def generator(file1,passw,n):
    for i in product(passw,repeat=n):
        file1.write("".join(i)+"\n")

def customlength():
    n = int(input("Enter length"))
    return n

def randomLength():
    n = randint(1,16)
    return n

def customPass():
    passw = str(input("Enter letters/numbers/special symbols you want in the worlist"))
    return passw

def randomPass():
    n  = randint(1,10)
    r = "".join(choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation,k = n))
    return r

print("\t*-----Wordlist Generator-----*")


print("Enter path carefully")
print("It will rewrite the file if the file exist on the path mentioned")
a = str(input("Enter Absolute or Relative Path with File Name"))
file1 = open(a,"w")

print("How do you want to make your wordlist?")
print("1.Random length and using all the letters/alphabets/special symbols")
print("2.Random length using custom letters/alphabets/special symbols")
print("3.Custom length using random letters/alphabets/special symbols")
print("4.Custom length using custom letters/alphabets/special symbols")
print("5.Random length using random letters/alphabets/special symbols")
choice = int(input("Enter a choice"))

while(choice):
    if(choice == 1):

        print("\tWARNING!!")
        print("This may take some time to complete and it will consume a lot of memory")
        print("This option is not recommended")
        print("Your System can hang")
        print("Do you still want to continue?")
        print("1.Yes")
        print("2.No, I want to change my choice")
        c = int(input("Enter a choice"))
        if(c == 1):
            n = randomLength()
            passw = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_=+><.,/?"
            generator(file1,passw,n)
            choice = 0
        else:
            choice = int(input("Enter another choice"))



    elif(choice == 2):
        n = randomLength()
        passw = customPass()
        generator(file1,passw,n)
        choice = 0

    elif(choice == 3):
        n = customlength()
        passw = randomPass()
        generator(file1,passw,n)
        choice = 0

    elif(choice == 4):
        n = customlength()
        passw = customPass()
        generator(file1,passw,n)
        choice = 0
        
    elif(choice == 5):
        n = randomLength()
        passw = randomPass()
        generator(file1,passw,n)
        choice = 0


print("Wordlist created at"+a)
