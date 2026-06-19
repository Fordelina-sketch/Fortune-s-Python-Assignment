# Define all students in the class
all_students = {"Fortune", "Beauty", "Chinedu", "Dapo", "Efe", "Felix", "Gloria", "Helen", "Ijeoma", "Jude"}

# Define who came on which day
monday_attendance = {"Fortune", "Beauty", "Chinedu", "Efe", "Helen", "Ijeoma"}
tuesday_attendance = {"Fortune", "Beauty", "Dapo", "Efe", "Gloria", "Helen", "Jude"}
wednesday_attendance = {"Fortune", "Chinedu", "Efe", "Helen", "Ijeoma", "Felix"}

# 1. Who attended all 3 days (Intersection: names in Mon AND Tue AND Wed)
attended_all = monday_attendance.intersection(tuesday_attendance).intersection(wednesday_attendance)

# 2. Who missed at least one day (Difference: all students MINUS the perfect attendees)
missed_some = all_students - attended_all

# 3. Who only came once
# First, figure out who came ONLY on specific days
only_monday = monday_attendance - tuesday_attendance - wednesday_attendance
only_tuesday = tuesday_attendance - monday_attendance - wednesday_attendance
only_wednesday = wednesday_attendance - monday_attendance - tuesday_attendance

# Then combine them together (Union)
came_once = only_monday.union(only_tuesday).union(only_wednesday)

# 4. Who never attended at all
# Combine all attendance first
everyone_who_came = monday_attendance.union(tuesday_attendance).union(wednesday_attendance)
# Subtract them from the class roster
never_came = all_students - everyone_who_came

# Print the results
print("--- ATTENDANCE TRACKER ---")
print("Attended all 3 days:", attended_all)
print("Missed at least one day:", missed_some)
print("Only came exactly once:", came_once)
print("Never attended at all:", never_came)