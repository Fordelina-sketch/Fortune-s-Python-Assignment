# Raw contact list with 15 names. Notice the messy spaces and capitalization.
raw_contacts = [
    "Emeka", " emeka ", "Blessing", "Bisi", "bisi", 
    "Chinedu", "Chika", " chisom", "David", "Esther", 
    "Femi", "FEMI ", "Gabriel", "Henry", "Ijeoma", 
    "Jude", "Kelechi", "Musa", "Nneka", "nneka  "
]

# We need a set to track duplicates and lists to store the final results
seen_names = set()
cleaned_contacts = []
duplicate_report = []

# Loop through each name in the raw list
for name in raw_contacts:
    # Remove empty spaces at the beginning and end
    clean_name = name.strip()
    # Make the first letter big and the rest small (e.g., "femi" -> "Femi")
    clean_name = clean_name.title()
    
    # Check if we already have this name in our set
    if clean_name in seen_names:
        duplicate_report.append(clean_name)
    else:
        # If it's new, add it to our set and our final clean list
        seen_names.add(clean_name)
        cleaned_contacts.append(clean_name)

# Print the results
print("--- CLEANED CONTACT LIST ---")
for contact in cleaned_contacts:
    print("-", contact)

print("\n--- DUPLICATE REPORT ---")
print(f"Found {len(duplicate_report)} duplicates.")
print("Names that were repeated:", duplicate_report)