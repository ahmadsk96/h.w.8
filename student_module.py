class Student:
    """ This Class for All students
     We use this class if we want to create ....
      """

    def __init__(self, name, age, city):
        self.f_name = name
        self.f_age = age
        self.f_city = city

        print(f'Hello  {self.f_name},'
              f'your age is {self.f_age} '
              f'and your are from {self.f_city}.')


    def add_mark(self, *mark):
        print(f'your marks:{mark}')



    def calc_avg(self, *marks):
        my_sum = 0
        for mark in marks:
            my_sum += mark
        my_avg = my_sum // len(marks)
        print(f'your avg: {my_avg}')




student1 = Student("Ahmed", 97, "Gaza")
student1.add_mark(5, 7, 9)
student1.calc_avg(8, 8, 8)
