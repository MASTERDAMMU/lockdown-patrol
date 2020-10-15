from flask import Flask, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/lockdown'
db = SQLAlchemy(app)


class Registration(db.Model):
    __tablename__ = 'registration'
   
    vehicle_number = db.Column(db.String(15), nullable=False,primary_key=True)
    citizen_name = db.Column(db.String(40), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    reason = db.Column(db.String(250), nullable=False)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email_id'] != 'admin@gmail.com' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('details'))
    return render_template('login.html', error=error)

@app.route("/details",methods=['GET', 'POST'])
def details():
    
    if(request.method=='POST'):
        vehi = request.form.get('vehicle_number')
       
        da = request.form.get('date_of_outing')
        k=Registration.query.filter_by(date=f"{da}")
        return render_template('details.html', k=k)
    return render_template('details.html')
 



@app.route("/registration", methods = ['GET', 'POST'])
def registration():
    
    if(request.method=='POST'):
        citizen = request.form.get('citizen_name')
        vehicle = request.form.get('vehicle_number')
       
        dat = request.form.get('date_of_outing')
        reaso = request.form.get('reason_of_outing')
        # cur =mysql.connection.cursor()
        # cur.execute('select count(vehicle_number) from registration where date={date}')
        # data=cur.fetchall()
        # if data<40:
        entry = Registration(citizen_name=citizen, vehicle_number = vehicle, date = dat,reason=reaso )
        db.session.add(entry)
        db.session.commit()
        #     cur.close()
        #     return render_template('index.html')
        # else:
        #     return render_template('login.html')
    return render_template('registration.html')


app.run(debug=True)


