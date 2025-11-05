with open("courses.txt", "r") as file:
    courses = file.read()
    print(courses, end="")                      # end="" will remove the last newline in the document