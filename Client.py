#Christopher McNames
#ID 010746700

import sys

# Import socket library
from socket import *

# Set hostname or IP address from command line or default to localhost
# Set port number by converting argument string to integer or use default
# Use defaults
if sys.argv.__len__() != 3:
    serverName = 'localhost'
    serverPort = 25005
# Get from command line
else:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])

# Choose SOCK_STREAM, which is TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server using hostname/IP and port
clientSocket.connect((serverName, serverPort))

# Get sentence from user
print('Hello, welcome to CN Banking.')

print('\n')

choice = input('Would you like to withdraw(W), deposit(D), check balance(B) or quit(Q): ')

while ( choice.upper() != 'W' and choice.upper() != 'D' and choice.upper() != 'B' and choice.upper() != 'Q'   ):
    choice = input('Please try again, would you like to withdraw(W), deposit(D), check balance(B) or quit(Q): ')

while (choice.upper() != 'Q'):
    
    
    
    
    
    if ( choice.upper() == 'W' or choice.upper() == 'D' ):   
        value = input('What is the amount?: ')
        sentence = value 
    
    try:
    # Intentionally raise an error.
        x = float(value)
    except:
    # Except clause:
        print("Error occurred. Please input a numerical value...")
        x = 0    
    
        
    while(x < 0):
        value = input('Please enter non-negitive amount: ')
        
        try:
    # Intentionally raise an error.
            x = float(value)
            sentence = value 
        except:
    # Except clause:
            print("Error occurred. Please input a numerical value...")
            x = -1
    
    
    
    
    if(choice.upper() == 'B'):
        sentence = 'B'
        value = 0
    
    try:
    # Intentionally raise an error.
        x = float(value)*-1
    except:
    # Except clause:
        print('\n')
        x = 0    

    #print('Look : ', x)

    if (choice.upper() == 'W'):
        sentence = str(x)

  
        
    

    # Send it into socket to server
    sentenceBytes = sentence.encode('utf-8')
    clientSocket.send(sentenceBytes)

    # Receive response from server via socket
    modifiedSentence = clientSocket.recv(1024)

    print('Your balance is : {0}'.format(modifiedSentence.decode('utf-8')))
    
    print('\n')
    
    
    
    choice = input('Welcome back, would you like to withdraw(W), deposit(D), check balance(B) or quit(Q): ')
    
    while ( choice.upper() != 'W' and choice.upper() != 'D' and choice.upper() != 'B' and choice.upper() != 'Q'   ):
        choice = input('Please try again, would you like to withdraw(W), deposit(D), check balance(B) or quit(Q): ')
    
    # Choose SOCK_STREAM, which is TCP
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Connect to server using hostname/IP and port
    clientSocket.connect((serverName, serverPort))
    
    


choice = input('Would you like to disconnect the server? (Y/N) :') 
    
if(choice.upper() == 'Y'):
    sentence = 'Q'
    sentenceBytes = sentence.encode('utf-8')
    clientSocket.send(sentenceBytes)
    modifiedSentence = clientSocket.recv(1024)
 # Send it into socket to server


    # Receive response from server via socket
#modifiedSentence = clientSocket.recv(1024)

print('\n')

print('Thank you for using CN Banking...goodbye' )

clientSocket.close()
