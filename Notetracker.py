import os

GRADES_FILE = "subjects.txt"


def pause():
    input("\nPress Enter to go back to the main menu...")


def load_grades():
    grades = {}

    if os.path.exists(GRADES_FILE):
        file = open(GRADES_FILE, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                subject_name = parts[0]
                subject_grades = []

                for grade_text in parts[1:]:
                    if grade_text != "":
                        try:
                            subject_grades.append(float(grade_text))
                        except ValueError:
                            pass

                grades[subject_name] = subject_grades

    return grades


def save_grades(grades):
    file = open(GRADES_FILE, "w")

    for subject_name in grades:
        file.write(subject_name)

        for grade in grades[subject_name]:
            file.write("," + str(grade))

        file.write("\n")

    file.close()


def add_subject(grades):
    print("\nAdd Subject")
    subject_name = input("Enter the subject name: ").strip()

    if subject_name == "":
        print("Subject name cannot be empty.")
        pause()
        return

    if subject_name in grades:
        print("This subject already exists.")
    else:
        grades[subject_name] = []
        save_grades(grades)
        print("Subject added.")

    pause()


def show_subjects(grades):
    subject_list = list(grades.keys())

    if len(subject_list) == 0:
        print("No subjects found.")
        return subject_list

    print("\nSubjects:")
    index = 1
    for subject_name in subject_list:
        print(str(index) + ". " + subject_name)
        index += 1

    return subject_list


def remove_subject(grades):
    print("\nRemove Subject")
    subject_list = show_subjects(grades)

    if len(subject_list) == 0:
        pause()
        return

    choice = input("Type the number of the subject to remove: ").strip()

    if choice.isdigit() == False:
        print("Not a valid number.")
        pause()
        return

    choice_number = int(choice)

    if choice_number < 1 or choice_number > len(subject_list):
        print("Number out of range.")
        pause()
        return

    subject_to_remove = subject_list[choice_number - 1]
    del grades[subject_to_remove]
    save_grades(grades)
    print("Subject removed: " + subject_to_remove)

    pause()


def add_grade(grades):
    print("\nAdd Grade")
    subject_list = show_subjects(grades)

    if len(subject_list) == 0:
        pause()
        return

    choice = input("Type the number of the subject: ").strip()

    if choice.isdigit() == False:
        print("Not a valid number.")
        pause()
        return

    choice_number = int(choice)

    if choice_number < 1 or choice_number > len(subject_list):
        print("Number out of range.")
        pause()
        return

    subject_name = subject_list[choice_number - 1]

    while True:
        grade_input = input("Enter the grade: ").strip()
        try:
            grade = float(grade_input)
            grades[subject_name].append(grade)
            save_grades(grades)
            print("Grade added to " + subject_name)
            break
        except ValueError:
            print("Invalid grade. Please enter a number.")

    pause()


def view_grades(grades):
    print("\nView Grades")

    if len(grades) == 0:
        print("No subjects or grades found.")
        pause()
        return

    for subject_name in grades:
        subject_grades = grades[subject_name]

        if len(subject_grades) == 0:
            print(subject_name + ": No grades yet.")
        else:
            average = sum(subject_grades) / len(subject_grades)
            print(subject_name + ": " + str(subject_grades) + " (Average: " + f"{average:.2f}" + ")")

    pause()


def main():
    grades = load_grades()

    while True:
        print("\nGrade Tracker Menu")
        print("1. Add Subject")
        print("2. Remove Subject")
        print("3. Add Grade")
        print("4. View Grades")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_subject(grades)
        elif choice == "2":
            remove_subject(grades)
        elif choice == "3":
            add_grade(grades)
        elif choice == "4":
            view_grades(grades)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            pause()


main()

