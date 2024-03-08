from flask import Blueprint, render_template, request, flash

space= Blueprint('space', __name__)

@space.route('/', methods=['GET','POST']) 
def home():
    return render_template("index.html")