stud_marks = {'Adam' : 98, 'Bobby' : 95, 'Cena' : 90, 'Dani' : '88'}
name = input("Enter the student's name:")
if stud_marks.get(name):
    print("{}'s marks:".format(name), stud_marks.get(name))
else:
    print("Student not found.")
