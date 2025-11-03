'''
    Based on Arnold Yim's TicTacToe.ipynb
    Build: TicTacToe_2PYAIBattles_build
    Change log:
    *Added more comments to explain what the AI is doing.
    *Added the ability to choose player vs player, player vs AI, AI vs AI
    *Added the TIC TAC TOE main screen.
    *My Head now hurts.
'''

#Imports numpy. But we can just refer to it as np
import numpy as np
#Imports importlib
import importlib

#listOfCurrentAIPlayer
from listOfCurrentAIPlayer import AIS

#Imports AI.
Player1 = importlib.import_module(AIS["Player1"])
Player2 = importlib.import_module(AIS["Player2"])


class TicTacToe:
    #When the class is first created, it creates the board using the reset function within the class.
    #Originally __init__ and reset did the same thing 
    def __init__(self):
        self.reset("Reset")

    def available_actions(self):
        actions = []
        #For each row, check each column to see if it's an emtpy spot. If yes, append actions list to include the move. 
        for x in range(3):
            for y in range(3):
                if self.board[x,y] == 0:
                    actions.append((x,y))
        return actions
    
    #Stole this form https://pythonguides.com/remove-the-first-and-last-character-from-a-string-in-python/    
    #Removes the first and last charater form the string inserted. This results in a removing the additonal [] that print(self.board) has. Making it look a little clearer.
    def return_current_board_for_print(self):
        #I have to keep converting the board to string.
        string_length = len(str(self.board))
        outputString = str(self.board)[1:string_length-1]
        return outputString

    #action is the location the player wants to mark.
    def make_move(self, action):

        #Checks if the spot is empty. otherwise it prints 0 "invalid action, try again"
        if self.board[action] == 0:
            #Set the location the player/ai wanted as marked for them.
            self.board[action] = self.current_player
            print(self.return_current_board_for_print())
            
            #Checks if the last player who moved has a complete line.
            if self.check_winner():

                #The last player who moved, wins!
                print(self.board)
                print(f'\nteam {self.current_player} wins!')


                print('Resetting board')
                #Returns winner. For the AI to read
                return self.reset("Winner")


            #Checks if there's no more moves to make.
            elif len(self.available_actions())==0:
                print('no more available moves, the game is a draw')
                print('Resetting board')
                #Returns Draw. For the AI to read
                return self.reset("Draw")

            #If none of the other statements apply. That must mean the game is still going. 
            else:
                '''
                % is remainer. 
                If self.curretplayer is 1: (1 % 2) = 1. Then it gets added by 1, equaling 2.
                If self.curretplayer is 2: (2 % 2) = 0 [because there's no remainer]. Then it gets added by 1, equaling 1. 
                If we ever wanted to add more 2 players, we would increase '2' int to any number we want.
                '''
                
                self.current_player = self.current_player%2+1
            
            #returns True, as in a turn was successfully executed. Mainly here for the user player.
            return True

        else:
            #returns False, as in a turn was not executed. Mainly here for the user player.
            print('invalid action, try again')
            return False



    def check_winner(self):

        #A list of every possible win condition.
        win_conditions = [((0,0),(0,1),(0,2)),
                          ((1,0),(1,1),(1,2)),
                          ((2,0),(2,1),(2,2)),
                          ((0,0),(1,0),(2,0)),
                          ((0,1),(1,1),(2,1)),
                          ((0,2),(1,2),(2,2)),
                          ((0,0),(1,1),(2,2)),
                          ((0,2),(1,1),(2,0))]
        

        for a, b, c in win_conditions:
            #Each letter corresponds with a location on the board form the win_condition list. [So the first win condition in the list would mean that a = (0,0), b = (0,1), c = (0,2)]
            #If ALL letters == self.current_player [the current player's marked locations], that means the player has a line and wins. 
            #[So if the current_player is 1. If a(0,0) = 1, b(0,1) = 1, and c(0,2) = 1. player 1 wins.]

            if self.board[a] == self.board[b] == self.board[c] == self.current_player:
                return True
        
        return False

    #Reset creates a new board 3 by 3 board and sets the curret player to 1
    def reset(self, reason):
        self.board = np.zeros((3,3))
        self.current_player = 1
        print(self.return_current_board_for_print())
        print("REASON FOR RESET:", reason)
        return reason

