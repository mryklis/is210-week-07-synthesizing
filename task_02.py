#!/usr/bin/env python
# -*- coding: utf-8 -*-


import authentication
import getpass

def login(username, maxattempts=3):
    authd = False
    while maxattempts != 0:
        password = getpass.getpass('Please enter your password:')
        authd = authentication.authenticate(username, password)
        if authd is False:
            maxattempts -= 1
            attempts = 'Incorrect credentials, You have ' + \
                       str(maxattempts) + ' attempts left.'
            print attempts
            if maxattempts == 0:
                return authenticated
        elif authd is True:
            return authd == True
	
