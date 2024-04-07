from question_model import Question
from data import question_data
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user = input(f"Q {self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user, current_question.answer)

    def check_answer(self, user , correct_answer):
        if user.lower() == correct_answer.lower():
            print("YouR Answer is !!!! CORRECT !!!! ")
            self.score += 1
        else:
            print("YouR Answer is !!! WRONG !!! ")
            print(f"The Correct Answer is : {correct_answer}")
        print(f"your Current Score Is {self.score}/{self.question_number}.")
        print("\n\n")