#TicTacToe Class ends here.


#This allows us to call the TicTacToe class with the game variable.
game = TicTacToe()


#Function that handles player's turn.
def human_player_turn():
        print(f"\nIt's the {game.current_player}'s turn to place something down!")
        print("[1] make a move. [2] reset the board. [CTRL + C] return to main menu")
        
        #Get user input
        user_input = input("")
            #Make a move
        if user_input == "1":
            while True:

                #Get user input, but this time to find where the player wants to mark
                print(f"\n{game.available_actions()}")
                user_input_action = input('Make your move. Your move should look like this "0 1": ')

                #Convert user action to tuple

                #First, we need to split the user's 2 numbers apart and store them into a list
                list_of_strings_to_be_converted_into_ints = user_input_action.split()

                #Create an empty list to be filled up with ints
                list_of_ints = []

                #for loop that converts all the strings in the list to be an int
                for x in list_of_strings_to_be_converted_into_ints:
                    list_of_ints.append(int(x))
                    
                #Now we can convert our list to a turple
                    
                user_action = tuple(list_of_ints)
                    
                #If this returns True, then that means the user made a move.
                result = game.make_move(user_action)
                if result:
                    return result
                
                #The player's turn is OVER.
            
        #Reset the board because the user is a little baby and doesn't want to lose.
        elif user_input == "2":
            print("Restarting game...")
            game.reset("Reset")

#Function that handles standard AI turn.
def AI_turn(AI):
    #Calls the the current AI's turn. Returns the move the AI choose
    return AI.main(game.return_current_board_for_print(), game.available_actions())
    


