#Implementation

#Importing python modules
import random
import csv
import time
import os

#Selecting functions from the tkinter module for future use
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

#Declaring the function to set which language to run the program in
def language_select():

    #Language options array
    language_array = ["","English","Gaelic","Spanish","French"]
    language = 5
    confirmed = False

    #Loop until valid input
    while confirmed == False:

        #Input validation to ensure that language selection is valid
        if language <1 or language >4:
            #Printing language selections
            print("\n")
            print("1.English")
            print("2.Gaelic")
            print("3.Spanish")
            print("4.French")
            print("\n")
            #Getting a new input
            language = int(input("Please select a language using the above numbers: "))

        #Else loop to double check users input 
        else:

            #Setting the original input to a new variable to compare after the user enters the selected language again
            check = language
            print("")
            print("You have selected",language_array[language]+", please confirm this selection")
            language = int(input("Please re-enter the number of your chosen language: "))

            #If condition for restarting the loop if the user does not enter the same input twice
            if language != check:
                language = 5
                confirmed = False
                #Printing new lines to keep SHELL clear
                print("\n" * 50)

            #Else to confirm the selection 
            else:

                confirmed = True
                #Language -=1 to match the selection with the correct index in the language bank arrays
                language -= 1
                #passing back the language variable for use in other functions
                return language



#Creating a function to get player names assuming that a game is not being imported
def player_names(language):

    print("\n")

    #Language Bank#
    bank_enter_names = ["Please enter the name of player", "cuir a-steach ainm an cluicheadair", "Por favor ingrese el nombre del jugador", "Entrez le nom du joueur"]
    bank_welcome = ["Welcome", "Fàilte", "Bienvenido", "Bienvenue"]
    bank_and = ["and", "agus", "y", "et"]
    ###############

    #Prompting users for names
    p1 = input(bank_enter_names[language]+" 1: ")
    p2 = input(bank_enter_names[language]+" 2: ")

    print("")
    #Printing welcome message
    print(bank_welcome[language],p1,bank_and[language],p2)
    #Time delay to allow users time to read the message
    time.sleep(2)
    print('\n' * 100)

    #Setting vital main program loop conditions to the start value
    p1_win = False
    p2_win = False
    pause_req = False

    #returning appropriate local variable for use in other functions
    return p1, p2, p1_win, p2_win, pause_req
    



