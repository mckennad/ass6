import sys, re, ParseFinanceMethods, requests, urllib
from bs4 import BeautifulSoup
from ParseFinanceMethods import mainOptions

choice = 0



print("--")
print ("Market information\n")


while (choice != 8):                    #Will loop until user chooses Quit
    choice = mainOptions()

    
