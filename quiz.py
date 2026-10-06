questions = [
    {
        "question": "Which language is used for Python programming?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which data type stores a collection of key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["A. get()", "B. input()", "C. scan()", "D. read()"],
        "answer": "B"
    }
]


def play_quiz():
    score = 0

    print("\n===== PYTHON QUIZ =====")
    print("Answer each question by entering A, B, C or D.")

    for number, item in enumerate(questions, 1):
        print(f"\nQuestion {number}: {item['question']}")

        for option in item["options"]:
            print(option)

        while True:
            user_answer = input("Your answer: ").strip().upper()

            if user_answer in ["A", "B", "C", "D"]:
                break

            print("Invalid answer. Please enter A, B, C or D.")

        if user_answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {item['answer']}.")

    print("\n===== QUIZ COMPLETED =====")
    print(f"Your score: {score}/{len(questions)}")

    if score == len(questions):
        print("Excellent! Perfect score!")

    elif score >= 3:
        print("Good job! You performed well.")

    else:
        print("Keep practicing and try again!")


def main():
    print("===== PYTHON QUIZ APPLICATION =====")

    while True:
        play_quiz()

        choice = input("\nDo you want to play again? (y/n): ").strip().lower()

        if choice == "y":
            print("\nStarting a new quiz...")

        elif choice == "n":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Quiz ended.")
            break


main()