def import_game(language):

    #Language Bank#
    bank_import = ["Import", "Import", "Importar", "Importer"]
    bank_newGame = ["Import new game query", "-mhalairt geama ùr ceiste", "Importar nueva consulta de juego", "Importer une nouvelle requête de jeu"]
    bank_selection = ["Enter selection", "Cuir a-steach taghadh", "Introducir selección", "Entrer la sélection"]
    bank_options = ["1 = yes, 2 = no", "1 = seadh, 2 = sam bith", "1 = sí, 2 = no", "1 = oui, 2 = non"]
    bank_enterName = ["Player", "Cluicheadair", "Jugador", "Joueur"]
    bank_enterName2 = ["Please enter the name of the original player", "Cuir a-steach an t-ainm tùsail cluicheadair", "Introduzca el nombre del reproductor original", "Veuillez entrer le nom du joueur original"]
    ###############

    #Setting initial value for importing a new game query
    query = False

    #Creating empty array to avoid errors with calling empty variables
    board = []
    stack = []
    stack.append(0)

    #Setting up tkinter window to allow the use of simpledialog and messagebox
    root = Tk()
    w = Label(root, text="Import game")
    w.pack()
    
    Uinput = 0

    #Creating a loop to continue to prompt the user for valid input
    while Uinput <1 or Uinput >2:

        #Sending a message box to tell the user what the query is asking
        tkinter.messagebox.showinfo(bank_import[language],bank_newGame[language])
        #Askinteger box to receive input to only allow integers to be input, removing the risk of the user entering a string and the program crashing
        Uinput = tkinter.simpledialog.askinteger(bank_selection[language], bank_options[language])

    if Uinput == 2:
        #Should the user not want to inport a game, initial game variables are set to 0
        query = False
        stack = [0,0,0,0,0,0,0,0]
        p1 = ""
        p2 = ""

    else:
        #The user will have selected that they do want to import a game
        #Using tkinter simpledialog boxes to receive the original player names
        p1 = tkinter.simpledialog.askstring(bank_enterName[language]+" 1", bank_enterName2[language]+" 1: ")
        p2 = tkinter.simpledialog.askstring(bank_enterName[language]+" 2", bank_enterName2[language]+" 2: ")
        #Finding the file by calculating the filename using players names
        filename = str(p1+" & "+p2+"'s game.txt")
        #Since the file contains unicode codes for characters, the file must be decoded using 'utf-8'
        file = open(filename,encoding='utf8')
        boardString = ""
        stackString = ""

        #Extracting the data from the file
        for line in file:
            boardString += str(line)

        #Closing the file
        file.close()
        #Removing the game file 
        os.remove(filename)

        #Currently the data is stored as a sting
        #Sting conditioning must be executed for simple conversion to an array
        temp = boardString.replace(",","")
        temp2 = temp.replace("'","")
        temp3 = temp2.replace("[[[",".[")
        temp4 = temp3.replace("]]]","]")
        temp5 = temp4.replace("]]","]")
        temp6 = temp5.replace("[[","[")
        temp7 = temp6.replace("] [","][")

        #Creating empty arrays to be filled with data from the file
        array = []
        stackArray = []

        new = ""

        #Range (1,215) since the full file contains both the game board and current stack data
        for i in range(1,215):
            new += temp7[i]

            #Each game slot is 5 characters long hence using modulus of 5 to detect when one full game slot has been created
            if i %5 == 0:
                #Adding the game slot to the new array
               array.append(new)
               new = ""
        
        counter = 0

        #Converting the 1D array to a 2D array to allow correct formatting etc when passed through to the main program loop
        #Loop inside a loop to create 6 rows with 7 slots in each row
        for row in range(0,6):

            #Setting the temporary row array to be empty after every loop 
            arrayRow = []

            for collum in range(0,7):

                #Condition placed to circumvent an occuring problem with the loop running too many times and returning an error
                if counter <42:
                    arrayRow.append(array[counter])
            
                counter += 1

            board.append(arrayRow)

        #Loop created to extract the stack data from the mega string
        for y in range(215,len(temp7)):

            #Using string concatenation to create a string containing only the stack data
            stackString += temp7[y]

        #String conditioning to remove all data which is not an number value
        temp8 = stackString.replace(" ", "")
        temp9 = temp8.replace("-", "")
        
        #Converting the stack string to a stack array
        for v in range(0,len(temp9)):
            stackArray.append(temp9[v])

        #Since stack system goes down into negative numbers all integers must either be 0 or negative
        #A loop had to be created to multiply each piece of data in the array by -1
        for t in range(0,len(temp9)-1):
            temP = int(stackArray[t])

            temP = temP * -1
            stack.append(temP)


        #If a new game has been imported the query boolean is set to true to trigger other functions such as firstMove
        query = True

    #Returning boolean variables that are used as conditions in the main program loop
    p1_win = False
    p2_win = False
    pause_req = False
            

    #Returning local variables for use in other functions
    return query,board,stack,p1,p2,p1_win,p2_win,pause_req


#Creating a function to process a users pause game request
def pause_game(board, stack):                  

    #Generating a file name using the player names
    filename = str(p1+" & "+p2+"'s game.txt")
    file = open(filename, "wb")
    #Writing to the file using the unicode encoder to handle unicode characters
    file.write(str(board).encode('utf8'))
    file.write("\n".encode('utf8'))
    file.write(str(stack).encode('utf8'))
    #Closing the file
    file.close()
    print('\n')
    #Printing a confirmation message
    print('Game export succesfull')
    time.sleep(0.3)
    print('File name : '+filename)
    print('\n')
    
    


