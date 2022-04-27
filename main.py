from typing_extensions import Self
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

def question():
    print("Hello! Welcome to this quiz")
    input(str("Enter your name: "))
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    
    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()


    print("You are done")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")

print(question())  