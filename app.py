from flask import *
from database import*
from model import *
app = Flask(__name__)

# @app.route('/')
# def home_page():

#     return render_template("home.html")


@app.route('/',methods=['GET','POST'])
def join_band():
    if request.method=='GET':
        return render_template('home.html' ,   instruments = ['Acoustic Guitar','Electric Guitar',"Drums",'Piano',"Bass","Violin",'Vocals','Saxophone','Oud','Trumpet','Flute',"Musical Triangles",'Kazoo','Other'])
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
        notes=request.form["notes"]
        add_user(name,age,email,skill_level,genre,instrument,notes)
        return redirect("/")
@app.route('/join_band/<string:instrument>')
def find_bandmates(instrument):
    instrument=instrument
    instruments=query_user_by_instrument(instrument)
    return render_template('instrument.html', instruments=instruments,instrument=instrument)
if __name__ == '__main__':
    app.run(debug=True)