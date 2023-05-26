#imports
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy

#initialize app
app = Flask(__name__)
app.secret_key = "##aladin##"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sandb_user:qxXi516HQ1U5Akjmv6xX4OO2kaY9gwQW@dpg-cho6nspmbg50piol4o00-a.oregon-postgres.render.com/sandb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()

#databases
db = SQLAlchemy(app)

class travels_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(100))
    country = db.Column("country", db.String(100))
    city = db.Column("city", db.String(100))
    days = db.Column("days", db.String(100))
    date = db.Column("date", db.String(100))

    def __init__(self,title,country,city,days,date):
        self.title = title
        self.country = country
        self.city = city
        self.days = days
        self.date = date

class wanderungs_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(100))
    location = db.Column("location", db.String(100))
    description = db.Column("description", db.String(100))

    def __init__(self,title,location,description):
        self.title = title
        self.location = location
        self.description = description

class restaurants_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(100))
    food_type = db.Column("food_type", db.String(100))
    location = db.Column("location", db.String(100))
    price_score = db.Column("price_score", db.String(100))
    food_score = db.Column("food_score", db.String(100))
    vibe_score = db.Column("vibe_score", db.String(100))

    def __init__(self,title,food_type,location,price_score,food_score,vibe_score):
        self.title = title
        self.food_type = food_type
        self.location = location
        self.price_score = price_score
        self.food_score = food_score
        self.vibe_score = vibe_score

class movies_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(100))
    category = db.Column("category", db.String(100))
    score = db.Column("score", db.String(100))

    def __init__(self,title,category,score):
        self.title = title
        self.category = category
        self.score = score

class plans_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(100))
    date = db.Column("date", db.String(100))
    comment = db.Column("comment", db.String(100))

    def __init__(self,title,date,comment):
        self.title = title
        self.date = date
        self.comment = comment

class messages_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    message = db.Column("message", db.String(100))
    person = db.Column("person", db.String(100))

    def __init__(self,message,person):
        self.message = message
        self.person = person


#outside functions
def createLevels(max_lvl,base):
    xp_req = [base]
    for i in range(max_lvl):
        xp_req.append(xp_req[i]*1.25)
    return xp_req[1:]
#lvl = createLevels(200,10)
def getLvl(xp,lvl):
    if float(xp) < lvl[0]:
        pr = 1 - (float(xp)/lvl[0])
        pr = pr*100
        return (1, pr)
    elif float(xp) > lvl[-1]:
        pr = 100
        return (len(lvl), pr)
    else:
        act_lvl = 1
        while float(xp) > lvl[act_lvl]:
            act_lvl = act_lvl+1
            
        pr = 1 - ((lvl[int(act_lvl)]-float(xp))/(lvl[int(act_lvl)]-lvl[int(act_lvl-1)]))
        pr = pr*100
        
        return (act_lvl+1,pr)
    

class user_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(100))
    password = db.Column("password", db.String(100))
    partner = db.Column("partner", db.String(100))

    def __init__(self,username,password,partner):
        self.username = username
        self.password = password
        self.partner = partner

class couple_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    level = db.Column("level", db.String(100))
    xp = db.Column("xp", db.String(100))
    start_date = db.Column("start_date", db.String(100))

    def __init__(self,level,xp,start_date):
        self.level = level
        self.xp = xp
        self.start_date = start_date

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
    if "user" in session:
        couple_data = couple_db.query.first()
        partner = session["partner"]
        levels = createLevels(200,10)
        level, progress = getLvl(couple_data.xp,levels)
        couple_data.level = level
        db.session.commit()
        return render_template('index.html',couple_data=couple_data,partner=partner,progress=progress)
    else:
        return redirect(url_for("login"))

#login
@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        usr = request.form["username"]
        pss = request.form["password"]
        q = user_db.query.filter_by(username = usr).first()
        if q:
            if q.password == pss:
                session["user"] = q.username
                session["partner"] = q.partner
                return redirect(url_for("index"))
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    if "user" in session:
        session.pop("user")
        return redirect(url_for("index"))

