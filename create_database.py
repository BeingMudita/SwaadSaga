import sqlite3
import pandas as pd

# Step 1: Connect to the SQLite database (it will create if it doesn't exist)
conn = sqlite3.connect('food_recommendations.db')
cursor = conn.cursor()

# Step 2: Create the food table (if not exists)
cursor.execute('''
CREATE TABLE IF NOT EXISTS food (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    image_url TEXT,
    description TEXT,
    cuisine TEXT,
    course TEXT,
    diet TEXT,
    prep_time TEXT,
    ingredients TEXT,
    instructions TEXT
)
''')

# Step 3: Load the data from the CSV file
df = pd.read_csv('indian_food_recipes.csv')

# Step 4: Insert data into the food table
for index, row in df.iterrows():
    cursor.execute('''
    INSERT INTO food (name, image_url, description, cuisine, course, diet, prep_time, ingredients, instructions)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (row['name'], row['image_url'], row['description'], row['cuisine'], row['course'], row['diet'],
          row['prep_time'], row['ingredients'], row['instructions']))

# Commit and close the connection
conn.commit()
conn.close()

print("Database created and data inserted successfully!")
