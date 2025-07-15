class Person:
    def __init__(self, name, birthday, occupation, higher_education):
        self.name = name
        self.birthday = birthday
        self.__occupation = occupation
        self.__higher_education = higher_education

    def get_occupation(self):
        return self.__occupation

    def get_higher_education(self):
        return self.__higher_education

    def introduce(self):
        print(
f'{self.name},whose birthday is on {self.birthday}, occupation is {self.get_occupation()} and has higher education:{self.get_higher_education()}')

class Classmate(Person):
    def __init__(self, name, birthday, occupation, higher_education, group_name):
        super().__init__(name, birthday, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(
f"My name is {self.name} and I am Aisha's classmate.I was born on {self.birthday},my occupation is {self.get_occupation()} and has higher education: {self.get_higher_education()} and we were studying together in {self.group_name}")

class Friend(Person):
    def __init__(self, name, birthday, occupation, higher_education, hobby):
        super().__init__(name, birthday, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(
f"My name is {self.name} and I am Aisha's friend.I was born on {self.birthday},my occupation is {self.get_occupation()} and has higher education: {self.get_higher_education()}.My hobby is {self.hobby}")

cl1 = Classmate(
    'Aimen', '11.02.2008', 'student', False, '11g')
cl2 = Classmate(
    'Ramina', '11.03.2009', 'student', False, "8l")
fr1 = Friend(
    'Aizhamal', '11.03.2006', 'teacher', True, 'hobby horsing')
fr2 = Friend(
    'Asema', '11.06.2003', 'physicist', True, 'playing music instuments')

people = [cl1, cl2, fr1, fr2]

for person in people:
    person.introduce()