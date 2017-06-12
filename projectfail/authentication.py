#!/usr/bin/env python
"""Este modulo propociona las funciones para autentificar usuarios."""

def login(username, password):
    """Login del usuario."""
    try:
        user_file = open('/etc/users.txt')    
        user_buf = user_file.read()
        users = [line.split("|") for line in user_buf.split("\n")]
        return [username, password] in users
    except IOError:
        print "No puedo autentificarte."
        return False
