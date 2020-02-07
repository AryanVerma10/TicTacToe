game={
      '1':' ','2':' ','3':' ',      #Initializing a Dictionary
      '4':' ','0':'0','6':' ',
      '7':' ','8':' ','9':' '
      }
player=1
tm=0    #total moves
em=0    #Winning counter

def check():         #Function to check who wins keeping in mind 0 is in the mid position

    
                 #Check for Horizontal Condition
    if game["1"]=="X" and game["2"]=="X" and game["3"]=="X":
        print("Player 1 wins" )

    
    if game["7"]=="X" and game["8"]=="X" and game["9"]=="X":
        print("Player 1 wins" )
        return 1
   
                 #Check for Vertical Condition
    if game["1"]=="X" and game["4"]=="X" and game["7"]=="X":
        print("Player 1 wins" )
        return 1
    
    if game["3"]=="X" and game["6"]=="X" and game["9"]=="X":
        print("Player 1 wins" )
        return 1
    
    
                 #Check for Horizontal Condition
    if game["1"]=="0" and game["2"]=="0" and game["3"]=="0":
        print("Player 2 wins" )
        return 1
    if game["4"]=="0" and game["0"]=="0" and game["6"]=="0":
        print("Player 2 wins" )
        return 1
    if game["7"]=="0" and game["8"]=="0" and game["9"]=="0":
        print("Player 2 wins" )
        return 1


                 #Check for Vertical Condition
    if game["1"]=="0" and game["0"]=="0" and game["9"]=="0":
        print("Player 2 wins" )
        return 1
    if game["3"]=="0" and game["0"]=="0" and game["7"]=="0":
        print("Player 2 wins" )
        return 1
    if game["1"]=="0" and game["4"]=="0" and game["7"]=="0":
        print("Player 2 wins" )
        return 1

                #Check for Diagonal Condition
    if game["2"]=="0" and game["0"]=="0" and game["8"]=="0":
        print("Player 2 wins" )
        return 1
    if game["3"]=="0" and game["6"]=="0" and game["9"]=="0":
        print("Player 2 wins" )
        return 1
    return 0
    
print("1 | 2 | 3 ")     #Printing the 3x3 block for playing
print("__+___+___")   
print("4 | 0 | 6 ")
print("__+___+___")   
print("7 | 8 | 9 ")

while True:     #Check conditions for the players 
    if tm==8:   #if Total moves are 8 game over 
        print("No one wins")
        break
    if(em==1):  # if the function returns 1 means someone has won 
        break
    while True:
      if player==1:
        p1=input("Player 1")     #Input for player 1
        if p1.upper() in game and game[p1.upper()]==" ":  #Player 1 has to enter X 
            game[p1.upper()]="X"
            player=2
            break
        else:
            print("Invalid Input,\nChance of player 1")   # Check condition if player does not enters a valid input 
            continue
      else:
        p2=input("Player 2")    #Input for player 2
        if p2.upper() in game and game[p2.upper()]==" ":
                    game[p2.upper()]="0"    #Player 2 has to enter 0
                    player=1
                    break
        else:
            print("Invalid Input,\nChance of player 2")    # Check condition if player does not enters a valid input 
            continue
    tm+=1      # Increasing the number of total moves 
    print(game['1']+' | '+game['2']+' | '+game['3'])
    print("__+___+___")    
    print(game['4']+' | '+game['0']+' | '+game['6'])
    print("__+___+___")   
    print(game['7']+' | '+game['8']+' | '+game['9'])
    em=check()   #Calling the function to check wether anyone won or not
    
print()
                
                    
            
