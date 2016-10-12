def get_matches(players):
	matchup = []
	for indx1, player1 in enumerate(players):
		for indx2, player2 in enumerate(players):
			if player1 is not player2 and indx1 < indx2:
				pair = player1, player2
				matchup.append(pair)
	return matchup
