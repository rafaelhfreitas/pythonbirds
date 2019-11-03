class Person:
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Person()
    print(Person.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())