def help_query(language):

    tutorial = True

    
    #Language Bank#
    query_bank = ["Do you require a tutorial to explain how to play?: ",
                  "A bheil sibh a 'cur feum air tutorial mìneachadh ciamar a bhios a' cluich?: ",
                  "¿Necesita un tutorial para explicar cómo jugar?: ",
                  "Avez-vous besoin d'un tutoriel pour expliquer comment jouer?: "]

    input_bank = ["(Please use '1' for Yes and '2' for No)",
                  "(Cleachdaibh am '1' Bu Chòir agus '2' airson Cha Bu Chòir)",
                  "(Por favor, utilice '1' para Sí y '2' para No)",
                  "(Veuillez utiliser '1' pour Oui et '2' pour Non)"]
    
    bank_options = ["1 = yes, 2 = no",
                    "1 = seadh, 2 = sam bith",
                    "1 = sí, 2 = no",
                    "1 = oui, 2 = non"]

    bank_again = ["Replay the tutorial?",
                  "Ath-chluich air an oideachadh?",
                  "¿Reproducir el tutorial?",
                  "Rejouer le didacticiel?"]
    
    bank_1 = ["Welcome to Connect 4",
              "Fàilte gu Connect 4",
              "Bienvenido a Connect 4",
              "Bienvenue à Connect 4"]

    bank_2 = ["The aim of the game is to connect 4 of your counters in a straight line",
              "Tha an amas a 'gheama a tha a' ceangal 4 ur cunntairean ann an loidhne dhìreach",
              "El objetivo del juego es conectar 4 de sus contadores en línea recta",
              "Le but du jeu est de connecter 4 de vos compteurs en ligne droite"]

    bank_3 = ["You must also ensure that you stop your opponent from winning by blocking their lines",
              "Feumaidh tu dèanamh cinnteach cuideachd gu bheil thu a 'stad an neachdùbhlain agaibh bho bhuannaich le bacadh aca lines",
              "También debe asegurarse de que evite que su oponente gane bloqueando sus líneas",
              "Vous devez également vous assurer que vous arrêtez votre adversaire de gagner en bloquant leurs lignes"]
              
    bank_vert = ["You can win by creating vertical lines:",
                 "Faodaidh tu dìreach a bhuannachadh le bhith a 'cruthachadh sreathan:",
                 "Puedes ganar creando líneas verticales:",
                 "Vous pouvez gagner en créant des lignes verticales:"]

    bank_horz = ["Horizontal lines:",
                 "Loidhne chòmhnard:",
                 "Lineas horizontales:",
                 "Lignes horizontales:"]

    bank_diag = ["Diagonal lines:",
                 "Loidhne trastain:",
                 "Líneas diagonales:",
                 "Lignes diagonales:"]

    bank_pause = ["You can pause the game at any time during the game by entering '100'",
                  "Faodaidh tu stad a 'gheama aig àm sam bith rè a' gheama le bhith a 'tighinn a-steach' 100 '",
                  "Puedes pausar el juego en cualquier momento durante el juego ingresando '100'",
                  "Vous pouvez interrompre le jeu à tout moment pendant le jeu en entrant '100'"]

    bank_load = ["You may load in this game to continue playing after the program has been restarted",
                 "Faodaidh tu load sa gheama seo leantainn a 'cluich an dèidh a' phrògram air a bhith air ath-thòiseachadh",
                 "Puede cargar en este juego para continuar jugando después de reiniciar el programa",
                 "Vous pouvez charger dans ce jeu pour continuer à jouer après le redémarrage du programme"]
    ###########################

    
    #Printing the option to trigger the tutorial query
    print(input_bank[language])
    reply = int(input(query_bank[language]))

    print('\n')

    #Conditional loop to validate input
    while reply != 1 and reply != 2:
        print(input_bank[language])
        reply = int(input(query_bank[language]))
        print('\n')

    if reply == 2:
        tutorial = False

    #Runs if the user selected that they wanted to run the tutorial b
    while tutorial == True:

        #Printing the game instructions with various time delays for readability
        print(bank_1[language])
        for i in range(0,6):                
            print("----------",end='')
            time.sleep(0.05)
        print('\n')
        time.sleep(3)
        print(bank_2[language])
        time.sleep(3)
        print('\n')
        print(bank_3[language])
        time.sleep(3)
        print('\n')
        print(bank_vert[language])
        time.sleep(3)
        print('\n')

        #Loop to create an example horizontal win
        for i in range(0,4):
            print("[ ◌ ]",end='')
            time.sleep(0.05)
        print('\n'*2)
        
        time.sleep(3)
        
        print(bank_horz[language])
        print('\n')

        #Loop to create an example vertical win
        for i in range(0,4):
            print("          [ ◌ ]")
            time.sleep(0.05)
        print('\n')
        time.sleep(3)
        x = " "
        print(bank_diag[language])
        print('\n')

        #Loop to create an example diagonal win
        for i in range(4,8):
            print(str(x)+"[ ◌ ]")
            time.sleep(0.05)
            x+= "     "
        time.sleep(3)

        #Informing the user of the pause and load function
        print('\n')
        print(bank_pause[language])
        print('\n')
        time.sleep(3)
        print(bank_load[language])
        time.sleep(3)

        #Setting an unacceptable input to initiate the loop
        reply = 3

        #Input validation to receive instructions to either replay the tutorial or move on
        while reply != 1 and reply != 2:

            reply  = tkinter.simpledialog.askinteger(bank_options[language], bank_again[language])
            
        if reply == 2:
            tutorial = False

        else:
            tutorial = True

        print('\n'*50)
            

