import socket,pickle
import speech_recognition

HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while 1:
    # Listen to the speaker to convert Speech-to-Text
    speech = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("listening")
        audio = speech.listen(mic)
            
    try:
        text = speech.recognize_google(audio)
    except:
        text = ""
    
    # Serialise data and send to the client for Text-to-Speech conversion
    print(text)
    data_string = pickle.dumps(text)
    
    conn.send(data_string)
conn.close()
