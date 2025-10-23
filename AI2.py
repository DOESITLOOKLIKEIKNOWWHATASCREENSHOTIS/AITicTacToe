#Data base, which is a dictornay, with keys that are every possiable postion in the game 
#The data base would start off empty. We would create a new list element when the AI encounters a new postion.
#Each key of postions would have 2 elements. A list of every possible move, and a list of numbers. The numbers are the 
#chance for each possiable movement.

#Imports importlib and random
import importlib
import random 

#Imports classvalues from AImodule.py, as values 
from AI2module import classvalues as values

#Initializes values as a class. Otherwise, we can only access values and not functions.
values = values()

try: 
    #Uses importlib to import what whatever values.fileName is
    data = importlib.import_module(values.fileName)

    #Sets data_loaded_postions
    data_loaded_postions = data.data_loaded_postions
except: 
    #If there's an error, we need to create a new file that's named whatever values.fileName is
    print(f"The file {values.fileName} is missing! Creating new file!")
    
    f = open(f"{values.fileName}.py", "w")
    f.write("data_loaded_postions = {}")
    f.close()
    
    data = importlib.import_module(values.fileName) 
    data_loaded_postions = data.data_loaded_postions
    
    print("Created!")


#A function that if values.debugInformation, will print whatever string is. 
def doIPrint(string):
    if values.debugInformation:
        print(string)

#The postion data
loaded_postions = data_loaded_postions

#The history of moves for the current game
history_of_moves = {}

#main needs the current board and what avaible_moves are there. Which is what TicTacToe.py SHOULD BE providing.
def main(current_board, avaiable_moves):

    #Checks if the AI doesn't has the data of the curret board
    #If the AI doesn't have the data, we need to add the data immediately.  
    while True:

        if current_board in loaded_postions:
            #move equals whatever playamove returns
            move = playamove(current_board)

            #returns move to TicTacToe.
            return move
        else:
            doIPrint("New to create a new move set.")

            #Create an empty that's later going to be filled with numbers 
            listOfNumbers = []

            #For each element, add values.standard to a list called listOfNumbers
            for x in list(avaiable_moves):
                listOfNumbers.append(values.standard)

            #Adds data to loaded_postions
            loaded_postions[current_board] = {"Moves" : avaiable_moves, "Chances" : listOfNumbers}
            
            #Now update and play
            update_data(loaded_postions)

def playamove(current_board):

    #Create an empty lsit that's later going to be filled with numbers .
    doIPrint( f"Moves: {loaded_postions[current_board]["Moves"]}")
    doIPrint( f"Chances: {loaded_postions[current_board]["Chances"]}")

    #total is the value that gets added to. 
    total = 0
    
    #For each element in chance, added the value of chance to total
    for chance in loaded_postions[current_board]["Chances"]:
        total = total + chance

    #Picks a random number from 0, to total. Includes decimals
    choosennumber = random.uniform(0,total)
    doIPrint(f"choosennumber: {choosennumber}")

    '''
        This code is rather complex. What it's doing is if the choosennumber is not less then the current element in the list + addive, 
        then addive gets added by the current element in the list and choice gets added by 1. If the choosennumber is less then the current element
        then choice is the choosen move. 
    '''
    addive = 0
    choice = 0
    for numberofchance in loaded_postions[current_board]["Chances"]:
        if choosennumber < (numberofchance + addive):
            doIPrint( f"Placing down a point on:  {choice}")
            break
        else:
            addive = addive + numberofchance
            choice = choice + 1
    
    #Saves choosen move to history_of_moves
    history_of_moves[current_board] = loaded_postions[current_board]["Moves"][choice]

    doIPrint( f"history of moves {history_of_moves}")

    #Returns the move that the AI wants to play
    return loaded_postions[current_board]["Moves"][choice]

def is0orneagtive(number):
    if number <= 0:
        #The number is less or equal to 0. Forces the number to be 0.1
        print("IT'S 0 OR NEAGTIVE!!!!")
        number = 0.1
    return number


def findMove(history_of_moves, number):

    #Revereses the list because we want to effect the last move the AI made first.
    historyList = list(reversed(history_of_moves))

    doIPrint( f"Historylist:  {historyList}")

    #Gets the move we want to modify.
    moveLocation = historyList[number]

    doIPrint( f"movelocation: {moveLocation}")

    doIPrint( f"The move when it was in this postion:  {history_of_moves[moveLocation]}")

    #Gets the index of the move we want to modify.                
    postion = loaded_postions[moveLocation]["Moves"].index(history_of_moves[moveLocation])

    doIPrint( f"postion:  {postion}")
    
    #Returns historyList, moveLocation
    return historyList, moveLocation, postion, loaded_postions[moveLocation]["Chances"][postion]



