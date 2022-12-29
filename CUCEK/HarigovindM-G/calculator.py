#THIS IS A CALCULATOR APP
#importing the time module
import time
#ASCII art display
def display():
    print("   ___   _   _    ___ _   _ _      _ _____ ___  ___  ")
    time.sleep(0.5)
    print("  / __| /_\ | |  / __| | | | |    /_\_   _/ _ \| _ \ ")
    time.sleep(0.5)
    print(" | (__ / _ \| |_| (__| |_| | |__ / _ \| || (_) |   / ")
    time.sleep(0.5)
    print("  \___/_/ \_\____\___|\___/|____/_/ \_\_| \___/|_|_\ ")


#using a funtion input_taker to avoid repetition
#this function return a tuple of two digits entered by the user

def input_taker():
    a = int(input("enter the first number"))
    b = int(input("enter the second number"))
    return (a,b)

#function for displaying the answer

def output_display(t,symbol,answer):
    return "{} {} {} is {}".format(t[0],symbol,t[1],answer)

def addition_of_two_numbers():
    tup = input_taker()
    ans = tup[0] + tup[1]
    print(output_display(tup, "+", ans))

def multiplication_of_two_numbers():
    tup=input_taker()
    ans=tup[0]*tup[1]
    print(output_display(tup,"X",ans))


def subtraction_of_two_numbers():
    tup = input_taker()
    ans=tup[0]-tup[1]
    print(output_display(tup, "-", ans))

def division_of_two_numbers():
    tup=input_taker()
    ans = tup[0]/tup[1]
    print(output_display(tup, "/", ans))

def total():
    n=int(input("enter the number of elements you want to add together"))
    tot=0
    for i in range(1,n+1):
        x=int(input("Enter the element number {}".format(i)))
        tot=tot+x

    print("The sum is {}".format(tot))

display()
print("Welcome to the Calculator app")
print("-"*50)

while True:
    print("Main Menu")
    print("1.Add two numbers")
    print("2.Subtract two numbers")
    print("3.Multiply two numbers")
    print("4.Divide two numbers")
    print("5.Add more than two numbers")
    print("6.Exit")
    choice=input("Please enter your option")
    if choice=='1':
        addition_of_two_numbers()
    elif choice=='2':
        subtraction_of_two_numbers()
    elif choice == '3':
        multiplication_of_two_numbers()
    elif choice == '4':
        division_of_two_numbers()
    elif choice=='5':
        total()
    elif choice=='6':
        break
    else:
        print("Please enter a valid input")
