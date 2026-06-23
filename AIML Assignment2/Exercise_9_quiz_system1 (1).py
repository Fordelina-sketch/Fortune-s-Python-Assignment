# List of 15 questions: (question, answer, difficulty, points)
questions_data = [
    ("What is 2 + 2?", "4", "Easy", 10),
    ("Color of the sky?", "blue", "Easy", 10),
    ("Is fire hot or cold?", "hot", "Easy", 10),
    ("How many legs does a dog have?", "4", "Easy", 10),
    ("What is the name of Ugwunagbo Assistant Coordinator?", "Fortune Onwunli", "Easy", 10),
    
    ("Capital of France?", "Paris", "Medium", 20),
    ("How many hours in a day?", "24", "Medium", 20),
    ("What planet are we on?", "Earth", "Medium", 20),
    ("How many months in a year?", "12", "Medium", 20),
    ("What freezes to make ice?", "water", "Medium", 20),
    
    ("What is the square root of 64?", "8", "Hard", 30),
    ("Who wrote Romeo and Juliet?", "Shakespeare", "Hard", 30),
    ("What is H2O?", "water", "Hard", 30),
    ("First man on the moon?", "Armstrong", "Hard", 30),
    ("Largest ocean?", "Pacific", "Hard", 30)
]

def run_quiz(level):
    print(f"\nStarting the {level} Quiz!")
    score = 0
    total_possible = 0
    
    # loop through questions and pick the right level
    for q in questions_data:
        question_text = q[0]
        correct_answer = q[1]
        difficulty = q[2]
        points = q[3]
        
        if difficulty.lower() == level.lower():
            print("\nQuestion:", question_text)
            user_answer = input("Your answer: ")
            
            total_possible += points
            
            # check answer (ignoring caps)
            if user_answer.lower() == correct_answer.lower():
                print("Correct!")
                score += points
            else:
                print(f"Wrong! The answer was {correct_answer}")
                
    # final score calculation
    if total_possible > 0:
        percent = (score / total_possible) * 100
        print(f"\nQuiz Over! You scored {score} out of {total_possible} points ({percent:.1f}%).")
        
        # performance message based on percentage
        if percent == 100:
            print("Message: Perfect score! Amazing job!")
        elif percent >= 70:
            print("Message: Good job, you passed!")
        elif percent >= 50:
            print("Message: You did okay, but keep studying.")
        else:
            print("Message: Better luck next time.")
    else:
        print("No questions found for that level.")

# Test the quiz (You can change 'Easy' to 'Medium' or 'Hard' when you run it)
run_quiz("Easy")