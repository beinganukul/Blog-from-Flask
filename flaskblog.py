from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c4753c609661979896d81971507bf7d8'

posts = [
    {
        'author':'Anukul Adhikari',
        'title':'Blog Post 2',
        'Content':'First Post Comment',
        'date_posted':'April 20,2018'
    },
    {
        'author':'Shamaraj Adhikari',
        'title':'Blog Post 3',
        'Content':'First Post Comment',
        'date_posted':'April 69,2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')    
def about():
    return render_template('about.html',title='About')

@app.route('/register', methods=['GET', 'POST'])    
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)    

if __name__=='__main__':
    app.run(debug=True)

