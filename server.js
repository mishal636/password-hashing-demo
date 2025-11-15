const express = require("express");
const bodyParser = require("body-parser");
const bcrypt = require("bcrypt");
const path = require("path");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static("public"));

const users = {}; // simulated database

// Register API
app.post("/api/register", async (req, res) => {
  const { username, password } = req.body;
  if (users[username]) return res.json({ success: false, message: "User already exists!" });

  const saltRounds = 10;
  const salt = await bcrypt.genSalt(saltRounds);
  const hash = await bcrypt.hash(password, salt);

  users[username] = { hash, salt };

  res.json({
    success: true,
    password,
    salt,
    hash,
    message: "User registered successfully!"
  });
});

// Login API
app.post("/api/login", async (req, res) => {
  const { username, password } = req.body;
  const user = users[username];
  if (!user) return res.json({ success: false, message: "User not found!" });

  const match = await bcrypt.compare(password, user.hash);
  if (match) {
    res.json({
      success: true,
      message: "Login successful!",
      password,
      salt: user.salt,
      hash: user.hash
    });
  } else {
    res.json({ success: false, message: "Incorrect password!" });
  }
});

app.listen(3000, () => console.log("Server running on http://localhost:3000"));
