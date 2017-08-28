class Teacher():
    def __init__(self, name, age, qualifications):
        self.name = name
        self.age = age
        self.qualifications = qualifications

    def __repr__(self):
        return ("{0} is a(n) {1} year old Teacher, qualifications include {2}.".format(self.name, self.age, self.qualifications))