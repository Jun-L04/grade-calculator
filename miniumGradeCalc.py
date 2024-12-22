from my_grades import *
# not showing u my actual grades lol

# example grades dictionary:
gradesDictEx = {
    "Attendance": [100, 0.09],
    "Homework": [100, 0.10],
    "Midterm 1": [100, 0.15],
    "Midterm 2": [100, 0.15],
}
# key: specific assignment
# value: list[current grade, weight]


# weight of the final
finalWeight = 0.25
gradeWanted = 90


def finalGradeNeeded(gradesDict, finalWeight, gradeWanted):
    grade = 0.0
    for val in gradesDict.values():
        grade += val[0] * val[1]

    finalScoreNeeded = (gradeWanted - grade) / finalWeight

    return finalScoreNeeded


print(
    f'Need a final grade of: {finalGradeNeeded(gradesDict311, finalWeight, gradeWanted)}')
