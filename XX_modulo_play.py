for item in range(1, 13):
    num_lollies = 12
    num_students = item

    division = num_lollies / num_students
    per_student = num_lollies // num_students
    lollies_left = num_lollies % num_students

    if lollies_left == 0:
        print(f"{item} is a factor of 12!")

    print(f"Each student gets {per_student} and we have {lollies_left} left over")
