# 🔐 Password Hashing & Salting Demo  

![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)  

**Author:** Mishal Mohammed 
**Project Type:** Web Security / Authentication Demo  
**Demo Type:** In-Memory Database  

---

## 📌 Project Overview

This project demonstrates **secure password storage** using **hashing and salting**.  

Users can:  

- **Register** a new account  
- **Login** securely  
- **View all users** (hashes only)  
- **Search** for a specific user  

> Passwords are **never stored in plain text**; only hashed passwords with unique salts are saved.  

**Key Learning Outcomes:**  

- Understanding **password hashing and salting**  
- Implementing **secure authentication**  
- Simulating a **database in memory** for demo purposes  

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **User Registration** | Register with username and password |
| **Password Hashing** | Passwords hashed using bcrypt |
| **Salting** | Unique salt generated per user |
| **Login Verification** | Compares entered password against stored hash |
| **View Database** | `/view-db` shows all users with hash & salt |
| **Search User** | `/search/:username` returns specific user data |

---

## 🛠️ Tech Stack

- **Backend:** Node.js, Express  
- **Frontend:** HTML, JavaScript  
- **Security:** bcrypt (hashing & salting)  
- **Database:** In-memory JavaScript object  

---

## 📂 Project Structure

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

## ⚙️ Setup & Usage
# 1️⃣ Clone Repository
git clone https://github.com/yourusername/password-hashing-demo.git
cd password-hashing-demo

# 2️⃣ Install Dependencies
npm install

# 3️⃣ Start Server
node server.js

# 4️⃣ Open in Browser

Register: http://localhost:3000/register.html

Login: http://localhost:3000/login.html

View All Users: http://localhost:3000/view-db

Search User: http://localhost:3000/search/<username>

## 📸 Demo Screenshots

Register Page:

View Database:

## 🧠 What We Learn

Password Hashing: Converts a plain text password into an irreversible string using bcrypt.

Salting: Adds a unique random string to each password before hashing, preventing rainbow table attacks.

Secure Verification: During login, the entered password is hashed with the same salt and compared to the stored hash.

Safe Storage: Only hash + salt are stored, never the actual password.

Authentication Flow Understanding: Shows how registration, login, and verification work securely.

## 🔍 How It Works

Registration

User submits username and password

Server generates a salt and hashes the password

Stores hash + salt in memory

Login

User submits credentials

Server compares input password with stored hash using bcrypt

View/Search Users

/view-db → Shows all users

/search/:username → Returns specific user’s hash & salt

## 💡 Notes

In-memory storage → data is lost when server restarts

Ideal for learning and demo purposes

For production, replace with a database like MySQL or MongoDB

## 📖 Conclusion

This project demonstrates:

Importance of hashing and salting passwords

How authentication works in a simple web app

Safe handling of user credentials

Beginner-friendly demo ready for portfolio showcase
