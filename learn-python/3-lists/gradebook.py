last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Subject names below: 
subjects = [["physics"], ["calculus"], ["poetry"], ["history"]]
# Grades for each of the courses included below
grades=[98, 97, 85, 88]
#Merged the two together to make a list of grades and subjects
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
#Added in an example CS grade with append
new_value = ["computer science", 100]
gradebook.append(new_value)
#Also added in Visual Art with append
visual_arts=["visual arts", 93]
gradebook.append(visual_arts)
#changed visual art grade to a 98
gradebook[-1][-1]=98
#removed the 85 to make it a pass or fail course
gradebook[2].remove(85)
gradebook[2].append("Pass")
#added in last semesters example grades to make one full gradebook
full_gradebook= last_semester_gradebook + gradebook
print(full_gradebook)