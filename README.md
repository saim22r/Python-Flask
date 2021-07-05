# Model View Controller (MVC) with Python Flask
# HTML details and basics

## Python Flask
- Flask is a python micro-framework
- Flask is used to develop web apps
````
from flask import Flask, redirect, url_for, render_template
# We have to create an object of this class
app = Flask(__name__) # Creating an app instance
````
Make a route to the home page
```
# Let's create a function to link to our home/default page#
# Let's connect this function to our browser
@app.route("/") # Decorating our function with @app.route to set route in our browser
def index():
    return "<h1> Welcome to Engineering 89 DevOps team </h1> "
```