from flask import Flask, render_template, request, redirect, flash
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# SQLite DB Setup
conn = sqlite3.connect('submissions.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    message TEXT,
    submitted_at TEXT
)
''')
conn.commit()
conn.close()

@app.route('/')
def home():
    log_visit('/')
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    log_visit('/contact')
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        save_to_db(name, email, message)
        flash('Thank you! Your message has been submitted.', 'success')
        return redirect('/contact')
    return render_template('contact.html')

def save_to_db(name, email, message):
    conn = sqlite3.connect('submissions.db')
    c = conn.cursor()
    c.execute('INSERT INTO contacts (name, email, message, submitted_at) VALUES (?, ?, ?, ?)',
              (name, email, message, datetime.now()))
    conn.commit()
    conn.close()

def log_visit(route):
    with open('logs/visits.log', 'a') as f:
        f.write(f"{datetime.now()} - Visited {route}\n")


@app.route('/view-log')
def view_log():
    with open('logs/visits.log') as f:
        content = f.read()
    return f"<pre>{content}</pre>"


@app.route('/submissions')
def view_submissions():
    conn = sqlite3.connect('submissions.db')
    c = conn.cursor()
    c.execute("SELECT name, email, message, submitted_at FROM contacts ORDER BY submitted_at DESC")
    rows = c.fetchall()
    conn.close()

    html = "<h2 class='mt-3'>📋 Form Submissions</h2><ul class='list-group'>"
    for row in rows:
        html += f"<li class='list-group-item'><strong>{row[0]}</strong> ({row[1]})<br>{row[2]}<br><em>{row[3]}</em></li>"
    html += "</ul>"
    return html


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
