class Person:
    def __init__(self, name, birthday, occupation, higher_education):
        self.name = name
        self.birthday = birthday
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        print(f'{self.name},whose birthday is on {self.birthday}, occupation is {self.occupation} and has higher education:{self.higher_education}')
class Classmate(Person):
    def __init__(self, name, birthday, occupation, higher_education, group_name):
        super().__init__(name, birthday, occupation, higher_education)
        self.group_name = group_name
    def introduce(self):
        print(f"My name is {self.name} and I am Aisha's classmate.I was born on {self.birthday},my occupation is {self.occupation} and has higher education: {self.higher_education} and we were studying together in {self.group_name}")
class Friend(Person):
    def __init__(self, name, birthday, occupation, higher_education, hobby):
        super().__init__(name, birthday, occupation, higher_education)
        self.hobby = hobby
    def introduce(self):
        print(f"My name is {self.name} and I am Aisha's friend.I was born on {self.birthday},my occupation is {self.occupation} and has higher education: {self.higher_education}.My hobby is {self.hobby}")
aimen = Classmate('Aimen', '11.02.2008', 'student', False, '11g')
ramina = Classmate('Ramina', '11.03.2009', 'student', False, "8l")
aizhamal = Friend('Aizhamal', '11.03.2006', 'teacher', True, 'hobby horsing')
asema = Friend('Asema', '11.06.2003', 'physicist', True, 'playing music instuments')
people = [aimen, ramina, aizhamal, asema]
for person in people:
    person.introduce()