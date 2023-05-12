# You have to set the secret key for sessions to work
# Make sure you keep this secret
 

from flask import flash, session
from functools import wraps

def login_required(function_to_protect):
    @wraps(function_to_protect)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')
        if user_id:
            user = database.get(user_id)
            if user:
                print("alreqady logged in")
                return function_to_protect(*args, **kwargs)
            else:
                flash("Session exists, but user does not exist (anymore)")
                return "AAAA"
        else:
            flash("Please log in")
            return "BBBB"