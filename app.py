#imports
from flask import Flask, render_template, redirect
from flask_restful import Api, Resource, reqparse, abort

#initialize app
app = Flask(__name__)

########## routes

#user passwords
users = {
    'sofy': {'password':'totoro'},
    'blank': {'password':'aladin'}
}

rel = {
    'level': 1
}

#couple level generator
def createLevels(max_lvl):
    xp_req = [10]
    for i in range(max_lvl):
        xp_req.append(xp_req[i]*1.1)
    return xp_req

#index
@app.route('/')
def index():
    return render_template('index.html')

#travels
@app.route('/travels')
def travels():
    return render_template('travels.html')

#add travel

#wanderungs
@app.route('/wanderungs')
def wanderungs():
    return render_template('wanderungs.html')

#add wanderung

#restaurants
@app.route('/restaurants')
def restaurants():
    return render_template('restaurants.html')

#add restaurant

#movies
@app.route('/movies')
def movies():
    return render_template('movies.html')

#add movie

#plans
@app.route('/plans')
def plans():
    return render_template('plans.html')

#add plan

#messages
@app.route('/messages')
def messages():
    return render_template('messages.html')

#add message

##########

#run app
if __name__ == '__main__':
    app.run(debug=True)