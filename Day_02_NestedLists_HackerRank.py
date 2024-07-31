"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

"""

def second_ranker_list(students):
    grades_list = [student[1] for student in students]
    second_grade = sorted(list(set(grades_list)))[1]
    # print(grades_list,second_grade)
    ranker_list = []
    for s_name, s_grade in students:
        if s_grade == second_grade:
            ranker_list.append(s_name)

    for name in sorted(ranker_list):
        print(name)


if __name__ == "__main__":
    # students = [["Harsh",39], ["Akriti", 41], ["Harry",37.21], ["Berry", 37.21], ["Tina", 37.2]]
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

    second_ranker_list(students)
