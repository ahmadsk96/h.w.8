class Subject:
    """ This Class for All subjects
     We use this class if we want to create ....
      """

    def __init__(self, name, mark):
        self.f_name = name
        self.f_mark = mark

        print(f'Hello  {self.f_name} your mark is {self.f_mark}')


subject1 = Subject("Ahmed", 97)