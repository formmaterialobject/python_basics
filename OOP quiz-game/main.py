from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain 

question_bank = []

for each_question in question_data:
    question_text = each_question.get("text")
    question_answer = each_question.get("answer")
    
    question_bank.append(Question(question_text, question_answer))



quiz = QuizzBrain(question_bank) #Objekt "quiz" wird erstellt/ Objekt ist eine Instanz der Klasse QuizzBrain

while quiz.still_has_questions():
    quiz.next_question()
   

print(f"End of Game. Your final score: {quiz.score} of {quiz.question_number}")