#Main function. Starts the program
def main():
    global Player1
    global Player2
    #Tic Tac Toe
    print('''  \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
      ----- O      -----               -----       
        |       |    |           |       |         __
        |   |  |     |    |||   |        |   |||  |__|
        |   |  |     |   |  |   |        |   | |  |
        |   |   |    |    |||    |       |   |||   ---
    ''') 

    current_turn = 1
    print("[0] Human vs Human [1] Human vs AI [2] AI vs AI [3] Settings [CTRL + C] quit")
    try:
        gamemode = input("What gamemode would you like to choose: ")
    except KeyboardInterrupt: 
        print("\nGood bye!")
        quit()

    if gamemode == "0":
        #Human vs Human
        while True:
            try:
                human_player_turn()
                #Refer to line 59 if you have any questions about this line
                current_turn = current_turn % 2 + 1
            
            #KeyboardInterrupt means the user pressed CTRL + C and wants to quit the program.
            except KeyboardInterrupt:
                print("\nQuiting...")
                print("Done... (Press enter to go back to title screen)")
                input()
                main()
                break
                

            #KeyboardInterrupt means the user input something invaild
            except ValueError:
                print("Invaild input!")

            #KeyboardInterrupt means the user input something out of bounds
            except IndexError:
                print("Invaild input!")


            except Exception as e:
                #Prints what went wrong.
                print("Something went wrong")
                print(type(e))
                print(e)
    elif gamemode == "1":
        try: 
            print("Which AI do you want to play against? [1 or anything else other then 2] Player 1 [2] Player 2 [ctrl + c] Go back to main menu")
            userInputForAIPlayer = input()
            if userInputForAIPlayer == "2":
                current_player = Player2 
            else:
                current_player = Player1

        except KeyboardInterrupt:
            print("\nQuiting...")
            print("Done... (Press enter to go back to title screen)")
            input()
            main()

        #human vs AI


        while True:
            if current_turn == 1:
                #Player Turn.
                try:
                    print(f"player move as the {current_turn}'s")
                    result = human_player_turn()
                    if result == "Winner":
                        Player1.TicTacToe_communation("Loser")
                    current_turn = current_turn % 2 + 1
                    
                #KeyboardInterrupt means the user pressed CTRL + C and wants to quit the program.
                except KeyboardInterrupt:
                    print("Saving and quiting...")
                    #Tells the AI to save.
                    Player1.TicTacToe_communation("Quiting")
                    print("Done... (Press enter to go back to title screen)")
                    input()
                    main()
                    break

                    #ValueError means the user input something invaild
                except ValueError:
                    print("Invaild input!")

                #IndexError means the user input something out of bounds
                except IndexError:
                    print("Invaild input!")


                except Exception as e:
                    #Prints what went wrong.
                    print("Something went wrong")
                    print(type(e))
                    print(e)
            else:
                #AI turn
                print(f"AI player move as the {current_turn}'s:")


                result = game.make_move(AI_turn(current_player))
                if result:
                    current_player.TicTacToe_communation(result)
                current_turn = current_turn % 2 + 1

    elif gamemode == "2":
        #AI vs AI
        player1Wins = 0
        player2Wins = 0 
        ties = 0
        while True:
            try: 
                #Player 1 turn
                if current_turn == 1:
                    print(f"AI player 1 move as the {current_turn}'s:")
                    result = game.make_move(AI_turn(Player1))
                    if result:

                        if result == "Winner":
                            #If player 1 wins, tell player 2 that they lost
                            Player1.TicTacToe_communation(result)
                            Player2.TicTacToe_communation("Loser")
                            player1Wins = player1Wins + 1

                        else:
                            #It's a draw!
                            Player1.TicTacToe_communation(result)
                            Player2.TicTacToe_communation(result)
                            ties = ties + 1

                    current_turn = current_turn % 2 + 1
                
                #Player 2 turn
                else:
                    print(f"AI player 2 move as the {current_turn}'s:")
                    result = game.make_move(AI_turn(Player2))
                    if result:

                        if result == "Winner":
                            #If player 2 wins, tell player 1 that they lost
                            Player2.TicTacToe_communation(result)
                            Player1.TicTacToe_communation("Loser")
                            player2Wins = player2Wins + 1

                        else:
                            #It's a draw!
                            Player2.TicTacToe_communation(result)
                            Player1.TicTacToe_communation(result)
                            ties = ties + 1

                    current_turn = current_turn % 2 + 1
            
            #This means the user is quiting.
            except KeyboardInterrupt:
                print("\nSaving and Quiting...")

                #Tells both AIs to save before exiting.
                Player1.TicTacToe_communation("Quiting")
                Player2.TicTacToe_communation("Quiting")

                print("Player1 Won this many times:", player1Wins)
                print("Player1 Won this many times:", player2Wins)
                print("This is how many draws happened:", ties)
                print("Done... (Press enter to go back to title screen)")
 
                input()
 
                main()
 
                break
    elif gamemode == "3": 
        print("----")
        print("SETTINGS")
        while True: 
            try: 
                print("[1] Swtich player 1 with a different AI. [2] Swtich player 2 with a different AI. [3] Display who the current AIs are playing [4] Save current players [CTRL + C] return to main menu")
                userinput = input("Input: ")

                #Swtich player 1
                if userinput == "1":
                    print("What AI model do you want to replace player 1? (Type file name but leave the file extension)")
                    userFile = input("")

                    #Asigns Player1 to a new AI
                    Player1 = importlib.import_module(userFile)
                    print(Player1)
                
                #Swtich player 2
                elif userinput == "2":
                    print("What AI model do you want to replace player 2? (Type file name but leave the file extension)")
                    userFile = input("")

                    #Asigns Player2 to a new AI
                    Player2 = importlib.import_module(userFile)
                    print(Player2)
                
                #Display current players
                elif userinput == "3":
                    print(f"\nPlayer1: {Player1}")
                    print(f"Player2: {Player2}")

                    print(f"Player1 file name: {Player1.__name__}")
                    print(f"Player2 file name: {Player2.__name__}\n")
                
                #Save current players
                elif userinput == "4":
                    print("Saving...")

                    #Saves the currently playing AIs to be choosen again later
                    AIPlayers = 'AIS = {"Player1" : "' + Player1.__name__ + '", "Player2" : "' + Player2.__name__ + '"}'
                    print(AIPlayers)

                    f = open("listOfCurrentAIPlayer.py", "w")
                    f.write(AIPlayers)
                    f.close()

                    print("Done!")
            
            #Exit back to title screen
            except KeyboardInterrupt:
                main()
                break

            except Exception as e:
                #Prints what went wrong.
                print("Something went wrong")
                print(type(e))
                print(e) 
    else: 
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        main()


#This calls the main function. It's in a if statement just incase you import this python file, but don't want it run yet. 
if __name__ == "__main__":
    main()