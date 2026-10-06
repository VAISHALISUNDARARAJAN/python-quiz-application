# Python Quiz Application

A beginner-friendly multiple-choice quiz application developed using Python.

## Features

- Contains 5 multiple-choice questions
- Displays questions one at a time
- Accepts answers from the user
- Checks answers automatically
- Shows correct and incorrect feedback
- Keeps track of the score
- Displays the final score
- Shows a simple performance message
- Allows the user to replay the quiz
- Validates user input
- Uses Python lists and dictionaries to store questions and answers

## Technologies Used

- Python

## Question Format

Each question is stored as a Python dictionary containing:

- Question text
- Four answer options
- Correct answer

All questions are stored inside a Python list.

## Scoring Rules

- Each correct answer gives 1 point.
- Incorrect answers give 0 points.
- The final score is displayed out of 5.

## Performance Message

- 5/5: Excellent! Perfect score!
- 3/5 or 4/5: Good job! You performed well.
- 0/5, 1/5 or 2/5: Keep practicing and try again!

## How to Run

1. Make sure Python is installed on your computer.
2. Open `quiz.py` using Python IDLE or any Python IDE.
3. Run the program.
4. Read each question and select A, B, C or D.
5. View the final score and performance message.
6. Choose whether to play the quiz again.

## Example

```text
===== PYTHON QUIZ APPLICATION =====

===== PYTHON QUIZ =====
Answer each question by entering A, B, C or D.

Question 1: Which language is used for Python programming?
A. Python
B. HTML
C. CSS
D. SQL

Your answer: A
Correct!

===== QUIZ COMPLETED =====
Your score: 5/5
Excellent! Perfect score!

Error Handling
The application validates the user's answer.
If the user enters something other than A, B, C or D, the program asks the user to enter a valid answer.
Project Structure
python-quiz-application/
│
├── quiz.py
├── README.md
└── screenshots/
    ├── question.png
    ├── correct-answer.png
    ├── wrong-answer.png
    └── final-score.png
Demo Screenshots
The screenshots folder contains examples of the quiz questions, correct and incorrect answers, and the final score.
