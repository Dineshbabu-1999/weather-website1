const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

// Middleware to serve static files
app.use(express.static(path.join(__dirname, "public")));

// Route for the index page
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "index.html"));
});

// Route for the weather page
app.get("/weather", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "weather.html"));
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});