#Creating a function to determine which player should go first if a game save has been imported
def firstMove(board):

    #The method is to count the number of player 1 and player 2 counters in the board
    count1 = 0
    count2 = 0

    #Loop within a loop to check all 42 spaces in the board
    for row in range(0,6):

        for collum in range(0,7):

            #Adding +1 on to the player 1 counter if a piece is found
            if board[row][collum] == "[ ⁕ ]":
                count1 += 1

            #Adding +1 on to the player 2 counter if a piece is found
            elif board[row][collum] == "[ ◌ ]":
                count2 += 1

    #Setting a boolean value to be passed to the main program loop
    #Where False = Player 1 goes first and True = Player 2 goes first
    whoFirst = False

    #Comparing the sum of each counter variable
    #If 1 = 2 then player 1 must take the next move
    if count1 == count2:
         whoFirst = False

    #Else player 2 has less counters hence must make the next move
    else:
        whoFirst = True
    movesMade = count1 + count2
    return whoFirst, movesMade

#Creating a function to create a new game board should the user decide not to import a new game           
def create_array():

    #Creating an empty array for appending
    board=[]

    #Loop inside a loop to create rows and collums
    for repeat in range(0,6):
        single_row = []

        #Creating each row individually by adding 7 slots to a temporary array
        for collum in range(0,7):
            single_row.append("[   ]")
        #Adding each row the the main board
        board.append(single_row)

    movesMade = 0
    #Returning the local variable board for use in other functions
    return board, movesMade



#Creating a function to format the game board in such a way that is readable by the user
def format_array(board):

    #Printing a 'guide' to easily show the user which collum is which
    print("[ 1 ][ 2 ][ 3 ][ 4 ][ 5 ][ 6 ][ 7 ]")

    #Loop inside a loop to print all slots in the board in grid form
    for row in range(0,6):

        for collum in range(0,7):
            #Printing each row at a time using ,end='' to print on the same line
            print(board[row][collum],end='')
        
        print(" ")

    print(" ")



#Creating a function to process player 1's turn and validating the input
def player1(language, p1, board, stack, pause_req, movesMade):

    #Language Bank#
    bank_invalid = ["Invalid selection!", "Taghadh mì-dhligheach!", "Selección invalida!", "Sélection non valide!"]
    bank_rule = ["Select a collum ranging from 1 to 7", "Tagh collum bho 1 gu 7", "Seleccione un collum de 1 a 7", "Sélectionnez un collum allant de 1 à 7"]
    bank_full = ["Stack full", "Cruachadh làn", "Pila llena", "Pile pleine"]
    ###############

    #Assuming the input is false to initiate the while loop
    valid = False

    #Loop until a valid input is accepted
    while valid == False:
        turn = int(input(p1+": "))

        #If condition to trigger the pause game function
        if turn == 100:
            valid = True
            pause_req = True
            #Calling the pause game function internally
            pause_game(board,stack)

        #Assuming the player does not want to pause:
        else:

            #First validation deals with receiving an input which is between 1 and 7
            while turn <1 or turn >7 and turn != 100:
                print(bank_invalid[language])
                #Continues to ask for an input until its within the range
                turn = int(input(bank_rule[language]+": "))
                print('\n')
            #If condition to check is the stack in the selected is full 
            if stack[turn] == -6:
                print(bank_full[language])

            #This else will only pass if the input is between 1-7 and the selected collum is not full
            else:
                #Valid is set to true to exit the loop
                valid = True
                #Stack array is updated to support the newest move
                stack[turn] -= 1
                #A player counter is added to the appropriate slot
                board[stack[turn]][turn-1] = "[ ⁕ ]"
                movesMade += 1
    print('\n'*50)
    #Returns the local variables to be used in other functions
    return pause_req, stack, movesMade
                                     

    
                                
