#File handling program in Python for Hacktoberfest 2021
import os
import time
from os import listdir
from os.path import isfile, join
import pathlib
from pathlib import Path
#Declare global variables

workAns = None
fileNameAns = None
#Function to get the path name of the files

def getFilePathName():
    return os.listdir(os.path.abspath(os.getcwd()))


#Function to handle the files. Read, overwrite, append or open/list folders

def handleFiles(fileNameAns):
    while True:
        tmp = input("What would you like to do with the file?\n-Read: r\n-Overwrite: w\n-Add some data: a\n-Open folder: o\n >:")

        if tmp == 'r' or tmp == 'a' or tmp == 'w':
            if tmp == 'r':
                print("\n\nOkey, here is the content of the file:\n")
                f = open(fileNameAns, "r")
                print(f.read())
                f.close()
            if tmp == 'w':
                print("Overwrite the file's content.")
                f = open(fileNameAns, "w")
                f.write(input("Add your new idea here:\n"))
                f.close()
                print("\nHere is the result:")
                f = open(fileNameAns, "r")
                print(f.read())
            if tmp == 'a':
                f = open(fileNameAns, "a")
                f.write(input("Add your new idea here:\n"))
                f.close()
                print("\nHere is the result:")
                f = open(fileNameAns, "r")
                print(f.read())
        if tmp == 'o':
            files = getFilePathName()

            for f in files:
                print(f)
        ans = input("Would you like to keep edit the file? y/n\n")
        if ans == 'n' or ans == 'close':
            return True
#Check if the file or folder exists


def checkFiles():
    while True:
        fileNameAns = input("\nAdd the fullname of the file (filename.py/folder):\n")
        #If the file name contains dot, it isn't a folder

        dotCheck = "."
        if dotCheck in fileNameAns:
            if os.path.exists(fileNameAns):
                print("\nSuccess! ", fileNameAns, " file exists!")

                #Call the function with the argument of the input file name
                if handleFiles(fileNameAns):
                    print("Thanks for the use!")
                    break
            else:
                print("\nWe are sorry, file doesn't exists.")
                #Short animation in the console window
                for i in range(0, 3):
                    time.sleep(1)
                    print(".")
        else:
            if fileNameAns == "close":
                print("Thanks for the use!")
                break
            else:

                if os.path.exists(fileNameAns):
                    print("\nSuccess! ", fileNameAns, " folder exists!")
                    #Add the file name with a backslash to the file's directory path
                    location = os.path.abspath(os.getcwd()) + "\\" + fileNameAns
                    #With this new location, opens the folder and with a for loop, print the files
                    print(pathlib.Path(location).iterdir)
                    files = os.listdir(location)

                    for f in files:
                        print(f)

                    if handleFiles(fileNameAns):
                        print("Thanks for the use!")
                        break
                else:
                    print("\nWe are sorry, file doesn't exists.")
                    for i in range(0, 3):
                        time.sleep(1)
                        print(".")

print("\nWelcome to the FileHandler.")
if input("List the files? Yes or No:\n").lower() == "yes":
    files = getFilePathName()

    for f in files:
        print(f)
    while workAns == None:
        workAns = input("Would you like to work with files?\nType 'Yes' or 'No'\nAnytime in the program, type 'close' as answer to stop the program.\n")
        if workAns.lower() == "yes":
            checkFiles()
        elif workAns.lower() == "no" or workAns.lower() == "close":
            print("Thanks for the use!")
            break
        else:
            print("\nYour answer is not correct. Type 'Yes' or 'No'.")
            workAns = None
            time.sleep(3)
else:
    print("Thanks for the use!")
