import random
import os

class UserClass:
    def __init__(self, name = "John Doe" , score = 0):
        self.name = name
        self.score = score
        
    def userWin(self):
        self.score = self.score +1

def playNext():
    print("Do you want to continue the game.")
    playOption = input("Press x to quit: ")
    
    return playOption
    

def userName(nr):
    valid = False
    
    while(valid == False):
        userN = input("Player " + nr + " enter your name : ")
        
        if(userN != ''):
            valid = True
        else:
            print("You must enter a name.")
            
    return userN
            

def generateRand():
    return random.sample(range(0,3),3)


def asignItem():
    stringIt = ["rock", "papper", "scissors"]
    listIt = [' ', ' ', ' ']
    indexIt = generateRand()
    j = 0
    
    for i in indexIt:
        listIt[i] = stringIt[j]
        j +=1
        
    return listIt
    
def playerInput(name1, name2):
    
    getOut = False
    
    while(getOut == False):
        try:
            player1 = int(input(name1 + " : Select a number from 1 to 3: "))
            player2 = int(input(name2 + " : Select a number from 1 to 3: "))
        
            if((player1 <= 3 and player1 >= 1) and (player2 <= 3 and player2 >= 1)):
                getOut = True
            else:
                print("The selected number must be : 1, 2 or 3!")
                
        except:
            print("Error: Enter a number!")
    
    return player1 ,  player2
    
       

def theWinner(player1Name, player2Name, player1Opt, player2Opt):
    if(player1Opt == "rock" and player2Opt == "papper") or (player2Opt == "rock" and player1Opt == "papper"):
        if player1Opt == "papper":
            print("Papper beats Rock. " + player1Name + " Wins!")
            return player1Name
        else:
            print("Papper beats Rock. " + player2Name + " Wins!")
            return player2Name
            
            
    elif(player1Opt == "rock" and player2Opt == "scissors") or (player2Opt == "rock" and player1Opt == "scissors"):
        if player1Opt == "rock":
            print("Rock beats Scissors. " + player1Name + " Wins!")
            return player1Name
        else:
            print("Rock beats Scissors. " + player2Name + " Wins!")
            return player2Name
    
    elif(player1Opt == "papper" and player2Opt == "scissors") or (player2Opt == "papper" and player1Opt == "scissors"):
        if player1Opt == "scissors":
            print("Scissors beats Papper. " + player1Name + " Wins!")
            return player1Name
        else:
            print("Scissors beats Papper. " + player2Name + " Wins!")
            return player2Name
            
    elif(player1Opt == player2Opt):
        print("Draw, both Players have " + player1Opt)
        
        return 0
    
    
def toSaveGame(saveFile, saveNr, player1Name, player1Score, player2Name, player2Score):
    openSaveGameFile = open(saveFile, "a")
    saveGameName = input("Insert a title for the saved game:  ")
                    
    openSaveGameFile.write(str(saveNr) + " ### " + saveGameName)
    openSaveGameFile.write(" " + player1Init.name + " has: " + str(player1Init.score) + " points")
    openSaveGameFile.write(" " + player2Init.name + " has: " + str(player2Init.score) + " points" + "\n")
    openSaveGameFile.write("")

                
    openSaveGameFile.close()
    
        
        
if __name__ == "__main__":
    
    saveGameNr = 1
    
    saveGameFile = 'C:/Users/Florentin/Documents/Python/MyPyWorld/RPS game/SavedGames.txt'
    
    if(os.stat(saveGameFile).st_size == 0):
    
        gamestatus = True
    
    
        player1 = userName('1')
        player2 = userName('2')
    
        player1Init = UserClass(player1)
        player2Init = UserClass(player2)
    
    
        while(gamestatus):
    
            opt1,opt2 = playerInput(player1Init.name, player2Init.name)
    
    
            opt1 = asignItem()[(opt1) - 1]
            print(player1Init.name + " has : " + opt1)
    
            opt2 = asignItem()[(opt2) - 1]
            print(player2Init.name + " has : " + opt2)
    
            winner = theWinner(player1Init.name, player2Init.name, opt1, opt2)
        
            if(winner == player1Init.name):
                player1Init.userWin()
            elif(winner == player2Init.name):
                player2Init.userWin()
        
            print("The score is: ")
            print(player1Init.name + " has: " + str(player1Init.score) + " points")
            print(player2Init.name + " has: " + str(player2Init.score) + " points")
        
            if('x' == playNext().lower()):
                print("Game Over!")
                saveGame = input("Do you want to save the game? Press 'y' if you want to save the game: ")
                
                if(saveGame.lower() == 'y'):
                    
                    toSaveGame(saveGameFile, saveGameNr, player1Init.name, player1Init.score, player2Init.name, player2Init.score )
                    
                gamestatus = False
    
    else:
        gamestatus = True
        
        openSaveGameFile = open(saveGameFile, "r")
        fileReadLine = openSaveGameFile.readlines()
        countLines = 0
        openSaveGameFile.close()
        
        for i in fileReadLine:
            print(i)
            countLines +=1
           
        
        ifOptOk = True
        
        
        while(ifOptOk):
            userOptSaveGame = (input("Enter the number of the Saved game: "))
            userOptSaveGame = int(userOptSaveGame) - 1
            if(userOptSaveGame > countLines):
                print("Select a valid number!")
            
            else:
                userOptLine = fileReadLine[userOptSaveGame].split()
                ifOptOk = False
        
        
        
        player1Init = UserClass(userOptLine[3], int(userOptLine[5]))
        player2Init = UserClass(userOptLine[7], int(userOptLine[9]))
        
        print("The score is: ")
        print(player1Init.name + " has: " + str(player1Init.score) + " points")
        print(player2Init.name + " has: " + str(player2Init.score) + " points")
        
        while(gamestatus):
    
            opt1,opt2 = playerInput(player1Init.name, player2Init.name)
    
    
            opt1 = asignItem()[(opt1) - 1]
            print(player1Init.name + " has : " + opt1)
    
            opt2 = asignItem()[(opt2) - 1]
            print(player2Init.name + " has : " + opt2)
    
            winner = theWinner(player1Init.name, player2Init.name, opt1, opt2)
        
            if(winner == player1Init.name):
                player1Init.userWin()
            elif(winner == player2Init.name):
                player2Init.userWin()
        
            print("The score is: ")
            print(player1Init.name + " has: " + str(player1Init.score) + " points")
            print(player2Init.name + " has: " + str(player2Init.score) + " points")
        
            if('x' == playNext().lower()):
                print("Game Over!")
                saveGame = input("Do you want to save the game? Press 'y' if you want to save the game: ")
                
                if(saveGame.lower() == 'y'):
                    countLines = countLines + 1
                    toSaveGame(saveGameFile, countLines, player1Init.name, player1Init.score, player2Init.name, player2Init.score  )
                    
                gamestatus = False
        
        
        
        
        openSaveGameFile.close()
    
        
    
    
    

