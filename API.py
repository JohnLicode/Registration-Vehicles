from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/registration vehicles'
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

# Routes for Vehicle
@app.route('/vehicles', methods=['POST'])
def create_vehicle():
    data = request.get_json()
    new_vehicle = Vehicle(
        vehicle_vin=data['vehicle_vin'],
        make=data['make'],
        model=data['model'],
        year=data['year'],
        color=data['color'],
        engine_type=data['engine_type'],
        plate_type=data['plate_type']
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify({"message": "Vehicle created"}), 201

# Define other routes for GET, PUT, and DELETE operations for vehicles

# Routes for Owner
@app.route('/owners', methods=['POST'])
def create_owner():
    data = request.get_json()
    new_owner = Owner(
        name=data['name'],
        contact_details=data['contact_details'],
        address=data['address']
    )
    db.session.add(new_owner)
    db.session.commit()
    return jsonify({"message": "Owner created"}), 201


@app.route('/registrations', methods=['POST'])
def create_registration():
    data = request.get_json()
    new_registration = Registration(
        vehicle_vin=data['vehicle_vin'],
        owner_id=data['owner_id'],
        plate_number=data['plate_number'],
        registration_status=data['registration_status'],
        expiry_date=data['expiry_date']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify({"message": "Registration created"}), 201


if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    # Run the Flask app
    app.run(debug=True)
