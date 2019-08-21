from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():

    # return "<h1>Welcome to the IDFCTS small demo! </h1>"

    return "<h1 style=\"color:blue;\">Welcome to the IDFCTS small demo! </h1> <br><br><br> <iframe src=\"https://www.pc.co.il/news/287438/\" width=\"1000\" height=\"600\"> ></iframe>"

if __name__ == "__main__":
    application.run()