#TicTacToe_commuation requests function is for when the TicTacToe.py needs information sent over to it, or when TicTacToe needs information to be sent over the AI.
#Data is what addiatonal information is sent (like if the AI won, lost, or if it was a tie).
def TicTacToe_communation(data):

    #Imports history_of_moves
    global history_of_moves
    


    doIPrint( f"AI1's Data =  {data}")
    doIPrint( f"AI1's Move History =  {history_of_moves}")
    if data == "Winner":
        def winnerfunction(number):

            #Assigns, historyList, postion, and theChanceWeMod to whatever findMove returns
            historyList, moveLocation, postion, theChanceWeMod,  = findMove(history_of_moves, number)

            doIPrint( f"theChanceWeMod orginal value: {theChanceWeMod}")

            #Adds theChanceWeMod by values.reward    
            theChanceWeMod = theChanceWeMod + values.reward

            doIPrint( f"thechancewemod new value: {theChanceWeMod}")
            
            #Sets theChanceWeMod to  values.capMax if it went over
            if theChanceWeMod > values.capMax:
                theChanceWeMod = values.capMax

            #Checks if theChanceWeMod is less then values.KILL. If so, sets theChanceWeMod to values.death
            #Only here if the user were to make reward negative
            if theChanceWeMod <= values.KILL:
                theChanceWeMod = values.death
            
            #Checks if theChanceWeMod is is0orneagtive
            theChanceWeMod = is0orneagtive(theChanceWeMod)

            #If theChanceWeMod is above stichUp, values.reward is mutipled by values.stichUpMutipler, and then the pervious move gets effected.
            if theChanceWeMod >= values.stichUp:
                values.reward = values.reward * values.stichUpMutipler
                if (number + 1) != len(historyList):
                    winnerfunction(number + 1)
            
            
            #Updates the chance we wanted to change to theChanceWeMod
            loaded_postions[moveLocation]["Chances"][postion] = theChanceWeMod
        

        #Calls function and starts with the very first move.
        winnerfunction(0)

        #Wipe History.
        history_of_moves = {}
        
        #Save to file
        update_data(loaded_postions)

    if data == "Loser": 
        def loserfunction(number):
            
            #Assigns, historyList, postion, and theChanceWeMod to whatever findMove returns
            historyList, movelocation, postion, theChanceWeMod,  = findMove(history_of_moves, number)

            doIPrint( f"theChanceWeMod orginal value: {theChanceWeMod}")
                
            #Subtracts theChanceWeMod by values.condem    
            theChanceWeMod = theChanceWeMod - values.condem
            
            #Checks if theChanceWeMod is less then values.KILL. If so, sets theChanceWeMod to values.death
            if theChanceWeMod <= values.KILL:
                theChanceWeMod = values.death

            doIPrint( f"thechancewemod new value: {theChanceWeMod}")

            #Checks if theChanceWeMod is is0orneagtive
            theChanceWeMod = is0orneagtive(theChanceWeMod)
            
            #If theChanceWeMod is below or equal to bleedThough, values.condem is mutipled by values.bleedThoughMutipler, and then the pervious move gets effected.
            if theChanceWeMod <= values.bleedThough:
                values.condem = values.condem * values.bleedThoughMutipler
                if (number + 1) != len(historyList):
                    loserfunction(number + 1)
            
            #Updates the chance we wanted to change to theChanceWeMod
            loaded_postions[movelocation]["Chances"][postion] = theChanceWeMod

        #Calls function and starts with the very first move.
        loserfunction(0)
        
        #Wipe History.
        history_of_moves = {}
        
        #Save to file
        update_data(loaded_postions)

    if data == "Draw":
        def drawfunction(number):

            #Assigns, historyList, postion, and theChanceWeMod to whatever findMove returns
            historyList, movelocation, postion, theChanceWeMod,  = findMove(history_of_moves, number)

            doIPrint( f"thechancewemod orginal value: {theChanceWeMod}")
            #More then 100, but it's a draw. Does drawCondem
            if theChanceWeMod > values.drawValue:

                #Subtracts theChanceWeMod by values.drawvalue. Number is asigned to drawNewNumber
                drawNewNumber = theChanceWeMod - values.drawValue 

                #if drawNewNumber is greater then values.drawCondem, then drawNewNumber if forced to become values.drawCondem
                if drawNewNumber > values.drawCondem:
                    drawNewNumber = values.drawCondem

                #Subtracts theChanceWeMod by drawNewNumber   
                theChanceWeMod = theChanceWeMod - drawNewNumber
            
            #Less then 0.1, but it's a draw. Does reward.
            elif theChanceWeMod < values.drawValue:

                #Subtracts theChanceWeMod by values.drawvalue. Number is asigned to drawNewNumber
                drawNewNumber = values.drawValue - theChanceWeMod
                
                #if drawNewNumber is greater then values.drawReward, then drawNewNumber if forced to become values.drawReward
                if drawNewNumber > values.drawReward:
                    drawNewNumber = values.drawReward

                #Adds theChanceWeMod by drawNewNumber   
                theChanceWeMod = theChanceWeMod + drawNewNumber

            doIPrint( f"thechancewemod new value: {theChanceWeMod}")
            
            #Checks if theChanceWeMod is is0orneagtive
            theChanceWeMod = is0orneagtive(theChanceWeMod)

            #If theChanceWeMod is  equal to drawValue, values.drawCondem is mutipled by values.drawBleedThoughMutipler,
            #values.drawReward is mutipled by and values.drawStichUpMutipler, and then the pervious move gets effected.
            if theChanceWeMod == values.drawValue:

                values.drawReward = values.drawReward * values.drawStichUpMutipler

                values.drawCondem = values.drawCondem * values.drawBleedThough
                
                if (number + 1) != len(historyList):
                    drawfunction(number + 1)
            

            
            #Updates the chance we wanted to change to theChanceWeMod
            loaded_postions[movelocation]["Chances"][postion] = theChanceWeMod

        #Calls function and starts with the very first move.
        drawfunction(0)

        #Wipe History.
        history_of_moves = {}

        #Save to file
        update_data(loaded_postions)

    #If the user reseted the board.
    if data == "Reset": 
        history_of_moves = {}

    #The program is shutting down, save the information 1 last time.
    if data == "Quiting":
        update_data(loaded_postions)

    #Resets all the values back to their original values
    values.reset()

