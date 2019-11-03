"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

Motor
Direção
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

Atributo de dado velocidade
Método acelerar, que deverá incremetar a velocidade de uma unidade
Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
Método girar_a_direita
Método girar_a_esquerda

       N
    W     E
       S

Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocity
    0
    >>> motor.speed_up()
    >>> motor.velocity
    1
    >>> motor.speed_up()
    >>> motor.velocity
    2
    >>> motor.speed_up()
    >>> motor.velocity
    3
    >>> motor.brake()
    >>> motor.velocity
    1
    >>> motor.brake()
    >>> motor.velocity
    0
    >>> # Testando Direcao
    >>> direction = Direction()
    >>> direction.value
    'North'
    >>> direction.turn_right()
    >>> direction.value
    'East'
    >>> direction.turn_right()
    >>> direction.value
    'South'
    >>> direction.turn_right()
    >>> direction.value
    'West'
    >>> direction.turn_right()
    >>> direction.value
    'North'
    >>> direction.turn_left()
    >>> direction.value
    'West'
    >>> direction.turn_left()
    >>> direction.value
    'South'
    >>> direction.turn_left()
    >>> direction.value
    'East'
    >>> direction.turn_left()
    >>> direction.value
    'North'
    >>> car = Car(direction, motor)
    >>> car.get_velocity()
    0
    >>> car.speed_up()
    >>> car.get_velocity()
    1
    >>> car.speed_up()
    >>> car.get_velocity()
    2
    >>> car.brake()
    >>> car.get_velocity()
    0
    >>> car.get_direction()
    'North'
    >>> car.turn_right()
    >>> car.get_direction()
    'East'
    >>> car.turn_left()
    >>> car.get_direction()
    'North'
    >>> car.turn_left()
    >>> car.get_direction()
    'West'
"""

DIRECTIONS = ['North', 'East', 'South', 'West']

class Car:
    def __init__(self, direction, motor):
        self.direction = direction
        self.motor = motor

    def get_velocity(self):
        return self.motor.velocity

    def speed_up(self):
        self.motor.speed_up()

    def brake(self):
        self.motor.brake()

    def get_direction(self):
        return self.direction.value

    def turn_right(self):
        self.direction.turn_right()

    def turn_left(self):
        self.direction.turn_left()


class Motor:

    def __init__(self, velocity=0):
        self.velocity = velocity

    def speed_up(self):
        self.velocity += 1

    def brake(self):
        self.velocity -= 2
        self.velocity = max(0, self.velocity)


class Direction:

    def __init__(self, direction=0):
        self.direction = 0
        self.value = DIRECTIONS[self.direction]

    def turn_right(self):
        self.direction = (self.direction + 1) % len(DIRECTIONS)
        self.value = DIRECTIONS[self.direction]

    def turn_left(self):
        self.direction = (self.direction - 1) % len(DIRECTIONS)
        self.value = DIRECTIONS[self.direction]
