# import dependency 
from flask import Flask
# create new flask app
app = Flask(__name__)
#create flask routes
@app.route('/')
def hello_world():
    return 'Hello world'

if __name__ == '__main__':
    app.run()