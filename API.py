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
from flask import redirect, url_for

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
        return redirect(url_for('new_owner_form'))  # Redirect to home.html
    except Exception as e:
        return f"Error creating vehicle: {str(e)}"


from flask import redirect, url_for

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
        return redirect(url_for('new_registration_form'))  # Redirect to home.html
    except Exception as e:
        return f"Error creating owner: {str(e)}"

from flask import redirect, url_for

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
        return redirect(url_for('home'))  # Redirect to home.html
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



@app.route('/vehicles/<int:vehicle_vin>/update', methods=['GET'])
def update_vehicle_form(vehicle_vin):
    vehicle = Vehicle.query.get(vehicle_vin)
    return render_template('update_vehicle.html', vehicle=vehicle)

# Route to handle updating a vehicle
@app.route('/vehicles/<int:vehicle_vin>', methods=['POST'])
def update_vehicle(vehicle_vin):
    try:
        vehicle = Vehicle.query.get(vehicle_vin)
        data = request.form
        vehicle.make = data['make']
        vehicle.model = data['model']
        vehicle.year = data['year']
        vehicle.color = data['color']
        vehicle.engine_type = data['engine_type']
        vehicle.plate_type = data['plate_type']
        db.session.commit()
        return redirect('/data')
    except Exception as e:
        return f"Error updating vehicle: {str(e)}"

# Route to display the delete vehicle confirmation page
@app.route('/vehicles/<int:vehicle_vin>/delete', methods=['GET'])
def delete_vehicle_confirm(vehicle_vin):
    vehicle = Vehicle.query.get(vehicle_vin)
    return render_template('delete_vehicle.html', vehicle=vehicle)

@app.route('/vehicles/<int:vehicle_vin>/delete', methods=['POST'])
def delete_vehicle(vehicle_vin):
    try:
        vehicle = Vehicle.query.get(vehicle_vin)
        if vehicle is None:
            return "Vehicle not found.", 404

        db.session.delete(vehicle)
        db.session.commit()
        return redirect('/data')
    except Exception as e:
        return f"Error deleting vehicle: {str(e)}"




@app.route('/owners/<int:owner_id>/update', methods=['GET', 'POST'])
def update_owner(owner_id):
    try:
        owner = Owner.query.get(owner_id)
        if request.method == 'POST':
            data = request.form
            owner.name = data['name']
            owner.contact_details = data['contact_details']
            owner.address = data['address']
            # Update other attributes similarly
            db.session.commit()
            return redirect('/data')  # Redirect to owner list page
        else:
            return render_template('update_owner.html', owner=owner)
    except Exception as e:
        return f"Error updating owner: {str(e)}"



@app.route('/owners/<int:owner_id>/delete', methods=['GET'])
def delete_owner_confirm(owner_id):
    owner = Owner.query.get(owner_id)
    return render_template('delete_owner.html', owner=owner)



@app.route('/owners/<int:owner_id>/delete', methods=['POST'])
def delete_owner(owner_id):
    try:
        owner = Owner.query.get(owner_id)
        if owner is None:
            return "Owner not found.", 404

        db.session.delete(owner)
        db.session.commit()
        return redirect('/data')
    except Exception as e:
        return f"Error deleting owner: {str(e)}"







@app.route('/registrations/<int:registration_id>/update', methods=['GET'])
def update_registration_form(registration_id):
    registration = Registration.query.get(registration_id)
    return render_template('update_registration.html', registration=registration)

@app.route('/registrations/<int:registration_id>/update', methods=['POST'])
def update_registration(registration_id):
    try:
        registration = Registration.query.get(registration_id)
        if registration:
            data = request.form
            registration.plate_number = data.get('plate_number', registration.plate_number)
            registration.registration_status = data.get('registration_status', registration.registration_status)
            registration.expiry_date = data.get('expiry_date', registration.expiry_date)
            # Update other attributes similarly
            db.session.commit()
            return redirect('/data')
        else:
            return "Registration not found.", 404
    except Exception as e:
        return f"Error updating registration: {str(e)}"


@app.route('/registrations/<int:registration_id>/delete', methods=['GET'])
def delete_registration_confirm(registration_id):
    registration = Registration.query.get(registration_id)
    return render_template('delete_registration.html', registration=registration)

@app.route('/registrations/<int:registration_id>/delete', methods=['POST'])
def delete_registration(registration_id):
    try:
        registration = Registration.query.get(registration_id)
        if registration is None:
            return "Registration not found.", 404

        db.session.delete(registration)
        db.session.commit()
        return redirect('/data')
    except Exception as e:
        return f"Error deleting registration: {str(e)}"


@app.route('/exit', methods=['GET'])
def exit_data_view():
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)
