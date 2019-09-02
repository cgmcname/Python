#Christopher McNames
#ID 010746700

import sys

# Import socket library
from socket import *

# Set port number by converting argument string to integer
# If no arguments set a default port number
# Defaults
if sys.argv.__len__() != 2:
    serverPort = 25005
# Get port number from command line
else:
    serverPort = int(sys.argv[1])

# Choose SOCK_STREAM, which is TCP
# This is a welcome socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# The SO_REUSEADDR flag tells the kernel to reuse a local socket
# in TIME_WAIT state, without waiting for its natural timeout to expire.
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Start listening on specified port
serverSocket.bind(('', serverPort))

# Listener begins listening
serverSocket.listen(1)

print("CN Banking is at your service... ")


class Account:
   'Common base class for all employees'
   balance = 10000


    
   def transact( self, x ):
        self.balance =  x + self.balance
        Account.balance = self.balance
        return self.balance
   
   def lazyness(self, x):
       Account.balance = x
       
   
   def __init__(self):
      self.balance = Account.balance
      
   
   

   def displayAccount(self):
      print ("Balance : ", self.balance)

# Forever, read in sentence, convert to uppercase, and send
while 1:
    # Wait for connection and create a new socket
    # It blocks here waiting for connection
    connectionSocket, addr = serverSocket.accept()

    # Read bytes from socket
    sentence = connectionSocket.recv(1024)
  
    # Convert sentence to uppercase
    # Note you can often send strings directly and it will work but
    # you should be aware that it does not always act correct.
    sentenceString = sentence.decode('utf-8')
    
    acc = Account()
    
    save = acc.balance
    
    if (sentenceString == 'Q'):
        connectionSocket.close()
        serverSocket.close()
        exit()
    
    if ( sentenceString != 'B' and sentenceString != 'Q' ):
        try:
    # Intentionally raise an error.
            acc.transact(float(sentenceString))
        except:
    # Except clause:
            print("\n")
        
        #this = acc.balance
        
    if (sentenceString == 'B'):
        acc.transact(0.0)
        
   
    
    
    #acc.displayAccount()
    
    this = acc.balance
    
    bob = str(this)
    
    if (this < 0):
        bob = "Insufficient funds for withdrawal "
        acc.lazyness(save)
    
    
    #print(bob)
    #capitalizedSentence = sentenceString.upper()
    capitalizedSentenceBytes = bob.encode('utf-8')
  
    # Send it into established connection
    connectionSocket.send(capitalizedSentenceBytes)
  
    # Close connection to client but do not close welcome socket
    connectionSocket.close()
