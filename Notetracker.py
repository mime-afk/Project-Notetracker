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
                subject = parts[0]
                subject_grades = []

                for g in parts[1:]:
                    if g != "":
                        try:
                            subject_grades.append(float(g))
                        except ValueError:
                            pass

                grades[subject] = subject_grades

    return grades


def save_grades(grades):
    file = open(GRADES_FILE, "w")
    for subject in grades:
        grade_list = grades[subject]
        file.write(subject)

        for g in grade_list:
            file.write("," + str(g))

        file.write("\n")
    file.close()


def add_subject(grades):
    print("\nAdd Subject")
    subject = input("Enter the subject name: ").strip()

    if subject == "":
        print("Subject name cannot be empty.")
        pause()
        return

    if subject in grades:
        print("This subject already exists.")
    else:
        grades[subject] = []
        save_grades(grades)
        print("Subject added.")

    pause()


def show_subjects(grades):
    subjects = list(grades.keys())

    if len(subjects) == 0:
        print("No subjects found.")
        return subjects

    print("\nSubjects:")
    i = 1
    for s in subjects:
        print(str(i) + ". " + s)
        i += 1

    return subjects


def remove_subject(grades):
    print("\nRemove Subject")
    subjects = show_subjects(grades)

    if len(subjects) == 0:
        pause()
        return

    choice = input("Type the number of the subject to remove: ").strip()

    if choice.isdigit() == False:
        print("Not a valid number.")
        pause()
        return

    choice_num = int(choice)

    if choice_num < 1 or choice_num > len(subjects):
        print("Number out of range.")
        pause()
        return

    subject_to_remove = subjects[choice_num - 1]
    del grades[subject_to_remove]
    save_grades(grades)
    print("Subject removed: " + subject_to_remove)

    pause()


def add_grade(grades):
    print("\nAdd Grade")
    subjects = show_subjects(grades)

    if len(subjects) == 0:
        pause()
        return

    choice = input("Type the number of the subject: ").strip()

    if choice.isdigit() == False:
        print("Not a valid number.")
        pause()
        return

    choice_num = int(choice)

    if choice_num < 1 or choice_num > len(subjects):
        print("Number out of range.")
        pause()
        return

    subject = subjects[choice_num - 1]

    while True:
        grade_text = input("Enter the grade: ").strip()
        try:
            grade = float(grade_text)
            grades[subject].append(grade)
            save_grades(grades)
            print("Grade added to " + subject + ".")
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

    for subject in grades:
        subject_grades = grades[subject]
        if len(subject_grades) == 0:
            print(subject + ": No grades yet.")
        else:
            average = sum(subject_grades) / len(subject_grades)
            print(subject + ": " + str(subject_grades) + " (Average: " + f"{average:.2f}" + ")")

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
