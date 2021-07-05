# Creating a file called app.py
# Let's see how we can use Python flask to interact with our browser
# Install flask:
# pip install flask

from flask import Flask
# We have to create an object of this class
app = Flask(__name__) # Creating an app instance

# Let's create a function to link to our home/default page#
# Let's connect this function to our browser
@app.route("/") # Decorating our function with @app.route to set route in our browser
def index():
    return "Welcome to Engineering 89 DevOps team"

# To run type `flask run`

# Let's create a welcome page
@app.route("/welcome/")
def welcome():
    return "<h1> Welcome page for Flask app</h1> "

# Create a decorator to route traffic to a login page
# Display two messages of your choice in heading1 and heading2

@app.route("/login/")
def login():
    return "<h1> Please Login </h1> <h2> Using your email and password </h2> "