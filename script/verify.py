from replit import db

def listKeys(user = "none"):
  if user == "none":
    print(db.keys())
  else:
    print(db[user])

def addKey(user,password):
  try:
    value = db[user]
    return print(f'Já existe esse usuário : {user} \n Tente outro')
  except:
    db[user] = {"user":user ,
                "password":password,
                "id" : ""}

def deletKey(user,password):
  try:
    value = db[user]
    DBpassword = (value.value['password'])
    if password == DBpassword:
      del db[user]
    else:
      return print("Usuário não encontrado")
  except:
      return print('Nao existe esse usuário')
    

def verifyKey(user,password):
  try:
    value = db[user]
    DBpassword = (value.value['password'])
    if password == str(DBpassword):
      print('Acesso Permitido')
      return True
    else:
      print("Senha Incorreta!")
      return False
  except:
    print('Usuário não encontrado')
    return False

def updateSocketId(user,socket):
  db[user]['id'] = socket
  print(db[user])