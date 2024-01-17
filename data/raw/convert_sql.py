# Convert the raw data to SQL format
# Usage: python convert_sql.py

import pandas as pd
import sqlite3

# Read the raw data
dataframe = pd.read_csv('/Users/guttofranca/Repos/brazilian_houses_for_rent/data/raw/updated_brasilian_housing_to_rent.csv')

# Create a connection to the database
conn = sqlite3.connect('/Users/guttofranca/Repos/brazilian_houses_for_rent/data/processed/brazilian_houses.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute('''
CREATE TABLE rentals (
        id INTEGER,
        city INTEGER,
        area INTEGER,
        rooms INTEGER,
        bathroom INTEGER,
        parking_spaces INTEGER,
        floor INTEGER,
        animal INTEGER,
        furniture INTEGER,
        hoa INTEGER,
        rent_amount INTEGER,
        property_tax INTEGER,
        fire_insurance INTEGER,
        total INTEGER
    )
''')

# Insert the dataframe into the table
dataframe.to_sql('rentals', conn, if_exists='replace', index=False)

# Commit the changes
conn.commit()
conn.close()