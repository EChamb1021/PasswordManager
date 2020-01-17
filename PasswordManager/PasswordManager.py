#Name: Evan Chambers
#Date: Wednesday, January 15th, 2020
#Description: This program is a password manager which allows the user to generate a random password for a service, retrieve a password,
#             and change a password.  

#MASTER PASSWORD: Shopify123


#Importing OS to change to the directory where the script is located 
import os

#Import string for string manipulation
import string

#Random used to generate random strings for secure passwords
import random

#This module is used to ensure that the master password used to login to the system is not displayed in plain text 
from getpass import getpass

#Changing directory to where python script is located
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#Opening the file where the master password and all subsequent passwords will be stored 
with open("passwords.txt", "r") as f:

    #The master password is in the first line of the file and is stored in the constant MASTER_PASSWORD
    MASTER_PASSWORD = f.readline().strip("\n").split(",")[1]

#Dictionary (database) where passwords will be stored in the program 
pass_dict = {}

#Creating a list of upper and lowercase characters and numbers 0-9 to be used for passwords generating later in the program
char_list = list(string.ascii_lowercase + string.ascii_uppercase)
num_list = list(string.digits)

#This is the main menu the user will see after logging in 
def main_menu():
    
    #Main loop
    while True:
        update_dict()

        print("Select an option:")
        print("1. Get a password")
        print("2. Generate a password")
        print("3. Change a password")
        print("4. Quit")
        try:
            option = int(input())
            if option == 1:
                get_password()
            elif option == 2:
                generate_password()
            elif option == 3:
                change_password()
            elif option == 4: 
                exit(0)
            else:
                print("Error.  Invalid Option.")
                main_menu()
        except ValueError:
            print("Error.  Invalid Option.")
            main_menu()

#This function allows the user to change their password 
def change_password():

    #Prompts the user to enter a service until the service is valid (i.e. in the dictionary)
    while True:
        service = input("Enter service:")
        service = service.lower()

        if service not in pass_dict:
            print("Service not found")
        else:
            break

    #Getting old password and new password 
    old_password = pass_dict[service]
    new_password = input("Enter new password: ")
    
    #Reads each line of the file
    with open("passwords.txt", "r") as f:
        lines = f.readlines()

    #Rewrites the file with the updated password 
    with open("passwords.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != "{},{}".format(service,old_password):
                f.write(line)
        f.write("{},{}\n".format(service,new_password))
    print("Password changed successfully.")


#This function retrieves a password for the user 
def get_password():
    
    #Getting the service from the user
    service = input("Enter service:")
    service = service.lower()
    update_dict()

    #Tries to retrieve the password from the database if it exists
    try:
        passphrase = pass_dict[service]
        
        print("Password for " + service + " is " + passphrase + ".\n")
    
    #If the service is not in the dictionary, an error message is displayed and the user is prompted to try again
    except KeyError:
        print("Service Not Found.  Please Try Again.")
        get_password()
    
    return

#This function generates a password of the desired length consisting of random alphanumeric characters 
def generate_password():

    #Get the service from the user 
    service = input("Enter new service: ")
    service = service.lower()

    #Get the desired password length
    pass_length = int(input("Enter Password Length: "))
    
    generated_password = ""

    for i in range (pass_length):

        #Generates either 1 or 2 randomly so there is an equal chance of appending a letter or a character to the password
        num = random.randint(1,2)

        #If 1 is generated then a letter is added and if a 2 is generated then a number is added
        if num == 1:
            generated_password = generated_password + random.choice(char_list)
        else:
            generated_password = generated_password + random.choice(num_list)
    
    print("Password generated successfully.  ")
    
    with open("passwords.txt", "a") as f:
        f.write("{},{}\n".format(service,generated_password))
    
    update_dict()

    print("Password stored successfully.  ")

    #Telling the user what the password is 
    print("Password for " + service + " is " + generated_password + ".")

#This function updates the database/dictionary
def update_dict():

    #Clears the dictionary initially
    pass_dict.clear()
    

    with open("passwords.txt", "r") as f:
        for line in f:
            line = line.strip("\n")

            #Getting the comma separated service and password and storing them in a list
            elements = line.split(",")

            #If the file has nothing in it, then the function exits
            if len(elements) == 1:
                break

            #Otherwise the service and password from each line are stored in the dictionary respectively
            else:
                service = elements[0]
                password = elements[1]
                pass_dict.update({service:password})
        


#Initial Home Screen seen when program runs
while True:

    #Password Prompt that keeps the text entered hidden
    password = getpass("Welcome, Enter your password: ")

    #If the password is correct then the system gives access to the user
    if password == MASTER_PASSWORD:
        update_dict()
        main_menu()
        break

    #Otherwise it asks the user to try again.  
    else:
        print("Incorrect Password.  Try Again.")


