import math

LUT_encryption = dict()
LUT_decryption = dict()
publickey = []
privatekey = []
n = 0
e = 0
d = 0
message = ""
encrpted_message = "" 
decrypted_message = ""

def findd(on, e):
  x = 1
  y = "p"
  j = 1
  while y != x:
    y = (j*e) % on
    j += 1
  return (j - 1)

def coprime(on, i):
  return math.gcd(i, on)

def makekeys(p, q):
  global publickey, privatekey, n, e, d
  on = (p-1) * (q-1)
  n = p * q
  
  eops = []
  for pose in range(2, on):
    q = 0
    for i in range(1, pose +1):
      if coprime(i, on):
        eops.append(pose)

  e = eops[(len(eops)-1)]
  d = findd(on, e)

  publickey = [n, e]
  privatekey = [on, d]
  print ("Public Key:", publickey)
  print ("Private Key:", privatekey)
  print()
  welcome()


stillgoing = True

def welcome():
  global stillgoing
  while stillgoing:
    print('What would you like to do?')
    print('\t A. Make public/private keys')
    print('\t B. Encrpt a message')
    print('\t C. Decrpt a message')
    print("\t D. Exit")
    answer = input('Option:')
    if answer == 'a' or answer == 'A':
      i = int(input("Enter p:"))
      o = int(input('Enter q:'))
      print()
      makekeys(i, o)
    elif answer == 'b' or answer == 'B':
      print()
      encrypter()
    elif answer == 'c' or answer == 'C':
      print()
      decrypter()
    elif answer == 'd' or answer == 'D':
      stillgoing = False
    else:
      print ('Unknown command')
      welcome()




def encrypter():
  global encrpted_message, decrypted_message, e, n, message
  e = int(input('Enter e:'))
  n = int(input('Enter n:'))
  message = input("Enter message to encrypt:")
  for x in message:
    if x in LUT_encryption:
      encrpted_message += LUT_encryption[x]
    else:
      numerize = ord(x)
      encrypt = pow(numerize, e, n)
      denumerize = chr(encrypt)
      encrpted_message += denumerize
      LUT_encryption[x] = denumerize
    
  print (encrpted_message)
  print()
  welcome()
  
def decrypter():
  global encrpted_message, decrypted_message, e, n, d
  d = int(input('Enter d:'))
  n = int(input('Enter n:'))
  encrpted_message = input("Enter message to decrypt:")
  for t in encrpted_message:
    if t in LUT_decryption:
      decrypted_message += LUT_decryption[t]
    else:
      numerize = ord(t)
      decrypt = pow(numerize, d, n)
      denumerize = chr(decrypt)
      decrypted_message += denumerize
      LUT_decryption[t] = denumerize
  print (decrypted_message)
  print()
  welcome()












print('Welcome to the message encrpter and decrpter.')
welcome()












































































