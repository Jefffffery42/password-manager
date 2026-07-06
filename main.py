#PAsssword manager
import os 
import getpass
import json
while True:
 print("===== Password Manager =====")
 print("1. Add Password")
 print("2. View Password")
 print("3. Search Password")
 print("4. Delete Password")
 print("5. Exit")
 try:
    usr_input = int(input("Choose one of the following  "))
 except ValueError:
    print("please enter a number ")
    continue
    
 if usr_input == 1:
    Website = input("Website")
    Username = input("Username")
    Password = getpass.getpass("Password:")
    NewPasswd = {
       "website": Website,
       "Username": Username,
       "Password": Password
       }
 elif usr_input == 2:
    print("Coming soon")
 elif usr_input == 3:
    print("Coming soon")
 elif usr_input == 4:
    print("Coming soon")
 elif usr_input == 5:
    print("Goodbye")
    break
 else:
    print("Invalid choice!")