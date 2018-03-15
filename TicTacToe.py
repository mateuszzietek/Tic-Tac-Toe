import os

clear = lambda: os.system('cls')

#______________________PLAYERS FUNCTION DEFINITION______________________________________

def players ():
	plyrs = {"player1" : ["",""], "player2" : ["",""]}

	plyrs["player1"][0] = input("player 1 name: ").capitalize()
	plyrs["player1"][1] = input("\nplayer 1 character: ").upper()
	
	while plyrs["player1"][1] != "X" and plyrs["player1"][1] != "O":
		print("\nOnly 'x' or 'o' are allowed! Try again!")
		plyrs["player1"][1] = input("\nplayer 1 character: ").upper()



	plyrs["player2"][0] = input("\nplayer 2 name: ").capitalize()
	
	if plyrs["player1"][1] == "X":
		plyrs["player2"][1] = "O"
	else:
		plyrs["player2"][1] = "X"

	return plyrs

#______________________GAME FUNCTION DEFINITION______________________________________

def game(score, competitors, player_cont):
	
	clear()

	#LISTS DEFINITION
	fld = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
	pattern_x = ["X", "X", "X"]
	pattern_o = ["O", "O", "O"]
	variants = []
	lines_start = " | | \n | | \n | | "

	#FLOW CONTROL
	lines_start_control = 1
	
	#_________GAME LOOP___________

	while (pattern_x not in variants) and (pattern_o not in variants) and (" " in fld):
		
		
		#_______________________________
		# PRINT EMPTY GAME FIELD
		if lines_start_control == 1:    
			clear()
			print(lines_start)
			lines_start_control = 0
		#_______________________________


		# SELECT FIELD NUMBER
		if player_cont == 1:
			print("\n", competitors["player1"][0], " pick the field!")
			player_input = int(input("\nenter digit from 1 to 9\n"))-1
		else:
			print("\n", competitors["player2"][0], " pick the field!")
			player_input = int(input("\nenter digit from 1 to 9\n"))-1

		# CHECK IF SLECTED FIELD IS BETWEEN 1 AND 9
		if player_input in range(0,9):

			# PLATER 1 TURN
			if player_cont == 1:
				
				while fld[player_input] != " ":
					
					print("\nSelect one of empty field!\n")
					player_input = int(input())-1

				else:

					fld[player_input] = competitors["player1"][1]
					player_cont = 0

			# PLAYER 2 TURN
			else:
				
				while fld[player_input] != " ":

					print("\nSelect one of empty field!\n")
					player_input = int(input())-1

				else:
					fld[player_input] = competitors["player2"][1]
					player_cont = 1

		# WHAT IF SELECTED FIELD IS NOT 1-9
		else:
			
			while player_input not in range(0,9):

				print("\nWrong choice! Try again!")
				player_input = int(input())-1

			if player_cont == 1:

				fld[player_input] =  competitors["player1"][1]
				player_cont = 0
			
			else:

				fld[player_input] =  competitors["player2"][1]
				player_cont = 1

		# PRINTING AND VARIANT CHECKING
		variants = [
				[fld[0], fld[1], fld[2]], 
				[fld[3], fld[4], fld[5]],
				[fld[6], fld[7], fld[8]],
				[fld[6], fld[3], fld[0]],
				[fld[7], fld[4], fld[1]],
				[fld[8], fld[5], fld[2]],
				[fld[6], fld[4], fld[2]],
				[fld[8], fld[4], fld[0]],
				]

		lines = "{x[6]}|{x[7]}|{x[8]} \n{x[3]}|{x[4]}|{x[5]} \n{x[0]}|{x[1]}|{x[2]}".format(x = fld)
		
		clear()
		print(lines)


	else:

		clear()

		print(lines)

		# COUNTING SCORES
		if pattern_x in variants:

			if  competitors["player1"][1].lower() == "x":

				print("\n POINT FOR ",  competitors["player1"][0])
				score[0] += 1

			else:

				print("\n POINT FOR ",  competitors["player2"][0])
				score[1] += 1

			

		elif pattern_o in variants:

			if  competitors["player1"][1].lower() == "o":

				print("\n POINT FOR ",  competitors["player1"][0])
				score[0] += 1

			else:

				print("\n POINT FOR ",  competitors["player2"][0])
				score[1] += 1

		else:

			print("\nPlayers are tie!")


		print("\nSCORE:\n", competitors["player1"][0], ":{pt[0]}\n".format(pt = score), competitors["player2"][0], ":{pt[1]}".format(pt = score))
		

		# PLAY AGAIN?
		decision = input("\n\nPlay again? Y/N\n")
		
		if decision.lower() == "y":

			game(score, competitors, player_cont)
			
		else:

			pass

	return score


print("			WELCOME TO TIC TAC TOE GAME!\n\nEnter your names and choose characters:\n")

#______________________CALL THE GAME_________________________________    

players_var = players()

finalscore = game([0, 0], players_var, 1)

clear()

#______________________SUMMARY AND GAME OVER_________________________________  

print("\n GAME OVER. FINAL SCORE: \n", "\n", players_var["player1"][0], ": {fpt[0]}\n".format(fpt = finalscore), players_var["player2"][0],": {fpt[1]}".format(fpt = finalscore))

if finalscore[0] > finalscore[1]:
	print("\n" , players_var["player1"][0] , "WIN THE GAME!")

elif finalscore[0] < finalscore[1]:
	print("\n" ,players_var["player2"][0] , "WIN THE GAME!")

else:
	print("\n PLAYERS ARE TIE!")


input("\nPRESS ENTER TO QUIT.")