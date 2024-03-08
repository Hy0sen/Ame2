from flask import Blueprint, render_template, request, flash

lore= Blueprint('lore', __name__)

@lore.route('/lore', methods=['GET','POST']) 
def home():
    return render_template("lore.html")