def player2(language, p2, board, stack, pause_req, movesMade):

    #Language Bank#
    bank_invalid = ["Invalid selection!", "Taghadh mì-dhligheach!", "Selección invalida!", "Sélection non valide!"]
    bank_rule = ["Select a collum ranging from 1 to 7", "Tagh collum bho 1 gu 7", "Seleccione un collum de 1 a 7", "Sélectionnez un collum allant de 1 à 7"]
    bank_full = ["Stack full", "Cruachadh làn", "Pila llena", "Pile pleine"]   
    ###############

    #Assuming the input is false to initiate the while loop
    valid = False

    #Loop until a valid input is accepted
    while valid == False:
        turn = int(input(p2+": "))

        #If condition to trigger the pause game function
        if turn == 100:
            valid = True
            pause_req = True
            #Calling the pause game function internally
            pause_game(board,stack)

        #Assuming the player does not want to pause:
        else:

            #First validation deals with receiving an input which is between 1 and 7
            while turn <1 or turn >7 and turn != 100:
                print(bank_invalid[language])
                #Continues to ask for an input until its within the range
                turn = int(input(bank_rule[language]+": "))

            #If condition to check is the stack in the selected is full
            if stack[turn] == -6:
                print("Stack full")

            #This else will only pass if the input is between 1-7 and the selected collum is not full
            else:
                #Valid is set to true to exit the loop
                valid = True
                #Stack array is updated to support the newest move
                stack[turn] -= 1
                #A player counter is added to the appropriate slot
                board[stack[turn]][turn-1] = "[ ◌ ]"
                movesMade += 1
    print('\n'*50)
    #Returns the local variables to be used in other functions
    return pause_req, stack, movesMade

            

#Creating a function to search for horizontal wins
def horizontal_search(board, p1_win, p2_win, p1, p2):

    #Language Bank#
    bank_win = [" has won the game - Horizontal connect 4", "air a bhuannaicheadh ​​an gèam - Chòmhnard ceangal 4", "ha ganado el juego - Conexión horizontal 4", "a gagné le jeu - Connexion horizontale 4"]
    ###############


    for row in range(0,6):
        #Loops from 0 to 4 since if there hasnt been a match found by the fourth index in a row then its not possible for a win to occur - improving efficiency
        for collum in range(0,4):
            #Setting i to the slot which is being checked for a connect 4
            i = board[row][collum]

            #Condition testing if the counter is the same as the next 3 in the row
            if i == board[row][collum+1] and i == board[row][collum+2] and i == board[row][collum+3]:

                #If the condition is passed and i = "[ ⁕ ]" player 1 has won
                if i == "[ ⁕ ]":
                    p1_win = True

                    if language == 1:
                        print("Tha "+p1+" "+bank_win[language])

                    else:
                        print(p1+" "+bank_win[language])

                #If the condition is passed and i = "[ ◌ ]" player 2 has won
                elif i == "[ ◌ ]":
                    p2_win = True

                    if language == 1:
                        print("Tha "+p2+" "+bank_win[language])

                    else:
                        print(p2+" "+bank_win[language])

    #Returns the local variables for use in other functions
    return p1_win, p2_win



#Ceating a function to search for vertical wins
def vertical_search(board, p1_win, p2_win, p1, p2):

    #Language Bank#
    bank_win = [" has won the game - Vertical connect 4", "air a bhuannaicheadh ​​an gèam - ceangal dìreach 4", "ha ganado el juego - Conexión vertical 4", "a gagné le jeu - Connexion verticale 4"] 
    ###############

    #Creating a loop to test every slot on the board
    for row in range(3,6):

        for collum in range(0,7):
            #Setting i to the slot being tested
            i = board[row][collum]

            #Condition to test if i is equal to the next 3 slots below it
            if i == board[row-1][collum] and i == board[row-2][collum] and i == board[row-3][collum]:
                
                #If the condition is passed and i = "[ ⁕ ]" player 1 has won
                if i == "[ ⁕ ]":
                    p1_win = True
                    print(str(row))
                    print(str(collum))
                    if language == 1:
                        print("Tha "+p1+" "+bank_win[language])

                    else:
                        print(p1+" "+bank_win[language])

                #If the condition is passed and i = "[ ◌ ]" player 2 has won
                elif i == "[ ◌ ]":
                    p2_win = True

                    if language == 1:
                        print("Tha "+p2+" "+bank_win[language])

                    else:
                        print(p2+" "+bank_win[language])

    #Returns the local variables for use in other functions
    return p1_win, p2_win


