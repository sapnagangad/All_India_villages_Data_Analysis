
// Import  libraries

const express = require('express');
const mysql = require('mysql2');

// for open package
const open = (...args) => import('open').then(module => module.default(...args));

const app = express();


// My sql connecion

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'mysql',
    database: 'village_db'
});

db.connect((err) => {
    if (err) {
        console.log("Database Error:", err);
    } else {
        console.log("MySQL Connected");

        // Start server only after DB connected
        app.listen(3000, () => {
            console.log("Server running on port 3000");

            // Auto open browser
            open('http://localhost:3000/villages');  // here is your browser server link
        });
    }
});


// ROUTES :-
// Home route
app.get('/', (req, res) => {
    res.send("API is running ");
});


// Get villages (limit for villages)
app.get('/villages', (req, res) => {
    db.query("SELECT * FROM villages LIMIT 10", (err, result) => {
        if (err) {
            res.status(500).send(err);
        } else {
            res.json(result);
        }
    });
});


// Get all states (n0 limit in states)
app.get('/states', (req, res) => {
    db.query("SELECT DISTINCT state_name FROM villages", (err, result) => {
        if (err) {
            res.status(500).send(err);
        } else {
            res.json(result);
        }
    });
});


// Get districts by state (no limits for district)
app.get('/districts/:state', (req, res) => {
    const state = req.params.state;

    db.query(
        "SELECT DISTINCT district_name FROM villages WHERE state_name = ?",
        [state],
        (err, result) => {
            if (err) {
                res.status(500).send(err);
            } else {
                res.json(result);
            }
        }
    );
});


// For Searching villages
app.get('/search/:name', (req, res) => {
    const name = req.params.name;

    db.query(
        "SELECT * FROM villages WHERE village_name LIKE ? LIMIT 10",
        [`%${name}%`],
        (err, result) => {
            if (err) {
                res.status(500).send(err);
            } else {
                res.json(result);
            }
        }
    );
});