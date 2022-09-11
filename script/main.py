from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send
import templates
import verify
import Sockets

app = Flask('app')
io = SocketIO(app)

@app.route('/')
def homepage():
  return templates.homepage()

@app.route('/login')
def login():
  return templates.login()

@app.route('/register')
def register():
  return templates.register()

@app.route('/chat')
def chat():
  return templates.chat()

@app.route('/chathub')
def chathub():
  return templates.chathub()

  
#teste
@io.on('tryLogin')
def tryLogin(user,password):
  if(Sockets.tryLogin(user,password)):
    #conectar usuário a conta
    io.emit('conected',user)

@io.on('setSocketId')
def setSocket(user,socket):
  print(socket)
  verify.updateSocketId(user,socket)

if __name__ == "__main__":
  io.run(app,host = '0.0.0.0', port=8080)