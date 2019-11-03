class Person:
    def __init__(self, *sons, name=None, age=35):
        self.name = name
        self.age = age
        self.sons = list(sons)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    rafael = Person(name='Rafael')
    viviane = Person(rafael,name='Viviane')
    print(Person.cumprimentar(rafael))
    print(id(rafael))
    print(rafael.cumprimentar())
    print(rafael.name)
    print(rafael.age)
    print(viviane.sons)
    for son in viviane.sons:
        print(son.name)
    rafael.sobrenome = 'Henrique'
    del rafael.sons
    print(rafael.__dict__)
    print(viviane.__dict__)
