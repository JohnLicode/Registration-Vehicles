from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/registration vehicle'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    vehicle_vin = db.Column(db.String(17), primary_key=True)
    make = db.Column(db.String(45), nullable=False)
    model = db.Column(db.String(45), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(45), nullable=False)
    engine_type = db.Column(db.String(45), nullable=False)
    plate_type = db.Column(db.String(45), nullable=False)

class Owner(db.Model):
    __tablename__ = 'owner'
    owner_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    contact_details = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(245), nullable=False)

class Registration(db.Model):
    __tablename__ = 'registration'
    registration_id = db.Column(db.Integer, primary_key=True)
    vehicle_vin = db.Column(db.String(17), db.ForeignKey('vehicle.vehicle_vin'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.owner_id'), nullable=False)
    plate_number = db.Column(db.String(45), nullable=False)
    registration_status = db.Column(db.String(45), nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)


if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    # Run the Flask app
    app.run(debug=True)
