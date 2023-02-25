import random
from tkinter import *
import tkinter.messagebox



#Password
class passCreator:
    def __init__(self,length):
        self.length=length
        
        
    def createPass(self):
        passChars = [33,126]
        password = []
        for i in range(self.length):
            passChar = chr(random.randint(passChars[0],passChars[1]))+""
            password.append(passChar) 
        
        #Array = 
        #return type string
        finalPass =  ''.join(password)
        print(finalPass)
        return finalPass

#Get password
def getPass(length):
    objPassCreator = passCreator(length)
    fetchedPass = objPassCreator.createPass()
    return fetchedPass

#Write into file
def writeInFile(content):
    try: #error handling
        fileToWrite = open("passDb.txt","a")
        
    except PermissionError:
        return "Error!"
    finally:
        fileToWrite.write(content+"\n")
        fileToWrite.close()
    
#Structure Data in File
def structureData(email,website,password):
    salt = "1@*"
    structuredFormat = email + ": " + website + ":"+salt+ ""+ password[0]
    return structuredFormat
    
 #store data
def storeData():
    if len(email.get()) !=0 and len(website.get()) !=0: 
        contentFinal = structureData(email.get(), website.get(), password)
        writeInFile(contentFinal)
        return True
    else:
        return False 
#UI Integration
window = Tk()

window.title("Password Manager")

#Form Fields
emailLabel = Label(window, text="Email").grid(row=0, column=0)
email = StringVar()
emailEntry = Entry(window, textvariable=email, show='*').grid(row=0, column=1) # add show option to hide email input
websiteLabel = Label(window, text="Website").grid(row=1, column=0)
website = StringVar()
webUrlEntry = Entry(window, show = '*' ,textvariable=website).grid(row=1, column=1) 


# Hey Password

password = [""]

#Clear Field

#store Button function
def store():
    if storeData():
        
        tkinter.messagebox.showinfo("Pass Status","Password Stored in Secure DB") #file handling
        
        
    else:
        tkinter.messagebox.warning("Error!")
    
def showPass():
    password[0] = getPass(64)
    passLabel = Label(window,text=password[0]).grid(row=2,column=2)

#Generate Passss
generateButton = Button(window, text="Generate Password", command=showPass).grid(row=2, column=1) 
#store Button
storeButton = Button(window, text="Store This Password", command=store).grid(row=3, column=2)

#Okay
window.mainloop()