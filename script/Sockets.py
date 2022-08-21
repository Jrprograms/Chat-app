from flask_socketio import SocketIO, emit
import verify

def conetou(login,password):
  print(login,password)

def tryLogin(user,password):
  if(verify.verifyKey(user,password)):
    return True
  else:
    return False
