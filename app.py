from flask import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/join_band')
def join_band():
	return render_template('join_band.html')

@app.route('/sign_in')
def sign_in():
	return render_template('sign_in.html')

@app.route('/sign_up')
def sign_up():
	return render_template('sign up.html')

if __name__ == '__main__':
	app.run(debug=True)