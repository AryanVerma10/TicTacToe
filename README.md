# TicTacToe
This readme file will explain the basic working of the code. 
I have used Python Dictionary Data Structure for the working of the Game.
There are three variables namely player, tm for total moves and em is the checker for winning of cross or zero.
Then the function is created for checking who wins keeping one thing in mind that 0 is in the mid position.
There are three conditions vertical , horizontal and diagonal. The diagonal conditionfor X remains invalid because 0 is in the mid position.
The check conditons reurns 1 for X and 0 and if no one wins (draw condition) the check condition returns 0 and this 1 or 0 is stored in em(variable).
The while loop checks for winning if tm==8 it means all moves are over and it's a draw. If em==1 it means either 0 or X has won because the function returned 1.
The nested while loop rotates the move from player 1 to player 2 and vice-versa.The if conditions checks that whether the player has entered X or 0 in the stated position (1 to 9).
The else part is for making the iterating condition go back to first step if the input is wrong.
The game is printed with the moves from the players and then the function is called to check who win.
The program ends after the declaration of the result. 
