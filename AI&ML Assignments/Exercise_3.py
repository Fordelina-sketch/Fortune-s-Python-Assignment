# Create a list containing tuples of 8 buildings
# Format: (building_name, type, year_built)
street_buildings = [
    ("Nnamdi's House", "Residential", 1998),
    ("Crunchies", "Commercial", 2015),
    ("Grace Pharmacy", "Commercial", 2021),
    ("Fulfilment", "School", 2005),
    ("St. Peter's Church", "Religious", 1990),
    ("New Jerusalem Estate", "Residential", 2010),
    ("West swiss", "Hotel", 2005),
    ("Old Post Office", "Government", 1970)
]

# Variables to keep track of our findings
oldest_year = 2026 # Start with the current year
oldest_building = ""
unique_types = set() # Empty set to hold building types
buildings_after_2000 = []
total_age = 0
current_year = 2026

# Loop through every building on the street
for name, building_type, year in street_buildings:
    
    # 1. Find the oldest building
    if year < oldest_year:
        oldest_year = year
        oldest_building = name
        
    # 2. Add the building type to our set (sets automatically ignore duplicates)
    unique_types.add(building_type)
    
    # 3. Check if built after 2000
    if year > 2000:
        buildings_after_2000.append(name)
        
    # 4. Calculate age and add to total for our average later
    age = current_year - year
    total_age = total_age + age

# Calculate average age
number_of_buildings = len(street_buildings)
average_age = total_age / number_of_buildings

# Print the final report
print("--- STREET DATA REPORT ---")
print("Oldest Building:", oldest_building, f"(Built in {oldest_year})")
print("Unique Building Types:", unique_types)
print("Buildings Built After 2000:", buildings_after_2000)
print("Average Age of Buildings:", average_age, "years")
