# CSV Data Analysis Web Application

## Overview

This Django-based web application allows users to upload CSV files, perform data analysis using pandas and numpy, and display results and visualizations on a web interface. Users can handle missing values in their data using various strategies and view histograms of numerical columns.

## Features

- **CSV File Upload**: Users can upload CSV files for analysis.
- **Data Analysis**: Displays basic statistics and identifies missing values.
- **Missing Values Handling**: Options to drop rows, fill with mean/median, or use forward/backward fill.
- **Data Visualization**: Generates and displays histograms for numerical columns.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django
- Pandas
- Matplotlib
- Seaborn

### Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/Vedansh1857/django-data-visualizer.git
   cd django-data-visualizer

2. **Create and Activate a Virtual Environment**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt

4. **Ensure "requirements.txt" contains:**

   ```sh
   Django>=4.0
   pandas>=1.5.0
   matplotlib>=3.5.0
   seaborn>=0.12.0

5. **Apply Database Migrations**

   ```sh
   python manage.py migrate

6. **Run the Development Server**

   ```sh
   python manage.py runserver

7. **Access the Application**

   Open your web browser and navigate to 'http://127.0.0.1:8000/csv/upload/'.


## Project Structure

   ```
myproject/
├── myproject/ # Django project directory containing settings and configuration
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── csv_analysis/ # Django app directory for handling CSV files and data analysis
│ ├── migrations/ # Database migrations for the app
│ ├── templates/
│ │ └── csv_analysis/
│ │ ├── upload.html # HTML template for file upload page
│ │ └── analyze.html # HTML template for data analysis page
│ ├── static/
│ │ └── histograms/ # Directory for static files such as histogram images
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py # Contains forms for file upload
│ ├── models.py # Contains models for storing uploaded files
│ ├── tests.py
│ └── views.py # Contains logic for file upload, data processing, and visualization
├── static/ # Static files directory
│ └── histograms/ # Directory for static files such as histogram images
├── manage.py # Django's command-line utility for administrative tasks
└── requirements.txt # List of dependencies to be installed with pip

