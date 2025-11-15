Password Hashing & Salting Demo

Author: Your Name
Project Type: Web Security / Authentication Demo
Demo Type: In-Memory Database

📌 Project Overview

This project demonstrates secure password storage using hashing and salting.
Users can register, login, view all users, and search for specific users using a simple web interface.
The passwords are never stored in plain text—only hashes with unique salts are kept.

Key Learning Outcomes:

Understanding password hashing and salting

Implementing secure user authentication

Simulating a database in memory for demo purposes

✨ Features
Feature	Description
User Registration	Register with username and password
Password Hashing	Passwords hashed using bcrypt
Salting	Unique salt generated per user
Login Verification	Compares password against hash
View Database	/view-db shows all users
Search User	/search/:username returns specific user
🛠️ Tech Stack

Backend: Node.js, Express

Frontend: HTML, JavaScript

Security: bcrypt (hashing & salting)

Database: In-memory JS object (users)

📂 Project Structure
password-hashing-demo/
│
├─ public/
│   ├─ register.html
│   ├─ login.html
│
├─ images/
│   ├─ register-demo.png
│   ├─ view-db-demo.png
│
├─ server.js
├─ package.json
└─ README.md

⚙️ Setup & Usage
1️⃣ Clone Repository
git clone https://github.com/yourusername/password-hashing-demo.git
cd password-hashing-demo

2️⃣ Install Dependencies
npm install

3️⃣ Start Server
node server.js

4️⃣ Open in Browser

Register: http://localhost:3000/register.html

Login: http://localhost:3000/login.html

View All Users: http://localhost:3000/view-db

Search User: http://localhost:3000/search/<username>

📸 Demo Screenshots

Register Page

View Database

🧠 What We Learn

From this project, we understand the core principles of password security and authentication:

Password Hashing:

Converts a plain text password into an irreversible string using bcrypt.

Ensures passwords are never stored in plain text.

Salting:

Adds a unique random string to each password before hashing.

Prevents attackers from cracking passwords using precomputed tables.

Secure Verification:

During login, the entered password is hashed with the same salt and compared to the stored hash.

Authentication is successful only if the hash matches.

Safe Storage Practices:

Only hash + salt are stored, never the actual password.

Demonstrates best practices for protecting user credentials.

Authentication Flow Understanding:

How registration, login, and user verification work in a secure way.

Provides a hands-on understanding of real-world security principles in web applications.

🔍 How It Works

Registration:

User submits username and password

Server generates a salt and hashes the password

Stores hash and salt in memory

Login:

User submits credentials

Server compares input password with stored hash using bcrypt

View/Search Users:

/view-db → Shows all users

/search/:username → Returns a specific user’s hash & salt

💡 Notes

In-memory storage means data is lost on server restart

Ideal for learning and demo purposes

For production, replace with a database like MySQL or MongoDB

📖 Conclusion

This project demonstrates:

The importance of hashing and salting passwords

How authentication works in a simple web app

Safe handling of user credentials

A beginner-friendly demo ready for portfolio display
