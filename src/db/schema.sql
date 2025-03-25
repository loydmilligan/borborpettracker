-- SQLite Database Schema Fragment for BilboPetTracker
-- INTENTIONALLY INCOMPLETE - Part of modular schema implementation

-- Enable foreign key support
PRAGMA foreign_keys = ON;

-- Placeholder for future table definitions
-- This fragment represents the initial database configuration

-- Pet Profile Table Definition
-- INTENTIONALLY INCOMPLETE - Part of modular schema implementation

-- Pet Profile Table
CREATE TABLE IF NOT EXISTS pet_profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    breed TEXT,
    birth_date DATE,
    sex TEXT CHECK(sex IN ('Male', 'Female', 'Unknown')),
    microchip_number TEXT UNIQUE,
    color TEXT,
    current_status TEXT CHECK(current_status IN ('Active', 'Deceased', 'Rehomed', 'Missing'))
);

-- Weight History Table Definition
-- INTENTIONALLY INCOMPLETE - Part of modular schema implementation

-- Weight History Table
CREATE TABLE IF NOT EXISTS weight_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pet_id INTEGER NOT NULL,
    weight_kg REAL NOT NULL,
    measured_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Food Intake Table Definition
-- INTENTIONALLY INCOMPLETE - Part of modular schema implementation

-- Food Intake Table
CREATE TABLE IF NOT EXISTS food_intake (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pet_id INTEGER NOT NULL,
    food_name TEXT NOT NULL,
    amount_grams REAL NOT NULL,
    meal_type TEXT CHECK(meal_type IN ('Breakfast', 'Lunch', 'Dinner', 'Snack')),
    fed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Exercise Records Table Definition
-- INTENTIONALLY INCOMPLETE - Part of modular schema implementation

-- Exercise Records Table
CREATE TABLE IF NOT EXISTS exercise_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pet_id INTEGER NOT NULL,
    exercise_type TEXT NOT NULL,
    duration_minutes REAL NOT NULL,
    intensity TEXT CHECK(intensity IN ('Low', 'Moderate', 'High')),
    exercised_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    location TEXT,
    notes TEXT
);

-- Medical history table for tracking pet medical records
CREATE TABLE IF NOT EXISTS medical_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pet_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    diagnosis TEXT,
    treatment TEXT,
    notes TEXT,
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);