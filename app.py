# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('login.html')  # render a template


@app.route('/newpassword', methods=['GET', 'POST'])
def newpassword():    
    error = None
    if request.method == 'POST':
        if request.form['newpass'] != request.form['conpass']:
            error = 'Password Does not Match..!!'
        else:
            return redirect(url_for('home'))
    return render_template('newpassword.html', error=error)
    

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template('dashboard.html') # render a template

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)
    # Route for handling the login page logic
@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin@gmail.com':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('newpassword'))
    return render_template('forgot.html', error=error)


# Route for handling the login page logic
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        phone=request.form['phone']
        email=request.form['email']
        password=request.form['password']
        confirmpassword=request.form['confirmpassword']
        
        if confirmpassword!=password:
           error='Password does not match..!!'
                   
        else:
            return redirect(url_for('home'))            
    return render_template('register.html', error=error)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
