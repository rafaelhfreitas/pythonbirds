class Person:
    eyes = 2

    def __init__(self, *sons, name=None, age=35):
        self.name = name
        self.age = age
        self.sons = list(sons)

    def greetings(self):
        return f'Olá, meu nome é {self.name}'

    @staticmethod
    def method_static():
        return 10

    @classmethod
    def name_and_attributes_class(cls):
        return f'{cls} - eyes {cls.eyes}'


class Man(Person):
    def greetings(self):
        greetings_parent_class = super().greetings()
        return f'{greetings_parent_class}. Aperto de mão'


class Woman(Person):
    pass


class Mutant(Person):
    eyes = 3


if __name__ == '__main__':
    rafael = Man(name='Rafael')
    viviane = Woman(rafael, name='Viviane')
    print(Person.greetings(rafael))
    print(id(rafael))
    print(rafael.greetings())
    print(rafael.name)
    print(rafael.age)
    print(viviane.sons)
    for son in viviane.sons:
        print(son.name)
    rafael.last_name = 'Henrique'
    del rafael.sons
    print(rafael.__dict__)
    print(viviane.__dict__)
    print(Person.eyes)
    print(Person.method_static(), rafael.method_static())
    print(Person.name_and_attributes_class(), rafael.name_and_attributes_class(), viviane.name_and_attributes_class())
    person = Person()
    print(isinstance(person, Person))
    print(rafael.eyes)
    print(rafael.greetings())
    print(viviane.greetings())
