class Student:
    def __init__(self, name, age, student_id__):
        self.name = name
        self.age = age
        self.__student_id__ = student_id__

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_student_id__(self):
        return self.__student_id__

    def set_name(self, n):
        self.name = n

    def set_age(self, a):
        self.age = a


obj = Student("Bob", 21, 112457)
obj.__student_id__ = 112458
print(obj.__student_id__)