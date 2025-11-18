
import os
import smtplib


#tinker holds tkinter library
import tkinter as tinker
program_email = "YOU'LL NEVER KNOW EXCEPT ME"
# Prompt user to choose between creating a new folder or using an existing one
create = input("1.) Create a folder to store these passwords, 2.) Store in existing folder, 3.)Password Tester")

# def do_thing():
#     pass

#function for password tester 
def password_strength(password):
    points= 0
    special_char_count = 0
    status = '________'
    if password.length <= 8:
        points +=4
        points = 4
        status = "Weak...password too short"
    for char in password:
        special_chars = ["!","@","#","$","%","^","&","*","~"]
        nums = ["1","2","3","4","5","6","7","8","9","0"]
        #for each char in user_password check for special chars
        if char in special_chars:
            points+=3
            special_char_count +=1
        else:
            point -=2
        #for each char in user_password check for uppercasing 
        if password[char].isupper():
            points+=2
        else:
            points -=2
        #for each char check for nums
        if char in nums:
            points+=4
        else:
            points-=2
    
    if points >=12:
        status = "Perfect"
    elif points >=8:
        status = "Okay"
    
        
        
    
if create == "1":
    # Create a new folder
    folder_name = input("Make a name for the folder you can find this all in: ")
    os.makedirs(folder_name, exist_ok=True)
    print(f"If you go looking for these they will be inside of '{folder_name}'")
    
elif create == "2":
    # Use an existing folder
    folder_name = input("Enter name of existing folder: ")
    added_password = input("")
    

elif create == "3":
    #Mini password tester minigame 
    root  = tinker.Tk()

    def myClick():
        #format outcome of password test into text
        output =tinker.Label(root, text =" 4")


    #size of window
    root.geometry("800x500")
    root.title("Password Tester")

    #top of page instruction
    label = tinker.Label(root, text= "Enter Below", font = ("Arial",16))
    label.pack(padx=20, pady=20)
    textbox = tinker.Text(root,height=3, font=("Arial", 16))
    textbox.pack()

    #Confirm button
    Confirm_button= tinker.Button(root, text = "Test",padx=15 pady=10)
    Confirm_button.pack()


    #
    root.mainloop()


#3 = Inside password text implement option for 2Factor Authentication 
#4 = Forgot password - Using a librabry can send email containing things


# Prompt user for password details
specify = input("Name of password designation (basically what is it for): ")
password = input("Password: ")



# Combine the designation and password
combine = specify + ": " + password
file_name = "passwords.txt"
file_path = os.path.join(folder_name, file_name)

#send passwords to email

receiver_email = input("Add email for backup: ")


subject = "Password Manager"  

#Get passwords from txt file
message_passwords = "Password Set:  "

message = f"Subject: {subject} \n\n{message_passwords}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls() 

server.login(program_email, "fbbyaileaqdabnul")

server.sendmail(program_email,receiver_email, message)



# Write the combined string to the file
with open(file_path, 'a') as file:
    file.write(combine + '\n')

print(f"Password saved in '{folder_name}'")

#f is for formattting strings  



#Bin file thing ....... eventually 
