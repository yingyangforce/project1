# File: grace_p1.py
# Author: Isaiah Grace
# Date: 2022/3/7
# Lab Section: Tuesday
# Email: isaiah.grace@maine.edu
# Description: Library inventory manager
# Collabs: N/a

#read stock of books on init
initlist = []

def populatelist(inlist):
    file = open("bookStock.txt")
    for line in file:
        nextline = next(file)
        inlist.append([line.strip(), int(nextline.strip())])

populatelist(initlist) #populates initlist in format [title, count]

#store book title, quantity in 2d list


#add book
def addbook():
    pass

#rem book, err if DNE
def rembook():
    pass

#print stock
def stockreport():
    pass
