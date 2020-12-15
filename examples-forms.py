from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextField
#import boto3
import dbwrite

app = Flask(__name__)
app.config['SECRET_KEY'] = 'our very hard to guess secretfir'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')

# Simple form handling using raw HTML forms
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        print(first_name)
        print(last_name)    
        # Validate form data
        if len(first_name) == 0 or len(last_name) == 0:
            # Form data failed validation; try again
            error = "Please supply both first and last name"
        else:
            # Form data is valid; move along
            dbwrite.write_to_db(first_name, last_name)
            return redirect(url_for('thank_you'))

    # Render the sign-up page
    return render_template('sign-up.html', message=error)

# More powerful approach using WTForms
class RegistrationForm(Form):
    first_name = TextField('First Name')
    last_name = TextField('Last Name')

'''
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    form = RegistrationForm(request.form)

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return redirect(url_for('thank_you'))

    return render_template('register.html', form=form, message=error)
'''
# Run the application
app.run(debug=True,host='0.0.0.0',port=80)