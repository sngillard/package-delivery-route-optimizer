# Load package data from CSV into the hash table

import csv
from hash_table import HashTable
from package import Package

# Create a new hash table instance
package_hash = HashTable()

# Load the package data from CSV
def load_packages(filename):
    with open(filename, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader) # Skip header row
        for row in csv_reader:
            # Get information from each row
            if not row or not row[0].strip().isdigit(): # Skip empty rows
                continue
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            special_notes = row[7] if len(row) > 7 else ""

            # Create new Package object
            package = Package(package_id, address, city, state, zip_code, deadline, weight, special_notes)

            # Insert Package object into HashTable
            package_hash.add(package_id, package)

# Call the load_package_data function
if __name__ == "__main__":
    load_packages('data/packages.csv')