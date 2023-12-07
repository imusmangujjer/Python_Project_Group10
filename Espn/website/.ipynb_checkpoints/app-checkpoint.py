from flask import Flask, render_template, g, request, flash
import sqlite3
import pathlib
from pathlib import Path
import os


app = Flask(__name__)
app.secret_key = 'manbearpig_MD12'  # Set a secret key for Flask sessions

#base_path = pathlib.Path().cwd()

base_path = Path(__file__).resolve().parent  # Getting the parent directory of the current script
db_folder = base_path.parent / 'Database'
db_name = "cricket_records.db"
file_path = db_folder / db_name

# Get the absolute path to the database file
database_path = file_path  

# Function to get the SQLite connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database_path)
    return db

# Close the SQLite connection at the end of each request
@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data')
def data():
    conn = get_db()
    cursor = conn.cursor()

    # Fetch data from the database
    cursor.execute('SELECT * FROM batting_record LIMIT 15')
    batting_data = cursor.fetchall()
    flash(batting_data)

    cursor.execute('SELECT * FROM bowling_record LIMIT 15')
    bowling_data = cursor.fetchall()
    flash(bowling_data)

    conn.close()

    return render_template('data.html', batting_data=batting_data, bowling_data=bowling_data)

if __name__ == '__main__':
    app.run(debug=True)
