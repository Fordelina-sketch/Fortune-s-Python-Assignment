# calculate the average of a list of numbers
def calculate_average(scores_list):
    total = 0
    for score in scores_list:
        total += score
    return total / len(scores_list)

# get the letter grade using simple if-elif
def get_grade(average):
    if average >= 90:
        return "A - Excellent"
    elif average >= 80:
        return "B - Very Good"
    elif average >= 70:
        return "C - Good"
    elif average >= 60:
        return "D - Pass"
    else:
        return "F - Fail"

# process students and rank them without built-in sort
def rank_students(student_data):
    results = []
    
    # get averages and grades for everyone
    for data in student_data:
        name = data[0]
        scores = data[1]
        avg = calculate_average(scores)
        grade = get_grade(avg)
        
        # add to our results list
        results.append([name, avg, grade])
        
    # simple bubble sort to rank them highest to lowest (descending)
    n = len(results)
    for i in range(n):
        for j in range(0, n - i - 1):
            # check the average (index 1)
            if results[j][1] < results[j+1][1]:
                # swap places
                temp = results[j]
                results[j] = results[j+1]
                results[j+1] = temp
                
    # print the final table
    print("Pos | Name       | Average | Grade")
    print("-" * 40)
    pos = 1
    for student in results:
        print(f"{pos}   | {student[0]:<10} | {student[1]:.2f}   | {student[2]}")
        pos += 1

# Test the code
students = [
    ("John", [85, 90, 88, 92]),
    ("Mary", [70, 75, 68, 72]),
    ("Sam", [95, 98, 99, 94]),
    ("Anna", [60, 65, 58, 62]),
    ("Paul", [80, 82, 85, 88])
]

rank_students(students)