#!/usr/bin/env python

#Sample Place-In exam 2: Seventeen part 1 
#Imports
from random import randint

#Body

def main():
	print "Let's play the game of Seventeen!"
	n_marbles = 17

	while True:
		print "Number of marbles left in jar: {0}".format(n_marbles)
		player_n_take = raw_input("\nYour turn: How many marbles will you remove? (1-3) ")
		try:
			player_n_take_int = int(player_n_take)
		except:
			print "Invalid input. Try again, enter 1, 2, or 3."
			continue
		else:
			if player_n_take_int > 3 or player_n_take_int < 1 or (n_marbles - player_n_take_int) < 0:
				print "You must choose a number between 1 and 3 and not more than the number of marbles remaining. Try again."
				continue
			elif (n_marbles - player_n_take_int) == 0:
				print "There are no marbles left. Computer wins!"
				break
			else:
				n_marbles -= player_n_take_int
				print "You removed {0} marbles.".format(player_n_take)
				print "Number of marbles left in jar: {0}".format(n_marbles)

		#Min statement here ensures n_marbles doesn't go negative on computer's turn
		comp_n_take = randint(1, min(n_marbles, 3))
		if (n_marbles - comp_n_take) == 0:
			print "There are no marbles left. You win!"
			break
		else:
			n_marbles -= comp_n_take
			print "\nComputer's turn..."
			print "Computer removed {0} marbles.".format(comp_n_take)
			print "Number of marbles left in jar: {0}".format(n_marbles)


if __name__ == '__main__':
    main()