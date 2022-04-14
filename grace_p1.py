# File:         grace_p1.py
# Author:       Isaiah Grace
# Date:         2022/3/7
# Lab Section:  Tuesday
# Email:        isaiah.grace@maine.edu
# Description:  Library inventory manager
# Collabs:      N/a

#  ---Project 1---

bookdict = {}  #read stock of books on init

def addbook(dict, title, count=1):  #adds count to title,
    if title in dict:               #adds title if not in dict
        dict[title] += count
        return
    dict.update({title: count})

def rembook(dict, title):  #rem book, err if DNE
    if title in dict:
        dict[title] -= 1     #decr book count if in dict && count > 0
        if dict[title] < 1:
            dict.pop(title)  #rm book from list if count < 1
        return
    print(f"I can't find '{title}' in my list. Please check title formatting.")

def stockreport(dict):  #print report on current book stock
    print('\nStock Report -')
    for title in dict:
        print(f" • '{title}' ({dict.get(title)})")
    print()

def populatelist(inlist):  #load bookStock.txt into a dictionary on init
    file = open("bookStock.txt")
    print()
    for line in file:           # grab book title
        nextline = next(file)   # grab num of books
        addbook(inlist, line.strip(), int(nextline.strip()))

def inputloop():  #logic handler for inputs, functions
    print("-Welome to BookStock v0.0.1-")
    usrinput = input("Please enter a command (or [q] to quit): ")

    while usrinput != 'q':
        if usrinput == 'a':
            addbook(bookdict, input("What book would you like to add?: "))
        if usrinput == 'r':
            rembook(bookdict, input("What book would you like to remove?: "))
        if usrinput == 'p':
            stockreport(bookdict)
        if usrinput == 'help':
            print("[a] -> Add a book to the stock.")
            print("[r] -> Remove a book from the stock.")
            print("[p] -> Print a book stock report.")

        usrinput = input("Please enter a command (or [q] to quit): ")

    print("Goodbye")

# start script ---
populatelist(bookdict)  #populates bookdict in format {title: count}
inputloop()
