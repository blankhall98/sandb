#imports
from flask import Flask, render_template, redirect
from flask_restful import Api, Resource, reqparse, abort

#initialize app
app = Flask(__name__)

#outside functions
def createLevels(max_lvl,base):
    xp_req = [base]
    for i in range(max_lvl):
        xp_req.append(xp_req[i]*1.25)
    return xp_req[1:]
#lvl = createLevels(200,10)
def getLvl(xp,lvl):
    if xp < lvl[0]:
        return 1
    elif xp > lvl[-1]:
        return len(lvl)
    else:
        act_lvl = 1
        while xp > lvl[act_lvl]:
            act_lvl = act_lvl+1
        
        return act_lvl+1

def getLvl(xp,lvl):
    if xp < lvl[0]:
        return 1
    elif xp > lvl[-1]:
        return len(lvl)
    else:
        act_lvl = 1
        while xp > lvl[act_lvl]:
            act_lvl = act_lvl+1
        
        return act_lvl+1
    
#couple data
coupleData = {
    'partner1': {
        'username': 'sofy',
        'password': 'totoro'
    },
    'partner2': {
        'username': 'blank',
        'password': 'nietzsche'
    },
    'level': {
        'level': 1,
        'xp': 0
    },
    'relationship': {
        'start-date': '26/06/2022'
    }
}

########## routes

#index
@app.route('/')
def index():
    return render_template('index.html')

#login
@app.route('/login')
def login():
    return render_template('login.html')

#travels
@app.route('/travels')
def travels():
    return render_template('travels.html')

#add travel
@app.route('/addtravel')
def addtravel():
    return render_template('addtravel.html')

#wanderungs
@app.route('/wanderungs')
def wanderungs():
    return render_template('wanderungs.html')

#add wanderung
@app.route('/addwanderung')
def addwanderung():
    return render_template('addwanderung.html')

#restaurants
@app.route('/restaurants')
def restaurants():
    return render_template('restaurants.html')

#add restaurant
@app.route('/addrestaurant')
def addrestaurant():
    return render_template('addrestaurant.html')

#movies
@app.route('/movies')
def movies():
    return render_template('movies.html')

#add movie
@app.route('/addmovie')
def addmovie():
    return render_template('addmovie.html')

#plans
@app.route('/plans')
def plans():
    return render_template('plans.html')

#add plan
@app.route('/addplan')
def addplan():
    return render_template('addplan.html')

#messages
@app.route('/messages')
def messages():
    return render_template('messages.html')

#add message
@app.route('/addmessage')
def addmessage():
    return render_template('addmessage.html')

#onwork
@app.route('/onwork')
def onwork():
    return render_template('onwork.html')

##########

#run app
if __name__ == '__main__':
    app.run(debug=True)