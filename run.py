import os
import json

# request is going to handle things like finding out what method we used, and also it will contain our form object when we've posted it
# The flask library is used when we want to display a non-permanent message to the user, something that only stays until we refresh the page or go to a different one
from flask import Flask, render_template, request, flash

# After importing the class we need to create an instance of it and store it in a variable called app
app = Flask(__name__)
app.secret_key = 'some_secret'

# We use the route decorator to tell Flask what URL should trigger the function that follows.
# In Python, a decorator starts with the @ sign, which is
# also called pie notation. And, effectively, a decorator
# is a way of wrapping functions.
@app.route("/")
def index():
    return render_template("index.html")

# The root decorator binds the index() function to itself so that whenever that root is called, the function is called.
# Also, these functions which are called views
# Here we also added a second argument, a variable called page_title
@app.route("/about")
def about():
    
    # Initialize an empty array called data.
    # Then, using a with block, just as we did before when we were doing reading from files, I'm going to put: with open ("data/company.json", "r") as json_data.
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)
    
# Her we create a new route which will display more info about the character once the user click on his names
@app.route("/about/<member_name>")
def about_member(member_name):
    # First we create an empty object
    member = {}
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        # Now we iterate through that data array that we've created
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    
    return render_template("member.html", member=member)
    
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form["name"]))
    return render_template("contact.html", page_title="Contact")
    
@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")
    
# if __name__ == "__main__": then we're going to run our app with the following arguments:
# This is an internal environment variable that Cloud9 has set, and we're using the os
# module from the standard library to get that environment variable for us.
# It's the same with PORT, but this time we're casting it as an int, because it needs to be an integer. 
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            
# it's important to note that we should never have debug=true in a production
# application or when we submit our projects for assessment. This is very
# important because having debug equals true can allow arbitrary code to be run,
# and so obviously this is a security flaw. 