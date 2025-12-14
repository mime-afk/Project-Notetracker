import os

GRADES_FILE = "subjects.txt"


def pause():
    input("\nPress Enter to go back to the main menu...")


def load_grades():
    grades = {}
    if os.path.exists(GRADES_FILE):
        with open(GRADES_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    subject = parts[0]
                    subject_grades = []
                    for g in parts[1:]:
                        if g:
                            try:
                                subject_grades.append(float(g))
                            except ValueError:
                                pass
                    grades[subject] = subject_grades
    return grades


def save_grades(grades):
    with open(GRADES_FILE, "w") as file:
        for subject, subject_grades in grades.items():
            file.write(f"{subject},{','.join(map(str, subject_grades))}\n")


def list_subjects(grades):
    subjects = list(grades.keys())
    if not subjects:
        print("No subjects found.")
        return []

    print("\nSubjects:")
    for i, s in enumerate(subjects, start=1):
        print(f"{i}. {s}")
    return subjects


def add_subject(grades):
    print("\nAdd subject:")
    subject = input("Enter the subject name: ").strip()

    if not subject:
        print("Subject name cannot be empty.")
        pause()
        return

    if subject in grades:
        print(f"'{subject}' already exists!")
    else:
        grades[subject] = []
        save_grades(grades)
        print(f"'{subject}' added successfully!")
    pause()


def remove_subject(grades):
    print("\nRemove a subject:")
    subjects = list_subjects(grades)
    if not subjects:
        pause()
        return

    while True:
        choice = input("Enter the number of the subject to remove (or 'b' to go back): ").strip().lower()
        if choice == "b":
            return

        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(subjects):
                subject = subjects[idx - 1]
                del grades[subject]
                save_grades(grades)
                print(f"'{subject}' removed successfully!")
                pause()
                return

        print("Invalid choice. Please enter a valid number.")


def add_grade(grades):
    print("\nAdd grade:")
    subjects = list_subjects(grades)
    if not subjects:
        pause()
        return

    subject = None
    while True:
        choice = input("Enter the number of the subject (or 'b' to go back): ").strip().lower()
        if choice == "b":
            return

        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(subjects):
                subject = subjects[idx - 1]
                break

        print("Invalid choice. Please enter a valid number.")

    while True:
        grade_input = input("Enter the grade (or 'b' to go back): ").strip().lower()
        if grade_input == "b":
            return
        try:
            grade = float(grade_input)
            grades[subject].append(grade)
            save_grades(grades)
            print(f"Grade {grade} added to '{subject}'!")
            pause()
            return
        except ValueError:
            print("Invalid grade! Please enter a number.")


def view_grades(grades):
    print("\nView grades:")
    if not grades:
        print("No subjects or grades found!")
        pause()
        return

    for subject, subject_grades in grades.items():
        if subject_grades:
            average = sum(subject_grades) / len(subject_grades)
            print(f"{subject}: {subject_grades} (Average: {average:.2f})")
        else:
            print(f"{subject}: No grades yet.")

    pause()


def main():
    grades = load_grades()
    while True:
        print("\nGrade Tracker Menu:")
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
            print("Invalid choice! Please try again.")
            pause()


if __name__ == "__main__":
    main()
