import functools

from flask import Blueprint,redirect, render_template, request, flash, session, url_for

auth= Blueprint('auth', __name__)

@auth.route('/auth', methods=['GET','POST']) 
def home():
    if request.method=="POST":
        username=request.form.get('username')
        Password=request.form.get('password')
        error=None
        user=username
        if user!= "Frosty":
            error='Incorrect username'
        elif Password!="Rajat":
            error='Incorrect password'
        
        if error is None:
            return redirect(url_for('ame.home'))
    
    return render_template("auth.html")