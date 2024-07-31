"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example :
    alpha:[20,30,40]
    beta:[30,50,70]
    query_name = "beta"

    score is (30+50+70)/3 = 50.0 => output = 50.00

"""

if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float,line))
        student_marks[name] = scores
    
    query_name = input()

    # % operator
    print("%.2f" %(sum(student_marks[query_name])/len(student_marks[query_name])))

    # format method
    print(format(sum(student_marks[query_name])/len(student_marks[query_name]), ".2f"))

    # f-strings method
    print(f"{(sum(student_marks[query_name])/len(student_marks[query_name])):.2f}")

    # round function => works for floating value > 2 digits after decimal
    print(round(sum(student_marks[query_name])/len(student_marks[query_name]),2))
