from abc import abstractmethod, ABC


class Animal(ABC):

    @abstractmethod
    def run(self):
        pass


class Cat(Animal):
    def run(self):
        print("Cat run")


class Dog(Animal):
    def run(self):
        print("Dog run")


class Lion(Animal):
    def run(self):
        print("Lion run")


class Fish:

    def swim(self):
        print("Fish Swim")

    def calc(self, x):
        if x == 1:
            print(x)


def run_all(animals: list[Animal]) -> None:
    for animal in animals:
        print(animal, type(animal))
        animal.run()


if __name__ == "__main__":
    animals = [Cat(), Dog(), Lion(), Fish()]
    run_all(animals)
