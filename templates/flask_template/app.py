# A BASE TEMPLATE FOR FLASK APP FROM `GOD.py`
# Dir Structure

#/root
#   │   app.py
#   │   requirements.txt
#   │   
#   ├───static
#   │   ├───assets
#   │   ├───css
#   │   │       index.css
#   │   │       
#   │   ├───images
#   │   └───js
#   │           index.js
#   │
#   └───templates
#           404.html
#           index.html
#  


from flask import (Flask, session, request,
                  redirect, render_template, 
                  send_file, send_from_directory,
                  abort, flash, url_for, render_template_string)



app = Flask(__name__)
# change the secret_key to any random password. 
# This is used to save sessions.
app.secret_key = "YOUR_SECRET_KEY (A password like stuff)"





@app.route('/', methods=['GET'])
def index():
    # the index.html is located at
    # templates/index.html
    return render_template("index.html")




@app.errorhandler(404)
def _404():
    # the 404 page to show up, 
    # when the user has entered unknown endpoint.
    return render_template("404.html")





if __name__ == '__main__':
    # change the True to false, if you dont want the 
    # server to reload when you make changes in any file
    app.run("0.0.0.0", "7868", True)