def collect_student_details():
    """
    Collects student details from user input and appends them to a file.
    Prompts the user to enter the student's name, age, and email address.
    The collected information is then written to 'student_details.txt' in append mode.
    Note:
    - The stored data includes personally identifiable information (PII).
    - Consider anonymizing or protecting this data before storage or sharing, 
        such as hashing emails or using encryption, to comply with privacy regulations.
    """
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    email = input("Enter student email: ")

    with open("student_details.txt", "a") as file:
        file.write(f"Name: {name}, Age: {age}, Email: {email}\n")

if __name__ == "__main__":
    collect_student_details()