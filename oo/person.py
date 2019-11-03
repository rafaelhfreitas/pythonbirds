class Person:
    def __init__(self, name=None, age=35):
        self.name = name
        self.age = age

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Person()
    print(Person.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.name)
    p.name = 'Rafael'
    print(p.name)