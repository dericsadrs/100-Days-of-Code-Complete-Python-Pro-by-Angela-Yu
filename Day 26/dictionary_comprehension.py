


#
# Created on Mon Jun 19 2023
# Created by Software Engineer Deric San Andres
#


import random

names = [ "Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]


student_scores = {student:random.randint(1,100) for student in names}

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}


print(passed_students)