import csv
import random

class quiz_master:
    def __init__(self):
        self.quest_list = []
        self.answer = {}
        self.quiz_no = 0
        self.quiz()
        
    def quiz(self, start=0, no=0):
        number = 20
        if self.quiz_no<number:
            if start==0:
                with open('quiz.csv', 'r') as file:
                    questions = csv.reader(file)
                    for question in questions:
                        self.quest_list.append(question)
                    shuffled_question = random.shuffle(self.quest_list)
                    no = 1
                    for quiz in self.quest_list:
                        print('{}. {}'.format(no, quiz[1]))   
                        alpha = 97
                        valid_option = []
                        for options in range(2, len(quiz)):
                            print('{}) {}'.format(chr(alpha), quiz[options]), end='       ')
                            valid_option.append(chr(alpha))
                            alpha+=1
                        opt = input('Enter correct option : ')
                        print('\n')
                        if opt not in valid_option:
                            print('You have entered invalid option')
                            print('\n')
                            self.quiz(quiz[0], no)
                        else:
                            self.answer[quiz[0]] = opt
                            self.quiz_no+=1
                            if no==number:
                                self.quiz()
                        no+=1
                        print('\n')
            elif start!=0:
                with open('quiz.csv', 'r') as file:
                    questions = csv.reader(file)
                    for question in questions:
                        if question[0]==start:
                            print('{}. {}'.format(no, question[1]))
                            alpha = 97
                            valid_option = []
                            for options in range(2, len(question)):
                                print('{}) {}'.format(chr(alpha), question[options]), end='       ')
                                valid_option.append(chr(alpha))
                                alpha+=1
                            opt = input('Enter correct option : ')
                            print('\n')
                            if opt not in valid_option:
                                print('You have entered invalid option')
                                print('\n')
                                self.quiz(question[0], no)
                            else:
                                self.answer[question[0]] = opt
                                self.quiz_no+=1
                                if no==number:
                                    self.quiz()
        elif self.quiz_no==20:
            self.validate()
        
    def validate(self):
        answer = self.answer
        keys = []
        mark = 0
        with open('key.csv', 'r') as file:
            temp_keys = csv.reader(file)
            for i in temp_keys:
                keys.append(i)
        for answers in answer.items():
            for key in range(len(keys)):
                if keys[key][0]==answers[0] and keys[key][1]==answers[1]:       
                    mark+=1
        incorrect = self.quiz_no-mark
        percentage = (mark*100)/self.quiz_no
        print('Incorrect Answers: ', incorrect)
        print('Correct Answers: ', self.quiz_no-incorrect)
        print('Total marks : ', mark, '({}%)'.format(percentage))
        if percentage<70:
            print('You have failed the exam')
        else:
            print('Congratulations! You have successfully cleared the exam')
        