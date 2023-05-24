from flask import Flask

#initialize app
app = Flask(__name__)

#run app
if __name__ == '__main__':
    app.run(debug=True)