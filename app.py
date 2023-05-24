#imports
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

#initialize app
app = Flask(__name__)

########## routes

#index
@app.route('/')
def index():
    return '<h1>sandb</h1>' 

##########

#run app
if __name__ == '__main__':
    app.run(debug=True)