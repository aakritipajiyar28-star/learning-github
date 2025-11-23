# marks.py
# Simple program to read student marks, print each student's total & average,
# and print class total and class average.

def read_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")

def read_marks(prompt, subjects):
    while True:
        parts = input(prompt).replace(',', ' ').split()
        try:
            marks = [float(x) for x in parts]
        except ValueError:
            print("Enter numeric marks separated by space or comma.")
            continue
        if len(marks) != subjects:
            print(f"Please enter exactly {subjects} marks.")
            continue
        return marks

def main():
    print("Student marks -> total and average")
    n_students = read_int("Number of students: ")
    if n_students <= 0:
        print("No students.")
        return
    n_subjects = read_int("Number of subjects per student: ")
    if n_subjects <= 0:
        print("No subjects.")
        return

    students = []
    class_total = 0.0

    for i in range(1, n_students + 1):
        name = input(f"Name of student {i}: ").strip() or f"Student{i}"
        marks = read_marks(f"Enter {n_subjects} marks for {name} (space/comma separated): ", n_subjects)
        total = sum(marks)
        avg = total / n_subjects
        students.append((name, total, avg))
        class_total += total

    print("\nResults:")
    print(f"{'Name':20} {'Total':10} {'Average':10}")
    for name, total, avg in students:
        print(f"{name:20} {total:10.2f} {avg:10.2f}")

    overall_average = class_total / (n_students * n_subjects)
    print(f"\nClass total marks: {class_total:.2f}")
    print(f"Class average mark (per subject): {overall_average:.2f}")

if __name__ == "__main__":
    main()