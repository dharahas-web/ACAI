import hashlib
if __name__ == "__main__":
    collect_student_details()
    def hash_details(name, age, email):
        details = f"{name},{age},{email}"
        hashed = hashlib.sha256(details.encode()).hexdigest()
        with open("student_details_hashed.txt", "a") as file:
            file.write(f"{hashed}\n")

    name = input("Enter student name for hashing: ")
    age = input("Enter student age for hashing: ")
    email = input("Enter student email for hashing: ")
    hash_details(name, age, email)