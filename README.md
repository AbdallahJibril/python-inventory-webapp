# Project Version 2 - Web-Based Product and Bill Management System

## Overview
This repository contains the second version of the product and bill management system. It upgrades the original console-based application into a dynamic web-based interface using the Flask framework. The backend architecture follows Object-Oriented Programming (OOP) principles and utilizes the Pandas library for data persistence via CSV files. The core backend logic, routing, and data handling were independently developed, while the frontend HTML templates were implemented with the assistance of artificial intelligence.

## Technical Stack
- Backend: Python, Flask, Object-Oriented Programming (OOP)
- Data Persistence: Pandas, CSV storage
- Frontend: HTML templates using Jinja2 inheritance, CSS, (frontend assisted by AI)

## Project Structure and Components
- app.py: Core Flask web application handling routing, requests, sessions, and flash messages.
- product_manager.py: Manages business operations such as adding, viewing, updating, and deleting products.
- file_manager.py: Handles reading, writing, and updating records using Pandas DataFrames and CSV files.
- product.py: Object-Oriented model representing individual product attributes and automatic total calculations.
- Templates: Jinja2 HTML templates handling layouts, product tables, choice selection forms, product addition, and update workflows.

## Web Routes and Endpoints
- /: Home route displaying main operational choices.
- /inputs: Directs user actions to add, view, update, or delete products.
- /add: Processes new product creation with validation for existing names.
- /name_update, /types_update, /type_N_P_Q: Multi-step modification routes to update product names, prices, or quantities.
- /Delete: Handles product removal.

## Installation and Setup
1. Clone the repository and switch to the web branch:
   git clone <https://github.com/AbdallahJibril/python-inventory-webapp.git>
   git checkout web-version

2. Install the required dependencies (Flask and Pandas):
   pip install flask pandas

3. Run the application:
   python app.py

4. Open your web browser and navigate to the local server address provided in the terminal.
