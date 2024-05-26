FLASK API



# Vehicle Registration System

This project is a web-based application for managing vehicle registrations, owners, and registration details. It uses Flask as the web framework and SQLAlchemy for ORM (Object Relational Mapping).

## Prerequisites

- Python 3.x
- MySQL
- pip (Python package installer)

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    Create a MySQL database or import it from my repo named `registration vehicles` and configure the connection details in the `app.config['SQLALCHEMY_DATABASE_URI']` line of `app.py`.

    ```sql
    CREATE DATABASE registration_vehicles;
    ```

5. **Run the Flask application:**

    ```bash
    flask run
    ```

    The application will be available at `http://127.0.0.1:5000`.

## Usage

### Navigating the Application

1. **Home Page:**

    Navigate to `http://127.0.0.1:5000/` to access the home page. This page provides links to various forms for adding new vehicles, owners, and registrations.

2. **Adding a New Vehicle:**

    - Go to `http://127.0.0.1:5000/vehicles/new`.
    - Fill in the form with vehicle details and submit.

3. **Adding a New Owner:**

    - After adding a new vehicle, you will be redirected to add a new owner.
    - Alternatively, navigate to `http://127.0.0.1:5000/owners/new`.
    - Fill in the form with owner details and submit.

4. **Adding a New Registration:**

    - After adding a new owner, you will be redirected to add a new registration.
    - Alternatively, navigate to `http://127.0.0.1:5000/registrations/new`.
    - Fill in the form with registration details and submit.

### Viewing Data

- Go to `http://127.0.0.1:5000/data` to view all vehicles, owners, and registrations.

### Updating Data

1. **Updating a Vehicle:**

    - Navigate to `http://127.0.0.1:5000/vehicles/<vehicle_vin>/update` where `<vehicle_vin>` is the VIN of the vehicle you want to update.
    - Fill in the form with the updated vehicle details and submit.

2. **Updating an Owner:**

    - Navigate to `http://127.0.0.1:5000/owners/<owner_id>/update` where `<owner_id>` is the ID of the owner you want to update.
    - Fill in the form with the updated owner details and submit.

3. **Updating a Registration:**

    - Navigate to `http://127.0.0.1:5000/registrations/<registration_id>/update` where `<registration_id>` is the ID of the registration you want to update.
    - Fill in the form with the updated registration details and submit.

### Deleting Data

1. **Deleting a Vehicle:**

    - Navigate to `http://127.0.0.1:5000/vehicles/<vehicle_vin>/delete` where `<vehicle_vin>` is the VIN of the vehicle you want to delete.
    - Confirm deletion.

2. **Deleting an Owner:**

    - Navigate to `http://127.0.0.1:5000/owners/<owner_id>/delete` where `<owner_id>` is the ID of the owner you want to delete.
    - Confirm deletion.

3. **Deleting a Registration:**

    - Navigate to `http://127.0.0.1:5000/registrations/<registration_id>/delete` where `<registration_id>` is the ID of the registration you want to delete.
    - Confirm deletion.

### Exiting Data View

- To return to the home page from the data view, navigate to `http://127.0.0.1:5000/exit`.

## Error Handling

If an error occurs during any operation (creation, update, or deletion), an error message will be displayed on the screen.

