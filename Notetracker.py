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


def Adding_subject(grades):
    subject = input("enter subject")
    if subject in grades:
        print(f"{subject}""already exist")
    else:
        grades[subject] = []
        save_grades(grades)
        print(f"'{subject}' added successfully!")


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