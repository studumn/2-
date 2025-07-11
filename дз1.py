class Person:
    def __init__(self, name, birthday, occupation, higher_education):
        self.name = name
        self.birthday = birthday
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        print(f'{self.name},whose birthday is on {self.birthday}, occupation is {self.occupation} and has higher education:{self.higher_education}')
aisha = Person('Aisha', '10.01.2009', 'student', False )
aisha.introduce()
ulugbek = Person('Ulugbek', '28.11.2003', 'frontend', True )
ulugbek.introduce()