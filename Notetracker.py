import os

# file to store data
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
    """Save grades to the text file."""
    with open(file_Grades, "w") as file:
        for subject, grade_list in grades.items():
            line = f"{subject},{','.join(map(str, grade_list))}\n"
            file.write(line)

def add_grade(grades):
    subject = input("Für welches Fach möchtest du eine Note eintragen? ")

    if subject not in grades:
        print(f"Das Fach '{subject}' gibt es noch nicht.")
        return  # Funktion hier beenden

    grade_input = input("Welche Note möchtest du eintragen? (z.B. 5.5) ")

    try:
        grade = float(grade_input)  # Text -> Zahl (Kommazahl)
    except ValueError:
        print("Das war keine gültige Zahl.")
        return

    grades[subject].append(grade)  # Note zur Liste hinzufügen
    save_grades(grades)  # in Datei speichern
    print(f"Note {grade} wurde zu '{subject}' hinzugefügt.")


def delete_grade(grades):
    subject = input("Aus welchem Fach möchtest du eine Note löschen? ")

    if subject not in grades:
        print(f"Das Fach '{subject}' gibt es nicht.")
        return

    if not grades[subject]:
        print(f"Im Fach '{subject}' gibt es noch keine Noten.")
        return

    print(f"Noten in '{subject}':")
    for index, grade in enumerate(grades[subject], start=1):
        print(f"{index}. {grade}")

    choice_input = input("Welche Note (Nummer) möchtest du löschen? ")

    try:
        choice = int(choice_input)
    except ValueError:
        print("Das war keine gültige Zahl.")
        return

    if choice < 1 or choice > len(grades[subject]):
        print("Diese Nummer gibt es nicht.")
        return

    removed = grades[subject].pop(choice - 1)  # -1 wegen 0-Index
    save_grades(grades)
    print(f"Note {removed} wurde aus '{subject}' gelöscht.")
    

def Adding_subject(grades):
    subject = input("Enter subject: ")
    if subject in grades:
        print(f"{subject} already exist")
    else:
        grades[subject] = []
        save_grades(grades)
        print(f"{subject} added successfully!")


def remove_subject(grades):
    subject = input("Enter subject you want to remove: ")
    if subject in grades:
        del grades[subject]
        save_grades(grades)
        print(f"{subject} removed")
    else:
        print(f"{subject} not found")

def show_grades(grades):
    if not grades:
        print("Es sind noch keine Fächer vorhanden.")
        return

    for subject, grade_list in grades.items():
        print(f"\nFach: {subject}")

        if not grade_list:
            print("  Noch keine Noten eingetragen.")
        else:
            # Noten anzeigen
            print("  Noten:", ", ".join(map(str, grade_list)))

            # Durchschnitt berechnen
            average = sum(grade_list) / len(grade_list)
            print(f"  Durchschnitt: {average:.2f}")

def main():
    grades = Loading_file()
    while True:
        print("\nGrade Tracker Menu:")
        print("1. Add Subject")
        choice = input("Enter your choice: ")

        if choice == "1":
            Adding_subject(grades)
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
