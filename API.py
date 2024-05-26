from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/registration vehicles'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    vehicle_vin = db.Column(db.Integer, primary_key=True, autoincrement=True)
    make = db.Column(db.String(45), nullable=False)
    model = db.Column(db.String(45), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(45), nullable=False)
    engine_type = db.Column(db.String(45), nullable=False)
    plate_type = db.Column(db.String(45), nullable=False)

class Owner(db.Model):
    __tablename__ = 'owner'
    owner_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    contact_details = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(245), nullable=False)

class Registration(db.Model):
    __tablename__ = 'registration'
    registration_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plate_number = db.Column(db.String(45), nullable=False)
    registration_status = db.Column(db.String(45), nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)

# Home route to navigate to forms
@app.route('/')
def home():
    return render_template('home.html')

# Route to display the new vehicle form
@app.route('/vehicles/new', methods=['GET'])
def new_vehicle_form():
    return render_template('new_vehicle_form.html')

# Route to handle the new vehicle form submission
@app.route('/vehicles', methods=['POST'])
def create_vehicle():
    try:
        data = request.form
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
        return redirect('/vehicles/new')
    except Exception as e:
        return f"Error creating vehicle: {str(e)}"

# Route to display the new owner form
@app.route('/owners/new', methods=['GET'])
def new_owner_form():
    return render_template('new_owner_form.html')

# Route to handle the new owner form submission
@app.route('/owners', methods=['POST'])
def create_owner():
    try:
        data = request.form
        new_owner = Owner(
            owner_id=data['owner_id'],
            name=data['name'],
            contact_details=data['contact_details'],
            address=data['address']
        )
        db.session.add(new_owner)
        db.session.commit()
        return redirect('/owners/new')
    except Exception as e:
        return f"Error creating owner: {str(e)}"

# Route to display the new registration form
@app.route('/registrations/new', methods=['GET'])
def new_registration_form():
    return render_template('new_registration_form.html')

# Route to handle the new registration form submission
@app.route('/registrations', methods=['POST'])
def create_registration():
    try:
        data = request.form
        new_registration = Registration(
            registration_id=data['registration_id'],
            plate_number=data['plate_number'],
            registration_status=data['registration_status'],
            expiry_date=data['expiry_date']
        )
        db.session.add(new_registration)
        db.session.commit()
        return redirect('/registrations/new')
    except Exception as e:
        return f"Error creating registration: {str(e)}"


@app.route('/data', methods=['GET'])
def show_data():
    try:
        owners = Owner.query.all()
        vehicles = Vehicle.query.all()
        registrations = Registration.query.all()
        return render_template('data.html', owners=owners, vehicles=vehicles, registrations=registrations)
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
        return f"Error fetching data: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
