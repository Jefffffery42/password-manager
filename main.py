#PAsssword manager
import os 
import random
import getpass
import json
while True:
 print("""===== Password Manager =====
 1. Add Password
 2. View Password
 3. Search Password
 4. Delete Password
 5. Generate Password      
 6. Exit""")
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
    searched_site = input("Enter the website you want to remove the password of...")
    with open("passwords.json", "r") as file:
       passwords = json.load(file)
       for item in passwords:
          if item ["Website"] == searched_site:
             passwords.remove(item)
             with open("passwords.json" , "w")as file:
              json.dump(passwords, file, indent=4 )
              print("Password deleted successfuly")
              break
 elif usr_input == 5:
     try:
      password_len = int(input("Enter the length of the password "))
     except ValueError:
      (print("Enter a number"))
     if password_len <=0:
       print("Enter number bigger than 0 lmao ")
       continue
     all_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
     characters = (random.choices(all_characters, k = password_len))
     password = "".join(characters)
     print(f"Generated password: {password}")               
 elif usr_input == 6:
    print("Goodbye")
    break
 else:
    print("Invalid choice!")

 


