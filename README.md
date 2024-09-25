# coffeenest

Welcome to the Coffenest! This Django application is designed to manage a coffee shop's products, orders, and users efficiently.

## Requirements

- **PostgreSQL** (Make sure it's installed and running)
- **Python 3.12**

## Installation Guide

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository

Clone the project repository from GitHub to your local machine:

```bash
git clone https://github.com/castilloxavie/coffenest.git coffenest
cd coffenest
```

### 2. Create a Virtual Environment
Create a new virtual environment for the project:

```bash
sudo apt update
sudo apt install python3.12
sudo apt install python3.12-venv
python3.12 -m venv myenv
source myenv/bin/activate
python --version
deactivate
```

### 3. Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root directory and add your environment variables:

```bash
cp .env.example .env
```
Edit the `.env` file to include your database credentials and other required settings.

### 5. Set Up the Database

Create a new PostgreSQL database and update the `DATABASE_URL` in the `.env` file to match
your database credentials.

```bash
psql -U postgres -c "CREATE DATABASE coffeenest;"
python manage.py migrate
```

### 6. Create a Superuser
Create a superuser for the Django admin interface:

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
Run the development server:

```bash
./manage.py runserver
```

Access the project by navigating to http://127.0.0.1:8000 in your web browser.

#### Project Structure
**products:** Handles everything related to coffee products.
**users:** Manages user authentication and profiles.
**orders:** Manages customer orders.

