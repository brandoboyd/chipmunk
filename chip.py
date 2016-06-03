class Animal(object):
    pass

class Chipmunk(Animal):

    def __init__(self, name):
        self.name = name
charles = Chipmunk('Charles')

print(charles.name)
