class QuizzBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0 
 
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list) #True or False
    
    
    def next_question(self):
        current_question = self.question_list[self.question_number] 
        self.question_number += 1
       
        user_answer = input(f"Q.{self.question_number}: {current_question.text} True or False? ")
        self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("This is right.")
            self.score += 1
            
        else:
            print("Wrong.")
        print(f"Your current Score: {self.score}/{self.question_number}")
        
        
 
        