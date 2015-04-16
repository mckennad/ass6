import requests
from bs4 import BeautifulSoup


def mainOptions():
#Asks for input, checks validity, loops if not valid otherwise calls appropriate method

    onTheFence = True

    while(onTheFence):
        print("\nSelect one of the following :\n")
        print("1) S&P TSX \n2) S&P 500 \n3) Dow Jones \n4) Nasdaq \n5) CAD/USD \n6) Gold \n7) WTI Crude \n8) Quit \n")

        checkingInput = True
        while(checkingInput):
            checkForNum = True
            while(checkForNum):
                try:
                    choice = int(input())
                except ValueError:
                    print("\nThat is not an option, please try again.")
                    #catches whether input is a numeral
                else:
                    checkForNum = False
            if (choice == 1):
                checkingInput = False
                displaySP_TSX()
                return choice
            elif (choice == 2):
                checkingInput = False
                displaySP_500()
                return choice
            elif (choice == 3):
                checkingInput = False
                displayDow_Jones()
                return choice
            elif (choice == 4):
                checkingInput = False
                displayNasdaq()
                return choice
            elif (choice == 5):
                checkingInput = False
                displayCADUSD()
                return choice
            elif (choice == 6):
                checkingInput = False
                displayGold()
                return choice
            elif (choice == 7):
                checkingInput = False
                displayWTI_Crude()
                return choice
            elif (choice == 8):
                checkingInput = False
                return choice
            else:
                print("You must choose an option between 1-8.  Please try again.")

        onTheFence = False


#-----------------------------------

def displaySP_TSX():

    
    url = 'http://www.theglobeandmail.com/globe-investor/'      #v1 of grabbing web page and placing in BeautifulSoup
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)

    print("\nS&P TSX ", end = "")


    currVal = soup.find('div', {'data-id': '593253'}).find('div', {'class': 'prominent less-prominent last-value chars9'}).text
    #Finds current value of S&P TSX and stoes it
    changeVals = soup.find('div', {'data-id': '593253'}).find('div', {'class': 'change'}).text
    #Finds numeral change and percentage change of S&P TSX and stores it
    lastUpdate = soup.find('div', {'data-id': '593253'}).find('span', 'timing update-info').text
    #Finds out when the last update for S&P TSX occurred and stores it

    print(currVal, changeVals, "last updated", lastUpdate)
    #Prints out all stored values in specified format




#-----------------------------------

def displaySP_500():
#Same approach as S&P TSX, with small modifications
    

    html = (requests.get('http://www.theglobeandmail.com/globe-investor/')).content
    soup = BeautifulSoup(html)


    currVal = soup.find('div', {'data-id': '575769'}).find('div', {'class': 'prominent less-prominent last-value chars8'}).text

    changeVals = soup.find('div', {'data-id': '575769'}).find('div', {'class': 'change'}).text

    lastUpdate = soup.find('div', {'data-id': '575769'}).find('span', 'timing update-info').text
    

    print("\nS&P 500 ", currVal, changeVals, "last updated", lastUpdate)


#-----------------------------------

def displayDow_Jones():
#Same approach as S&P TSX, with small modifications

    soup = BeautifulSoup((requests.get('http://www.theglobeandmail.com/globe-investor/')).content)


    currVal = soup.find('div', {'data-id': '599362'}).find('div', {'class': 'prominent less-prominent last-value chars9'}).text

    changeVals = soup.find('div', {'data-id': '599362'}).find('div', {'class': 'change'}).text

    lastUpdate = soup.find('div', {'data-id': '599362'}).find('span', 'timing update-info').text
    

    print("\nDow Jones ", currVal, changeVals, "last updated", lastUpdate)


#-----------------------------------

def displayNasdaq():
#Same approach as S&P TSX, with small modifications
    
    soup = BeautifulSoup((requests.get('http://www.theglobeandmail.com/globe-investor/')).content)


    currVal = soup.find('div', {'data-id': '579435'}).find('div', {'class': 'prominent less-prominent last-value chars8'}).text

    changeVals = soup.find('div', {'data-id': '579435'}).find('div', {'class': 'change'}).text

    lastUpdate = soup.find('div', {'data-id': '579435'}).find('span', 'timing update-info').text
    

    print("\nNasdaq ", currVal, changeVals, "last updated", lastUpdate)


#-----------------------------------

def displayCADUSD():
#Same approach as S&P TSX, with small modifications

    soup = BeautifulSoup((requests.get('http://www.theglobeandmail.com/globe-investor/')).content)


    currVal = soup.find('div', {'data-id': 'Currencies'}).find('span', 'prominent less-prominent').text

    changeVals = soup.find('div', {'data-id': 'Currencies'}).find('div', {'class': 'change'}).text

    lastUpdate = soup.find('div', {'data-id': 'Currencies'}).find('span', 'timing update-info').text
    

    print("\nCAD/USD ", currVal, changeVals, "last updated", lastUpdate)


#-----------------------------------

def displayGold():
#Same approach as S&P TSX, with small modifications
    
    soup = BeautifulSoup((requests.get('http://www.theglobeandmail.com/globe-investor/')).content)


    currVal = soup.find('div', {'data-id': 'Commodities'}).find('div', {'class': 'value prominent less-prominent'}).text

    changeVals = soup.find('div', {'data-id': 'Commodities'}).find('div', {'class': 'change'}).text

    lastUpdate = soup.find('div', {'data-id': 'Commodities'}).find('span', 'timing update-info').text
    

    print("\nGold ", currVal, changeVals, "last updated", lastUpdate)


#-----------------------------------

def displayWTI_Crude():
#Same approach as S&P TSX, with small modifications

    soup = BeautifulSoup((requests.get('http://www.theglobeandmail.com/globe-investor/')).content)


    currVal = soup.find_all('div', {'data-id': 'Commodities'})[1].find('div', {'class': 'value prominent less-prominent'}).text

    changeVals = soup.find_all('div', {'data-id': 'Commodities'})[1].find('div', {'class': 'change'}).text

    lastUpdate = soup.find_all('div', {'data-id': 'Commodities'})[1].find('span', 'timing update-info').text
    

    print("\nWTI Crude ", currVal, changeVals, "last updated", lastUpdate)  


#-----------------------------------
