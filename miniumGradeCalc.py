

# key: specific assignment
# value: list[current grade, weight]

# weight of the final
finalWeight = 0.125
gradeWanted = 93


def finalGradeNeeded(gradesDict, finalWeight, gradeWanted):
    grade = 0.0
    for val in gradesDict.values():
        grade += val[0] * val[1]

    finalScoreNeeded = (gradeWanted - grade) / finalWeight

    return finalScoreNeeded


print(
    f'Need a final grade of: {finalGradeNeeded(gradesDict485, finalWeight, gradeWanted)}')
