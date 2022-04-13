# File: grace_p1.py
# Author: Isaiah Grace
# Date: 2022/3/7
# Lab Section: Tuesday
# Email: isaiah.grace@maine.edu
# Description: Library inventory manager
# Collabs: N/a

#read stock of books on init
bookdict = {}

def addbook(dict, title, count=1):
    #adds count to title, adds title if not in dict
    if title in dict:
        dict[title] += count
        return
    dict.update({title: count})
    

#rem book, err if DNE
def rembook(list, title):
    pass

#print stock
def stockreport(list):
    pass

def populatelist(inlist):
    #load bookStock.txt into a dictionary on init
    file = open("bookStock.txt")
    for line in file:             # grab book title
        nextline = next(file)     # grab num of books
        addbook(inlist, line.strip(), int(nextline.strip()))



# start script ---------

populatelist(bookdict) #populates initlist in format [title, count]

print(bookdict)
