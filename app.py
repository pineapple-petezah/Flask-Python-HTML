from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Mock database
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    fullname = request.form['fullname']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    dob = request.form['dob']
    
    if email in users:
        return "User already exists!"
    users[email] = {
        'fullname': fullname,
        'password': password,
        'phone': phone,
        'dob': dob
    }
    return "Signup successful! You can now login.<br><a href='https://codewithbismillah.vercel.app/'>Go back</a>"

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if email in users and users[email]['password'] == password:
        return f"Login successful! Welcome, {users[email]['fullname']}! Happy coding <a href='https://codewithbismillah.vercel.app/'>Home</a>"
    return "Invalid email or password."

if __name__ == '__main__':
    app.run(debug=True)