#Creates a function to search for diagonal wins from left to right
def diagonalLR_search(board, p1_win, p2_win, p1, p2):

    #Language Bank#
    bank_win = [" has won the game - Diagonal connect 4", "air a bhuannaicheadh ​​an gèam - Trastain ceangal 4", "ha ganado el juego - Conexión diagonal 4", "a gagné le jeu - Connexion diagonale 4"]    
    ###############

    #Arrays are created to search the correct diagonal lines in the game board
    repetitions = [1,2,3,3,2,1]
    xstartPTS = [2,1,0,0,0,0]
    ystartPTS = [0,0,0,1,2,3]

    
    for i in range(0,6):
        point = board[xstartPTS[i]][ystartPTS[i]]

        #Loop from 0 to however many times there can be a diagonal connect 4 in that line
        #This number was pre calculated
        for r in range(repetitions[i]):
            #Setting the starting point to the location calculated by the xstart and ystart arrays
            point = board[xstartPTS[i]+r][ystartPTS[i]+r]

            #Condition to test if point is equal to the next 3 slots in a diagonal line from left to right, top to bottom
            if point == board[xstartPTS[i]+r+1][ystartPTS[i]+r+1] and point == board[xstartPTS[i]+r+2][ystartPTS[i]+r+2] and point == board[xstartPTS[i]+r+3][ystartPTS[i]+r+3]:

                #If the condition is passed and i = "[ ⁕ ]" player 1 has won
                if point == "[ ⁕ ]":
                    p1_win = True

                    if language == 1:
                        print("Tha "+p1+" "+bank_win[language])

                    else:
                        print(p1+" "+bank_win[language])
    
                #If the condition is passed and i = "[ ◌ ]" player 2 has won
                elif point == "[ ◌ ]":
                    p2_win = True

                    if language == 1:
                        print("Tha "+p2+" "+bank_win[language])

                    else:
                        print(p2+" "+bank_win[language])

    #Returns the local variables for use in other functions
    return p1_win, p2_win


#creates a function to search for diagonal wins from right to left
def diagonalRL_search(board, p1_win, p2_win, p1, p2):

    #Language Bank#
    bank_win = [" has won the game - Diagonal connect 4", "air a bhuannaicheadh ​​an gèam - trastain ceangal 4", "ha ganado el juego - Conexión diagonal 4", "a gagné le jeu - Connexion diagonale 4"]    
    ##############

    #Arrays are created to search the correct diagonal lines in the game board
    repetitions = [1,2,3,3,2,1]
    xstartPTS = [0,0,0,0,1,2]
    ystartPTS = [3,4,5,6,6,6]

    for i in range(0,6):
        point = board[xstartPTS[i]][ystartPTS[i]]

        #Loop from 0 to however many times there can be a diagonal connect 4 in that line
        #This number was pre calculated
        for r in range(repetitions[i]):
            #Setting the starting point to the location calculated by the xstart and ystart arrays
            point = board[xstartPTS[i]+r][ystartPTS[i]-r]

            #Condition to test if point is equal to the next 3 slots in a diagonal line from right to left, bottom to top
            if point == board[xstartPTS[i]+r+1][ystartPTS[i]-r-1] and point == board[xstartPTS[i]+r+2][ystartPTS[i]-r-2] and point == board[xstartPTS[i]+r+3][ystartPTS[i]-r-3]:

                #If the condition is passed and i = "[ ⁕ ]" player 1 has won
                if point == "[ ⁕ ]":
                    p1_win = True

                    if language == 1:
                        print("Tha "+p1+" "+bank_win[language])

                    else:
                        print(p1+" "+bank_win[language])

                #If the condition is passed and i = "[ ◌ ]" player 2 has won
                elif point == "[ ◌ ]":
                    p2_win = True

                    if language == 1:
                        print("Tha "+p2+" "+bank_win[language])

                    else:
                        print(p2+" "+bank_win[language])

    #Returns the local variables for use in other functions
    return p1_win, p2_win


