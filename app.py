#imports
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

#initialize app
app = Flask(__name__)
app.secret_key = "##aladin##"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#databases
db = SQLAlchemy(app)

class travels_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(100))
    country = db.Column("country", db.String(100))
    city = db.Column("city", db.String(100))
    days = db.Column("days", db.String(100))
    date = db.Column("date", db.String(100))

class wanderungs_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(100))
    date = db.Column("date", db.String(100))
    description = db.Column("description", db.String(100))

class restaurants_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(100))
    food_type = db.Column("food_type", db.String(100))
    location = db.Column("location", db.String(100))
    price_score = db.Column("price_score", db.String(100))
    food_score = db.Column("food_score", db.String(100))
    vibe_score = db.Column("vibe_score", db.String(100))

class movies_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(100))
    category = db.Column("category", db.String(100))
    score = db.Column("score", db.String(100))

class plans_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(100))
    date = db.Column("date", db.String(100))
    comment = db.Column("comment", db.String(100))

class messages_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    message = db.Column("message", db.String(100))


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

#points
points = {
    'Travels': 1000,
    'Wanderungs': 250,
    'Restaurants': 100,
    'Movies': 50,
    'Plans': 25,
    'Messages': 10
}

########## routes

#index
@app.route('/')
def index():
    return render_template('index.html')

#login
@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

#travels
@app.route('/travels')
def travels():
    return render_template('travels.html')

#add travel
@app.route('/addtravel',methods=['GET','POST'])
def addtravel():
    if request.method == 'POST':
        title = request.form["title_instance"]
        country = request.form["country_instance"]
        city = request.form["city_instance"]
        days = request.form["days_instance"]
        date = request.form["date_instance"]
        return redirect(url_for('travels'))
    else:
        return render_template('addtravel.html')

#wanderungs
@app.route('/wanderungs')
def wanderungs():
    return render_template('wanderungs.html')

#add wanderung
@app.route('/addwanderung',methods=['GET','POST'])
def addwanderung():
    if request.method == 'POST':
        title = request.form["title_instance"]
        date = request.form["date_instance"]
        description = request.form["description_instance"]
        return redirect(url_for('wanderungs'))
    else:
        return render_template('addwanderung.html')

#restaurants
@app.route('/restaurants')
def restaurants():
    return render_template('restaurants.html')

#add restaurant
@app.route('/addrestaurant',methods=['GET','POST'])
def addrestaurant():
    if request.method == 'POST':
        title = request.form["title_instance"]
        food_type = request.form["ftype_instance"]
        location = request.form["location_instance"]
        price_score = request.form["pscore_instance"]
        food_score = request.form["fscore_instance"]
        vibe_score = request.form["vscore_instance"]
        return redirect(url_for('restaurants'))
    else:
        return render_template('addrestaurant.html')

#movies
@app.route('/movies',methods=['GET','POST'])
def movies():
    return render_template('movies.html')

#add movie
@app.route('/addmovie',methods=['GET','POST'])
def addmovie():
    if request.method == 'POST':
        title = request.form["title_instance"]
        category = request.form["category_instance"]
        score = request.form["score_instance"]
        return redirect(url_for('movies'))
    else:
        return render_template('addmovie.html')

#plans
@app.route('/plans')
def plans():
    return render_template('plans.html')

#add plan
@app.route('/addplan',methods=['GET','POST'])
def addplan():
    if request.method == 'POST':
        title = request.form["title_instance"]
        date = request.form["date_instance"]
        comment = request.form["comment_instance"]
        return redirect(url_for('plans'))
    else:
        return render_template('addplan.html')

#messages
@app.route('/messages')
def messages():
    return render_template('messages.html')

#add message
@app.route('/addmessage',methods=['GET','POST'])
def addmessage():
    if request.method == "POST":
        message = request.form["message_instance"]
        return redirect(url_for("messages"))
    else:
        return render_template('addmessage.html')

#onwork
@app.route('/onwork')
def onwork():
    return render_template('onwork.html')

##########

#run app
if __name__ == '__main__':
    app.run(debug=True)