import os

# File to store subjects and grades
GRADES_FILE = "subjects.txt"


def pause():
    """Pause for userfrindlyness."""
    input("\nPress Enter to go back to the main menu...")


def load_grades():
    """Load grades from the file. """
    grades = {}
    if os.path.exists(GRADES_FILE):
        # open file or creat it
        with open(GRADES_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split(",")
                    subject_name = parts[0]
                    subject_grades = []
                    for grade_text in parts[1:]:
                        if grade_text:  # Skips empty grades
                            try:
                                subject_grades.append(float(grade_text))
                            except ValueError:
                                # Skip invalid grade entries
                                pass
                    grades[subject_name] = subject_grades
    return grades


def save_grades(grades):
    """ Save grades to the file."""
    # write subject and grade in to the file
    with open(GRADES_FILE, "w") as file:
        for subject_name, subject_grades in grades.items():
            # Write subject and grades separated with commas
            file.write(f"{subject_name},{','.join(map(str, subject_grades))}\n")

def add_subject(grades):
    """Add a new subject to the grades dictionary."""
    print("\nAdd Subject")
    subject_name = input("Enter the subject name: ").strip()
    if not subject_name:
        print("Subject name cannot be empty.")
    elif subject_name in grades:
        print("This subject already exists.")
    else:
        # Add the new subject
        grades[subject_name] = []
        save_grades(grades)
        print("Subject added.")
   
    pause()


def show_subjects(grades):
    """Display the list of subjects."""
    subject_list = list(grades.keys())
    if not subject_list:
        print("No subjects found.")
        return subject_list
    print("\nSubjects:")
    for index, subject_name in enumerate(subject_list, 1):
        print(f"{index}. {subject_name}")
    return subject_list


def remove_subject(grades):
    """Remove a subject from the grades dictionary. """
    print("\nRemove Subject")
    subject_list = show_subjects(grades)
    if not subject_list:
        pause()
        return
    try:
        choice = int(input("Type the number of the subject to remove: ").strip())
        if 1 <= choice <= len(subject_list):
            # Remove the subject
            subject_to_remove = subject_list[choice - 1]
            del grades[subject_to_remove]
            save_grades(grades)
            print(f"Subject removed: {subject_to_remove}")
        else:
            print("Number out of range.")
    except ValueError:
        print("Not a valid number.")
   
    pause()


def add_grade(grades):
    """ Add a grade to a subject."""
    print("\nAdd Grade")
    subject_list = show_subjects(grades)
    if not subject_list:
        pause()
        return
    try:
        choice = int(input("Type the number of the subject: ").strip())
        if 1 <= choice <= len(subject_list):
            subject_name = subject_list[choice - 1]
            while True:
                try:
                    # Add the grade to subject
                    grade = float(input("Enter the grade: ").strip())
                    grades[subject_name].append(grade)
                    save_grades(grades)
                    print(f"Grade added to {subject_name}")
                    break
                except ValueError:
                    print("Invalid grade. Please enter a number.")
        else:
            print("Number out of range.")
    except ValueError:
        print("Not a valid number.")
    pause()


def view_grades(grades):
    """ Display all subjects and their grades,  with the average."""
    print("\nView Grades")
    if not grades:
        print("No subjects or grades found.")
        pause()
        return
    for subject_name, subject_grades in grades.items():
        if not subject_grades:
            print(f"{subject_name}: No grades yet.")
        else:
            # display subject, grades and average
            average = sum(subject_grades) / len(subject_grades)
            print(f"{subject_name}: {subject_grades} (average: {average:.2f})")
    pause()

def main():
    """Main function to run the Grade Tracker program."""
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

if __name__ == "__main__":
    main()