#Creates a function to write player statistics to a file
def WriteStats(board,p1,p2):

    #Setting variables to 0 before counting
    p1_moves = 0
    p2_moves = 0

    #Creating a loop to run for every slot in the board
    for row in range(0,6):

        for collum in range(0,7):

            #If the slot = [ ⁕ ] then add 1 to the player 1 counter
            if board[row][collum] == "[ ⁕ ]":
                p1_moves += 1

            #If the slot = [ ◌ ] then add 1 to the player 2 counter
            if board[row][collum] == "[ ◌ ]":
                p2_moves += 1

    #Since this function only runs after a winner has been found if both players have had equal moves then player 2 must have won
    if p1_moves == p2_moves:
        winner = 2

    #Else player 1 has won
    else:
        winner = 1

    #Identifying the csv file to be opened
    filename = "PlayerStats.csv"
    #Opening the file using the read operation
    file = open(filename,"r")
    #Using a reader object to extract data since the file is in csv format
    readerWS = csv.reader(file)

    #Creating empty arrays to be filled with data from the file
    names = []
    games = []
    wins = []
    loses = []
    totalmoves = []
    shortestwin = []
    numbernew = 0
    
    #Loop for every row in the file
    for row in readerWS:

        #Adding each piece of data to the appropriate array
        names.append(row[0])
        games.append(int(row[1]))
        wins.append(int(row[2]))
        loses.append(int(row[3]))
        totalmoves.append(int(row[4]))
        shortestwin.append(int(row[5]))    


    #Closing the file
    file.close()

    #Creating boolean values to determine if either players is new and must be added to the csv file
    p1New = True
    p2New = True

    #Condition to run assuming there is data in the csv file to begin with       
    if len(names) > 0: 

    
        for i in range(0,len(names)):

            #If player 1 is found then the boolean is set to false
            if p1 == names[i]:
                p1New = False
                index1 = i
                

            #If player 2 is found then the boolean is set to false
            if p2 == names[i]:
                p2New = False
                index2 = i
                


            
    #If there is only 1 new player then 1 new space will be added to each array 
    if p1New == False and p2New == True:
        index2 = len(names)
        numbernew = 1

    #If there is only 1 new player then 1 new space will be added to each array
    if p1New == True and p2New == False:
       index1 = len(names)
       numbernew = 1

    #If there are 2 new players then 2 new spaces will be added to each array 
    if p1New == True and p2New == True:
        numbernew = 2
        #Indexes for the new players will always be the last to indexes in the arrays
        index1 = len(names)
        index2 = len(names)+1

    #Adding the new slots looping for the number of new players calculated in the previous conditions
    for i in range(0,numbernew):
        #Adding blank data
        names.append("")
        games.append(0)
        wins.append(0)
        loses.append(0)
        totalmoves.append(0)
        shortestwin.append(100)

  
    #Condition that will run if player 1 is already in the arrays
    if p1New == False:
        #Overwriting appropriate data in the arrays in player 1's index
        temp = int(games[index1]) + 1
        games[index1] = temp
        totalmoves[index1] += p1_moves

        #Condition to update player 1's shortest win if appropriate
        if shortestwin[index1] > p1_moves and winner == 1:
            shortestwin[index1] = p1_moves

    #Updating wins and loses values on both player's profiles if player 1 won
    if winner == 1:
       wins[index1] += 1
       loses[index2] += 1


    #Updating wins and loses values on both player's profiles if player 2 won
    if winner == 2:
        loses[index1] += 1
        wins[index2] += 1
   

    #Condition that will run if player 2 is already in the arrays
    if p2New == False:
        #Overwriting appropriate data in the arrays in player 2's index
        games[index2] += 1
        totalmoves[index2] += p2_moves

        #Condition to update player 2's shortest win if appropriate
        if shortestwin[index2] > p2_moves and winner == 2:
            shortestwin[index2] = p2_moves


    #Condition to run if player 1 is new
    if p1New == True:
        #Filling the new profile with data
        names[index1]= p1
        games[index1]= 1

        #Updating number of wins and loses if player 1 won
        if winner == 1:
            wins[index1]= 1
            loses[index1]= 0
            shortestwin[index1] = p1_moves
            
        #Updating the number of wins and loses if player 2 won
        if winner == 2:
            wins[index2]= 0
            loses[index2]= 1
  
        #Setting the total moves value to the number of moves made in the game by player 1 since it is their first game
        totalmoves[index1] = p1_moves

    
    #Condition to run if player 2 is new
    if p2New == True:
        #Filling the new profile with data
        names[index2] = p2
        games[index2] = 1

        #Updating the number of wins and loses if player 2 won
        if winner == 2:
            wins[index2] = 1
            loses[index2] = 0
            shortestwin[index2] = p2_moves

        #Updating the number of wins and loses if player 1 won
        if winner == 1:
            wins[index2] = 0
            loses[index2] = 1
            
        #Setting the total moves value to the number of moves made in the game by player 2 since it is their first game
        totalmoves[index2] = p2_moves
        

  

    #Deleting the csv file to make room for the new version
    os.remove("PlayerStats.csv")
    #Opening a file that does not exist will create a new file
    file = open("PlayerStats.csv","w")


    records = []
    temp = []

    #Turning the arrays into a 2D array of records
    for i in range(0,len(names)):

        temp.append(names[i])
        temp.append(games[i])
        temp.append(wins[i])
        temp.append(loses[i])
        temp.append(totalmoves[i])
        temp.append(shortestwin[i])

        records.append(temp)
        temp = []


    #Writing the records to the new csv file in the correct format  
    for i in range(0,len(records)):
        for x in range(0,6):
            file.write(str(records[i][x])+",")
        file.write("\n")
    file.close()

    #Returning the records local variable for use in the sort function
    return records

