class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"i'm {self.make} {self.model}.")

my_car = Vehicle('tesla', 'model 3')

# print(my_car.make)
# print(my_car.model)
my_car.moves()
my_car.get_make_model()

your_car = Vehicle('cadilac', 'Escalade')
your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
    def moves(self):
        print('Flies Along..')

class Truck(Vehicle):
    def moves(self):
        print('Rumbling Along..')

class GolfCart(Vehicle):
    pass


cessna = Airplane('Cessna', 'Skyhowk')
mack = Truck('MAck', 'Pinnacle')
golfWagon = GolfCart('Yamaha','GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfWagon.get_make_model()
golfWagon.moves()

print('\n\n')

#polymorpihsm memangil semua object pada loop
for v in (my_car, your_car, cessna, mack, golfWagon):
        v.get_make_model()
        v.moves()