#This function updates the data
def update_data(New_data):

    #checks if for some reason the user doesn't want the AI to save anything.
    if values.saveToFile:
        f = open(f"{values.fileName}.py", "w")
        f.write(f"data_loaded_postions = {str(New_data)}")
        f.close()

    #checks if the user wants backup files.
    if values.saveToBackUpFile:

        #Picks a random number though 1 - values.backUpChance. If the random number equals  values.backUpChance, then save a backup file
        if random.randint(1, (values.backUpChance) ) == values.backUpChance:
            f = open(f"{values.backUpFileName}", "w")
            f.write(f"data_loaded_postions = {str(New_data)}")
            f.close()

def debug_menu():
    #Imports loaded_postions
    global loaded_postions

    print("DEBUG MENU")
    print("----------")
    while True:
        print("\n[1] View AI's loaded postions. [2] Modify the postions. [3] Exit [0] Reset the AI's loaded postions. ")
        userinputfordebugmenu = input("Selection: ")

        #View AI's loaded postions
        if userinputfordebugmenu == "1":
            print("Loading loaded_postions...")
            print(loaded_postions)
            print("Done.")

        #Modify the postions.
        elif userinputfordebugmenu == "2":
            ''

        #Exit
        elif userinputfordebugmenu == "3":
            print("Exiting...")
            print("Done.")
            break 
        
        #Reset the AI's loaded postions
        elif userinputfordebugmenu == "0":
            print("\n\n\nARE YOU SURE WANT TO RESET loaded_postions")
            print("This will completely wipe the AI's mermory and force it to start fresh!")
            
            userinputdeleteloadedpostions = input("Y/N: ")
            if userinputdeleteloadedpostions == "Y":
                print("Reseting AI's loaded pistions...")

                #Sets loaded_postions to nothing and then updates the file. Effectly wiping all of the data
                loaded_postions = {}
                update_data(loaded_postions)

                print("Done.")

        #COD4 MW reference.
        elif userinputfordebugmenu.lower() == "soap":
            print("Right...what the hell kind of name is \"Soap\", eh? How'd a muppet like you pass selection?")
                

#This calls the debug_menu function. If you open the AI directly 
if __name__ == "__main__":
    debug_menu()