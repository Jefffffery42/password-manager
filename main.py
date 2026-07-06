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
    website = input("Website: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    new_password = {
       "Website": website,
       "Username": username,
       "Password": password
       }
    with open("passwords.json" ,"r") as file:
       passwords = json.load(file)
       passwords.append(new_password)  
       with open("passwords.json", "w") as file:
          json.dump(passwords,file, indent=4)
          print("Password saved successfully")
    
 elif usr_input == 2:
    with open("passwords.json", "r") as file:
       data = json.load(file)
       print(json.dumps(data, indent=4))
   
 elif usr_input == 3:
    searched_site = input("Enter enter your site eg gmail discord etc: ")
    with open("passwords.json", "r") as file:
       passwords = json.load(file)
       for item in passwords:
          if item ["Website"] == searched_site:
             print(item["Password"])
          
 elif usr_input == 4:
    print("Coming soon")
 elif usr_input == 5:
    print("Goodbye")
    break
 else:
    print("Invalid choice!")