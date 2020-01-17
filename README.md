# Password Manager
This is a console application written in Python that manages passwords.  The application allows users to retrieve one of their passwords, generate a random password of a specified length, and change a password.  The passwords and services are stored in a text file called passwords.txt, but in future updates I plan to store the passwords in a more secure way.  

When the application runs, it asks for a master password.  The password is Shopify123 but this can be changed in the passwords.txt file.  The program then prompts the user to enter a number between 1 and 4 to select one of the following options.  

Get a password: 

The user is asked to enter a service such as Shopify for example.  Then the program retrieves the password from the text file and returns it to the user so they can copy and paste it to login.

Generate a password:

The user is asked to enter a service once again.  Then the user is prompted to enter the length of the password they wish to generate.  The program then returns a password consisting of random numbers and characters of the specified length.  This makes for a very safe password which does not need to be memorized as it is stored by the program.  

Change a password:

The user is asked to enter a service.  Then they are asked to enter the new password they wish to set.  Once they enter the new password the program updates the text file.  

The passwords are stored in the following format:

service1,password1
service2,password2
service3,password3

Once again storing passwords in plain text like this is not secure at all.  This project was mainly to understand how to store information such as passwords in a file and be able to access them.  In future updates as I learn more about cybersecurity I will store the passwords in a safer way.   
