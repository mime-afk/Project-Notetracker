import os  # This lets us check if the file exists

# The file where we save the grades
GRADES_FILE = "subjects.txt"

def load_grades():
    """Load grades from the text file."""
    grades = {}  # This dictionary will store subjects and grades
    if os.path.exists(GRADES_FILE):  # Check if the file exists
        with open(GRADES_FILE, "r") as file:  # Open the file for reading
            for line in file:  # Read each line in the file
                line = line.strip()  # Remove extra spaces
                if line:  # If the line is not empty
                    parts = line.split(",")  # Split the line into parts
                    subject = parts[0]  # The first part is the subject name
                    subject_grades = []  # List to store grades for this subject
                    for grade in parts[1:]:  # Loop through the rest (the grades)
                        if grade:
                            try:
                                 subject_grades.append(float(grade))  # Add each grade to the list
                            except ValueError: # Skip invalid grades
                                continue
                    grades[subject] = subject_grades  # Save the subject and grades
    return grades  # Return the dictionary with all subjects and grades

def save_grades(grades):
    """Save grades to the text file."""
    with open(GRADES_FILE, "w") as file:  # Open the file for writing
        for subject, subject_grades in grades.items():  # Loop through subjects and grades
            # Write the subject and grades as a line in the file
            file.write(f"{subject},{','.join(map(str, subject_grades))}\n")

def add_subject(grades):
    """Add a new subject."""
    subject = input("Enter the subject name: ")
    if subject in grades:  # Check if the subject already exists
        print(f"'{subject}' already exists!")
    else:
        grades[subject] = []  # Add the subject with an empty list of grades
        save_grades(grades)  # Save the changes to the file
        print(f"'{subject}' added successfully!")

def remove_subject(grades):
    """Remove a Subject."""
    print("\nRemove a Subject:")
    for subject, subject_grades in grades.items():
        print(f"{subject}")
    subject = input("Enter the subject name to remove: ")
    if subject in grades:  # Check if the subject exists
        del grades[subject]  # Remove the subject
        save_grades(grades)  # Save the changes
        print(f"'{subject}' removed successfully!")
    else:
        print(f"'{subject}' not found!")

def add_grade(grades):
    """Add a grade to a subject."""
    print("\nAdd grade:")
    subject = input("Enter the subject name: ")
    if subject in grades:  # Check if the subject exists
        try:
            grade = float(input("Enter the grade: "))  # Ask for the grade
            grades[subject].append(grade)  # Add the grade to the subject
            save_grades(grades)  # Save the changes
            print(f"Grade {grade} added to '{subject}'!")
        except ValueError:  # If the grade is not a number
            print("Invalid grade! Please enter a number.")
    else:
        print(f"'{subject}' not found!")


def view_grades(grades):
    """View all subjects and grades."""
    while True:  # Loop until the user chooses to go back
        if not grades:  # If there are no subjects
            print("No subjects or grades found!")
        else:
            for subject, subject_grades in grades.items():  # Loop through subjects and grades
                if subject_grades:  # If there are grades for the subject
                    average = sum(subject_grades) / len(subject_grades)  # Calculate the average
                    print(f"{subject}: {subject_grades} (Average: {average:.2f})")
                else:
                    print(f"{subject}: No grades yet.")

        # Ask the user if they want to go back
        print("\nPress '1' to go back to the main menu.")
        choice = input("Your choice: ").strip().lower()
        if choice == '1':
            break  # Exit the loop and return to the main menu
        else:
            print("Invalid choice! Press '1' to go back.")


def main():
    """Main function to run the grade tracker."""
    grades = load_grades()  # Load grades from the file
    while True:  # Loop forever until the user exits
        print("\nGrade Tracker Menu:")
        print("1. Add Subject")
        print("2. Remove Subject")
        print("3. Add Grade")
        print("4. View Grades")
        print("5. Exit")
        choice = input("Enter your choice: ")  # Ask for the user's choice
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
            break  # Exit the loop and end the program
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()  # Run the main function
