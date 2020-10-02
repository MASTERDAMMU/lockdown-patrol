from flask import Flask, render_template, request
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




@app.route("/registration", methods = ['GET', 'POST'])
def registration():
    if(request.method=='POST'):
        citizen = request.form.get('citizen_name')
        vehicle = request.form.get('vehicle_number')
       
        dat = request.form.get('date_of_outing')
        reaso = request.form.get('reason_of_outing')
        entry = Registration(citizen_name=citizen, vehicle_number = vehicle, date = dat,reason=reaso )
        db.session.add(entry)
        db.session.commit()
    return render_template('registration.html')


app.run(debug=True)


