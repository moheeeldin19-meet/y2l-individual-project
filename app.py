from flask import *
from database import*
from model import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/join_band',methods=['GET','POST'])
def join_band():
    if request.method=='GET':
        return render_template('join_band.html')
    else :
    	instrument=request.form["instrument"]
    	query_user_by_instrument(instrument)

# @app.route('/sign_in',methods=['GET','POST'])
# def sign_in():
# 	return render_template('sign_in.html')

@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
    if request.method=='GET':
        query_user_by_instrument("bass")
        return render_template('sign up.html')

    else :
        name=request.form['name']
        age=request.form['age']
    	email =request.form['email']
        skill_level =request.form['skill_level']
    	genre=request.form["genre"]
    	instrument=request.form["instrument"]
    	add_user(name,age,email,skill_level,genre,instrument)
    	return redirect("join_band")
@app.route('/instrument/<string:instrument>')
def find_bandmates(instrument):
    instruments=query_user_by_instrument(instrument)
    return render_template('instrument.html', instrument=instrument)
if __name__ == '__main__':
	app.run(debug=True)