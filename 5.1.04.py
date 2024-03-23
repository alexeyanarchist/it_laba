class Programmer:

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.work_time = 0
        self.earnings = 0
        if position == "Junior":
            self.salary = 10
        elif position == "Middle":
            self.salary = 15
        elif position == "Senior":
            self.salary == 20

    def work(self, time):
        self.work_time += time
        self.earnings += self.salary * time

    def rise(self):
        if self.position == "Junior":
            self.position = "Middle"
            self.salary = 15
        elif self.position == "Middle":
            self.position = "Senior"
            self.salary = 20
        elif self.position == "Senior":
            self.salary += 1
    
    def info(self):
        return f"{self.name} {self.work_time}ч. {self.earnings}тгр."
    
programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())