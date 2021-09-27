import socket
import pickle
import pyttsx3

# connect to localhost
HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while (1):
    # Receive the packet and start Text-to-Speech conversion
    packet = s.recv(4096)
    text = pickle.loads(packet)
    if (text != ''):
        print(text)
    else:
        continue

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

s.close()