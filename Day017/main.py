from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    new_question = Question(data["question"], data["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You're completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")