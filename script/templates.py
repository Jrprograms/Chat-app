from flask import render_template

def homepage():
    return render_template('homepage.html')

def login():
    return render_template('login.html')

def register():
    return render_template('register.html')

def chat():
    return render_template('chat.html')

def chathub():
    return render_template('chathub.html')