#travels
@app.route('/travels')
def travels():
    travels = travels_db.query.all()
    return render_template('travels.html',travels=travels)

#add travel
@app.route('/addtravel',methods=['GET','POST'])
def addtravel():
    if request.method == 'POST':
        title = request.form["title_instance"]
        country = request.form["country_instance"]
        city = request.form["city_instance"]
        days = request.form["days_instance"]
        date = request.form["date_instance"]
        T = travels_db(title,country,city,days,date)
        db.session.add(T)
        db.session.commit()

        couple = couple_db.query.first()
        couple.xp = float(couple.xp) + points['Travels']
        db.session.commit()

        return redirect(url_for('travels'))
    else:
        return render_template('addtravel.html')

#wanderungs
@app.route('/wanderungs')
def wanderungs():
    wanders = wanderungs_db.query.all()
    return render_template('wanderungs.html',wanders=wanders)

#add wanderung
@app.route('/addwanderung',methods=['GET','POST'])
def addwanderung():
    if request.method == 'POST':
        title = request.form["title_instance"]
        location = request.form["location_instance"]
        description = request.form["description_instance"]
        W = wanderungs_db(title,location,description)
        db.session.add(W)
        db.session.commit()

        couple = couple_db.query.first()
        couple.xp = float(couple.xp) + points['Wanderungs']
        db.session.commit()

        return redirect(url_for('wanderungs'))
    else:
        return render_template('addwanderung.html')

#restaurants
@app.route('/restaurants')
def restaurants():
    restaurants = restaurants_db.query.all()
    return render_template('restaurants.html',restaurants=restaurants)

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
        R = restaurants_db(title,food_type,location,price_score,food_score,vibe_score)
        db.session.add(R)
        db.session.commit()

        couple = couple_db.query.first()
        couple.xp = float(couple.xp) + points['Restaurants']
        db.session.commit()

        return redirect(url_for('restaurants'))
    else:
        return render_template('addrestaurant.html')

#movies
@app.route('/movies',methods=['GET','POST'])
def movies():
    movies = movies_db.query.all()
    return render_template('movies.html',movies=movies)

#add movie
@app.route('/addmovie',methods=['GET','POST'])
def addmovie():
    if request.method == 'POST':
        title = request.form["title_instance"]
        category = request.form["category_instance"]
        score = request.form["score_instance"]
        M = movies_db(title,category,score)
        db.session.add(M)
        db.session.commit()

        couple = couple_db.query.first()
        couple.xp = float(couple.xp) + points['Movies']
        db.session.commit()

        return redirect(url_for('movies'))
    else:
        return render_template('addmovie.html')

#plans
@app.route('/plans')
def plans():
    plans = plans_db.query.all()
    return render_template('plans.html',plans=plans)

#add plan
@app.route('/addplan',methods=['GET','POST'])
def addplan():
    if request.method == 'POST':
        title = request.form["title_instance"]
        date = request.form["date_instance"]
        comment = request.form["comment_instance"]
        P = plans_db(title,date,comment)
        db.session.add(P)
        db.session.commit()

        couple = couple_db.query.first()
        couple.xp = float(couple.xp) + points["Plans"]
        db.session.commit()

        return redirect(url_for('plans'))
    else:
        return render_template('addplan.html')

#messages
@app.route('/messages')
def messages():
    return render_template('messages.html', messages = messages_db.query.all())

#add message
@app.route('/addmessage',methods=['GET','POST'])
def addmessage():
    if request.method == "POST":
        message = request.form["message_instance"]
        person = session["user"]
        M = messages_db(message,person)
        db.session.add(M)
        db.session.commit()

        couple = couple_db.query.first()
        couple.xp = float(couple.xp) + points['Messages']
        db.session.commit()

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
    db.create_all()
    app.run(debug=True)