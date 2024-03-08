from flask import Blueprint, render_template, request, flash

ame= Blueprint('ame', __name__)

@ame.route('/ame', methods=['GET','POST']) 
def home():
    return render_template("ame.html")