#Creating a function to sort the data 
def sort(records, language):

    #Language Bank#
    bank_wins = ["Wins - Leaderboard", "DUAIS - leaderboard", "Ganancias - Tabla de posiciones", "Victoires - Classement"]
    ###############


    
    #Sort by number of wins
    sort_wins = records

    #Printing the message indicating what the data has been sorted into       
    print(bank_wins[language])

    #The data is sorted with insertion sort

    #Loop for every value in the wins index in each record
    for i in range(0,len(sort_wins)):
        #Setting the data to be compared to the others
        current = sort_wins[i][2]
        position = i
       
        #Basic insertion sort operation, first data is considered to be sorted then others are compared to it to determine its place in the array
        while int(position) > 0 and int(sort_wins[position-1][2]) > int(current):
            temp = sort_wins[i]
            sort_wins[position] = sort_wins[position-1]
            sort_wins[position-1] = temp
            position -= 1
            i -= 1
         
        

        
    #Printing the sorted data in an appropriate format
    for i in range(len(records),0,-1):
        print(str(sort_wins[i-1][0])+" - "+str(sort_wins[i-1][2]))
 
  

        




#Calling basic starter functions
language = language_select()
query, board, stack, p1, p2, p1_win, p2_win, pause_req = import_game(language)

#Run functions to set up a new game
if query == False:   

    p1, p2, p1_win, p2_win, pause_req = player_names(language)
    board, movesMade = create_array()
    help_query(language)

#Functions that are always called 
format_array(board)
whoFirst, movesMade = firstMove(board)

########################  Main Program Loop  #########################

while p1_win == False and p2_win == False and pause_req == False and movesMade < 42 :

    if whoFirst == False:
        pause_req,stack, movesMade = player1(language, p1, board, stack, pause_req, movesMade)
        format_array(board)
        p1_win, p2_win = horizontal_search(board, p1_win, p2_win, p1, p2)
        p1_win, p2_win = vertical_search(board, p1_win, p2_win, p1, p2)
        p1_win, p2_win = diagonalLR_search(board, p1_win, p2_win, p1, p2)
        p1_win, p2_win = diagonalRL_search(board, p1_win, p2_win, p1, p2)
 
    
    if p1_win == False and pause_req == False:
        pause_req,stack, movesMade = player2(language, p2, board, stack, pause_req, movesMade)
        format_array(board)
        p1_win, p2_win = horizontal_search(board, p1_win, p2_win, p1, p2)
        p1_win, p2_win = vertical_search(board, p1_win, p2_win, p1, p2)
        p1_win, p2_win = diagonalLR_search(board, p1_win, p2_win, p1, p2)
        p1_win, p2_win = diagonalRL_search(board, p1_win, p2_win, p1, p2)
        whoFirst = False
    

#########################################################################

if movesMade == 42:
        print("The game has ended in a draw")

#Only call the sort and write functions if the game has ended due to a connect 4 or a draw
if pause_req == False and movesMade != 42:
    records = WriteStats(board, p1, p2)
    sort(records, language)


# NOTE : FIRST [] IS FOR ROW SECOND [] IS FOR COLLUM

#Vertical win search algorithm bug discovered, algorithm would think that [ ] is a
#vertical connect 4. This may have been due to the range values in the loop
#using negeative numbers which when started looping at index 0 in an array python then
#cylces through the array backwards which caused problems when identifying a vertical
#connect 4
