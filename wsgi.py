from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    
    return "<h1>Welcome to the IDFCTS small demo! </h1>"

    # return "<h1>Welcome to the IDFCTS small demo! </h1> <br> <iframe src="https://www.pc.co.il/news/287438/"></iframe>"

if __name__ == "__main__":
    application.run()
