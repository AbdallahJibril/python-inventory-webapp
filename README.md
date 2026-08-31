# Project Version 1 - Console-Based Product and Bill Management System

## Overview
This repository contains the first version of the product and bill management system, built to run directly in the command-line interface (Terminal). It provides a robust console-based environment to manage product inventory, calculate costs, generate bills, and save data securely using local files.

## Technical Stack
- Programming Language: Python
- Data Processing & Persistence: Pandas, CSV and text file I/O operations
- Architecture: Procedural / Script-based logic designed for efficient command-line execution

## Project Structure and Components
- Main Application Script: Handles the interactive command-line menu, user inputs, and operational flow.
- Data Management: Handles reading and writing structured product and billing data to local CSV and text files.
- Bill Calculation Logic: Automatically computes item totals, quantities, prices, and final bill summaries.

## Core Features
- Add, update, and manage product lists dynamically through the terminal.
- Automated calculation of total costs and generation of detailed bills.
- Permanent data storage using CSV and text files.

## Installation and Setup
1. Clone the repository and switch to the main branch:
   git clone <repository-url>
   git checkout main

2. Install the required dependencies (Pandas):
   pip install pandas

3. Run the application:
   python main.py
