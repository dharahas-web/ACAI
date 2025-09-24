class Student:
    def __init__(self, n, a, m1, m2, m3):
        self.n = n
        self.a = a
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def details(self):
        print("Name: - task3.py:10", self.n, "Age:", self.a)

    def total(self):
        return self.m1 + self.m2 + self.m3

s1 = Student("Ravi", 20, 85, 90, 78)
s2 = Student("Anita", 19, 88, 76, 92)

s1.details()
print("Total Marks: - task3.py:19", s1.total())
print()
s2.details()
print("Total Marks: - task3.py:22", s2.total())
