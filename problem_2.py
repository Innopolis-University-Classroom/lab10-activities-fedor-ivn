class Burger:
    class Size:
        MINI = 0,
        MEDIUM = 1,
        BIG = 2
    def __init__(self) -> None:
        self.cheese = None
        self.peperone = None
        self.letucci = None
        self.tomato = None
        self.size = None

class BurgerBuilder:
    def __init__(self) -> None:
        self.instance = Burger()
    
    def add_cheese(self):
        self.instance.cheese = "cheese"
    
    def add_peperone(self):
        self.instance.peperone = "peperone"
    
    def add_tomato(self):
        self.instance.tomato = "tomato"
    
    def choose_size(self, size):
        self.instance.size = size
    
    def get_result(self) -> Burger:
        return self.instance

def main():
    builder = BurgerBuilder()
    builder.add_cheese()
    builder.add_tomato()
    builder.choose_size(Burger.Size.MEDIUM)

    burger = builder.get_result()


