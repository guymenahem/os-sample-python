from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Welcome to the IDFCTS small demo! </h1>"

if __name__ == "__main__":
    application.run()
