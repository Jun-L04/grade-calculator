from my_grades import *
# not showing u my actual grades lol

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
