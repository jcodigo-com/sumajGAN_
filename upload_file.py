import pyrebase

config = {
    "apiKey": "AIzaSyDO8U_NQjeXH52wjOTTZtvQQgVtfq4PI5U",
    "authDomain": "sumajgan.firebaseapp.com",
    "databaseURL": "https://sumajgan.firebaseio.com",
    "storageBucket": "sumajgan.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}


my_stream = db.child("experimentos").stream(stream_handler)