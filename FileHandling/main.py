import os
import time
workAns = None

def handleFiles():
    while True:
        tmp = input("What would you like to do with the file?\n-Read: r\n-Overwrite: w\n-Add some data: a\n >:")

        if tmp == 'r' or tmp == 'a' or tmp == 'w':
            if tmp == 'r':
                print("\n\nOkey, here is the content of the file:\n")
                f = open("demo.txt", "r")
                print(f.read())
                f.close()
            if tmp == 'w':
                print("Overwrite the file's content.")
                f = open("demo.txt", "w")
                f.write(input("Add your new idea here:\n"))
                f.close()
                print("\nHere is the result:")
                f = open("demo.txt", "r")
                print(f.read())
            if tmp == 'a':
                f = open("demo.txt", "a")
                f.write(input("Add your new idea here:\n"))
                f.close()
                print("\nHere is the result:")
                f = open("demo.txt", "r")
                print(f.read())
        ans = input("Would you like to keep edit the file? y/n\n")
        if ans == 'n':
            return True

def checkFiles():
    fileNameAns = None
    while True:
        fileNameAns = input("\nAdd the fullname of the file (example.py):\n")
        if os.path.exists(fileNameAns):
            print("\nSuccess! ", fileNameAns, " file exists!")
            if handleFiles():
                print("Thanks for the use!")
                break
        elif fileNameAns == "close":
            print("Thanks for the use!")
            break
        else:
            print("\nWe are sorry, file doesn't exists.")
            for i in range(0,3):
                time.sleep(1)
                print(".")

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


