# Creating a file called app.py
# Let's see how we can use Python flask to interact with our browser
# Install flask:
# pip install flask

from flask import Flask, redirect, url_for, render_template
# We have to create an object of this class
app = Flask(__name__) # Creating an app instance

# Let's create a function to link to our home/default page#
# Let's connect this function to our browser
@app.route("/") # Decorating our function with @app.route to set route in our browser
def index():
    return "<h1> Welcome to Engineering 89 DevOps team </h1> "

# To run type `flask run`

# Let's create a welcome page
@app.route("/welcome/")
def welcome():
    return render_template("welcome.html")

# Create a decorator to route traffic to a login page
# Display two messages of your choice in heading1 and heading2

@app.route("/login/")
def login(): # redirect and url_for we need to import to redirect users
    # return "<h1> Please Login </h1> <h2> Using your email and password </h2> "
    return redirect(url_for("welcome"))

if __name__ == "__main__":
    app.run(debug=True)
# Let's add our HTML file to redirect from Python flask to .html file
# We need to create a folder called templates
# project folder
    # Templates folder
        # welcome.html
    # app.py
# What if the login page is unavailable
# We would like to redirect the users if they visit the login page
# Create a decorator to route traffic