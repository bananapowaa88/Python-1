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
        break
