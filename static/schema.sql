-- Seasonal flavor offerings
CREATE TABLE IF NOT EXISTS flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    is_seasonal BOOLEAN NOT NULL,
    allergens TEXT
);

-- Ingredient inventory
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT NOT NULL UNIQUE,
    quantity INTEGER NOT NULL
);

-- Customer flavor suggestions and allergy concerns
CREATE TABLE IF NOT EXISTS suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    flavor_suggestion TEXT,
    allergy_concern TEXT
);
