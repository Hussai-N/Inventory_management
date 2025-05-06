# Flask Inventory Management System

This is a basic inventory management system built with Flask, SQLAlchemy, and WTForms. It allows users to manage products, track product movements between locations, and generate inventory balance reports.

## Features

- Add, view, and edit products
- Track product movement between locations
- View inventory balance by product and location
- SQLite database for storage
- Bootstrap-styled HTML templates

## Project Structure

/project-root
│
├── app.py # Main Flask application
├── models.py # SQLAlchemy models for Product, Location, Movement
├── forms.py # Flask-WTF form definitions
├── inventory.db # SQLite database (auto-generated)
│
├── templates/
│ ├── layout.html
│ ├── index.html
│ ├── product_form.html
│ ├── view_products.html
│ ├── movement_form.html
│ └── report.html
│
├── .env # Environment variables (SECRET_KEY)

## Usage

Visit /product/add to add a product

Visit /products to view/edit products

Visit /movement/add to track product movements

Visit /report/balance to see current inventory status

## Tech Stack

Flask - Backend framework

Flask-WTF - Form validation

SQLite - Database

SQLAlchemy - ORM

Bootstrap - Frontend styling
