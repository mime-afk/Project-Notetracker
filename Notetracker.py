import os

file_Grades = "Subject.txt"


def Loading_file():
    grades = {}
    if os.path.exists(file_Grades):
        with open(file_Grades, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    subject = parts[0]
                    grades[subject] = [float(grade) for grade in parts[1:]]
    return grades


def save_grades(grades):
    with open(file_Grades, "w") as file:
        for subject, grade_list in grades.items():
            line = f"{subject},{','.join(map(str, grade_list))}\n"
            file.write(line)


def pause():
    input("\nDrücke Enter, um zurück ins Menü zu gehen...")


def Adding_subject(grades):
    subject = input("Enter subject: ")

    if subject in grades:
        print(f"{subject} already exist")
    else:
        grades[subject] = []
        save_grades(grades)
        print(f"{subject} added successfully!")


def list_subjects(grades):
    subjects = list(grades.keys())
    if not subjects:
        print("Es sind noch keine Fächer vorhanden.")
        return []

    print("\nFächer:")
    for i, subject in enumerate(subjects, start=1):
        print(f"{i}. {subject}")

    return subjects


def remove_subject(grades):
    subjects = list_subjects(grades)
    if not subjects:
        return

    choice_input = input("Welche Nummer möchtest du löschen? ")

    try:
        choice = int(choice_input)
    except ValueError:
        print("Das war keine gültige Zahl.")
        return

    if choice < 1 or choice > len(subjects):
        print("Diese Nummer gibt es nicht.")
        return

    subject_to_remove = subjects[choice - 1]
    del grades[subject_to_remove]
    save_grades(grades)
    print(f"{subject_to_remove} removed")


def add_grade(grades):
    subjects = list_subjects(grades)
    if not subjects:
        return

    choice_input = input("Zu welchem Fach (Nummer) möchtest du eine Note hinzufügen? ")

    try:
        choice = int(choice_input)
    except ValueError:
        print("Das war keine gültige Zahl.")
        return

    if choice < 1 or choice > len(subjects):
        print("Diese Nummer gibt es nicht.")
        return

    subject = subjects[choice - 1]

    while True:
        grade_input = input("Welche Note möchtest du eintragen? (z.B. 5.5) ")

        try:
            grade = float(grade_input)
            break
        except ValueError:
            print("Das war keine gültige Zahl. Bitte nochmal eingeben.")

    grades[subject].append(grade)
    save_grades(grades)
    print(f"Note {grade} wurde zu '{subject}' hinzugefügt.")


def delete_grade(grades):
    subjects = list_subjects(grades)
    if not subjects:
        return

    choice_input = input("Aus welchem Fach (Nummer) möchtest du eine Note löschen? ")

    try:
        choice = int(choice_input)
    except ValueError:
        print("Das war keine gültige Zahl.")
        return

    if choice < 1 or choice > len(subjects):
        print("Diese Nummer gibt es nicht.")
        return

    subject = subjects[choice - 1]

    if not grades[subject]:
        print(f"Im Fach '{subject}' gibt es noch keine Noten.")
        return

    print(f"\nNoten in '{subject}':")
    for index, grade in enumerate(grades[subject], start=1):
        print(f"{index}. {grade}")

    grade_choice_input = input("Welche Note (Nummer) möchtest du löschen? ")

    try:
        grade_choice = int(grade_choice_input)
    except ValueError:
        print("Das war keine gültige Zahl.")
        return

    if grade_choice < 1 or grade_choice > len(grades[subject]):
        print("Diese Nummer gibt es nicht.")
        return

    removed = grades[subject].pop(grade_choice - 1)
    save_grades(grades)
    print(f"Note {removed} wurde aus '{subject}' gelöscht.")


def show_grades(grades):
    if not grades:
        print("Es sind noch keine Fächer vorhanden.")
        return

    for subject, grade_list in grades.items():
        print(f"\nFach: {subject}")

        if not grade_list:
            print("  Noch keine Noten eingetragen.")
        else:
            print("  Noten:", ", ".join(map(str, grade_list)))
            average = sum(grade_list) / len(grade_list)
            print(f"  Durchschnitt: {average:.2f}")


def main():
    grades = Loading_file()

    while True:
        print("\nGrade Tracker Menu:")
        print("1. Add Subject")
        print("2. Remove Subject")
        print("3. Add Grade")
        print("4. Delete Grade")
        print("5. Show Grades")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            Adding_subject(grades)
            pause()
        elif choice == "2":
            remove_subject(grades)
            pause()
        elif choice == "3":
            add_grade(grades)
            pause()
        elif choice == "4":
            delete_grade(grades)
            pause()
        elif choice == "5":
            show_grades(grades)
            pause()
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Invalid choice! Please try again.")
            pause()


if __name__ == "__main__":
    main()
