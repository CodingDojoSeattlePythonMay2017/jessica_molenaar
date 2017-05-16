from flask import Flask, render_template, request, redirect, flash
from base64 import b64encode
from os import urandom
random_bytes = urandom(10)
token = b64encode(random_bytes).decode('utf-8')
app = Flask(__name__)
app.secret_key = token #Genterated via terminal using >>> import os >>>os.urandom(13) () can me any number

@app.route('/')
def form():
   return render_template("/DojoSurveyValidation/Form.html")
   print "Got Post Info"

@app.route('/name', methods=['POST'])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(request.form['name']) < 1:
        flash("Name field cannot be empty.") #pass a string into the flash function, check len()
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Comments cannot be more than 120 characters.") #pass a string into the flash function, check len()
        return redirect('/')
    else:
        return redirect('/DojoSurveyValidation/success.html', name = name, location = location, language = language, comment = comment)

app.run(debug=True) # run our server
