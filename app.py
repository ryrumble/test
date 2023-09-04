#This is my first Flask app.
from flask import Flask
#create an object with the Flask module
app = Flask(__name__)
#tell Flask when to call the hello function
@app.route("/")
#show something in the browser
def hello():
    return "Hello World!";

#another route is made with an 'its me'function
@app.route("/ryan")
def itsme():
    return "here is page ryan"

#call the run function to run the app
    #making a note.. app failed to run first tiem, so waitress was installed
    #i commented out the line app.run(debug = True) and used the serve function
    #and then it worked!
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    #app.run(debug = True)
