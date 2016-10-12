#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module creates a matchup list of players"""


def get_matches(players):
	"""
	
	Args:
	    players (tuple): 
	    
	Returns:
	    matchup (list): 
	    
	Example:
	    >>> get_matches(['Harry', 'Howard', 'Hugh'])
	    [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
	"""
	matchup = []
	for indx1, player1 in enumerate(players):
		for indx2, player2 in enumerate(players):
			if player1 is not player2 and indx1 < indx2:
				pair = player1, player2
				matchup.append(pair)
	return matchup
