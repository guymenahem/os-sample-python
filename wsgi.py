from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():

    # return "<h1>Welcome to the IDFCTS small demo! </h1>"

    return "<h1>Welcome to the IDFCTS small demo! </h1> <br><br><br> <iframe src=\"https://www.pc.co.il/news/287438/\" width=\"1200\" height=\"600\" align=\"middle\"> ></iframe>"

if __name__ == "__main__":
    application.run()
