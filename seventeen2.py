#!/usr/bin/env python

#Sample Place-In exam 2: Seventeen part 2 
#Imports
from random import randint

#Body

def main():

	with open("i206_placein_input.txt", "r") as f:
		all_games = f.readlines()

	all_games_list = []

	for line in all_games:
		line_nospace = line.strip()
		line_list = line_nospace.split(",")
		all_games_list.append(line_list)


	with open("i206_placein_output.txt", "w") as g:

		game_num = 1
		p1_n_wins = 0
		p2_n_wins = 0

		for game in all_games_list:
			n_marbles = 17
			play_sequence = []
			winner = ""
			for turn in game:
				player_1_n_take = min(n_marbles, int(turn))
				if (n_marbles - player_1_n_take) == 0:
					play_sequence.append(str(player_1_n_take))
					winner = "P2"
					p2_n_wins += 1

					play_sequence_joined = "-".join(play_sequence)
					g.write("\nGame #{0}. Play squence: {1}. Winner: {2}".format(game_num, play_sequence_joined, winner))
					game_num += 1

					break
				else:
					n_marbles -= player_1_n_take
					play_sequence.append(str(player_1_n_take))

				player_2_n_take = randint(1, min(n_marbles, 3))
				if (n_marbles - player_2_n_take) == 0:
					play_sequence.append(str(player_2_n_take))
					winner = "P1"
					p1_n_wins += 1

					play_sequence_joined = "-".join(play_sequence)
					g.write("\nGame #{0}. Play squence: {1}. Winner: {2}".format(game_num, play_sequence_joined, winner))
					game_num += 1

					break
				else:
					n_marbles -= player_2_n_take
					play_sequence.append(str(player_2_n_take))
		else:
			g.write("\nPlayer 1 won {0} time(s); Player 2 won {1} time(s).".format(p1_n_wins, p2_n_wins))


if __name__ == '__main__':
    main()