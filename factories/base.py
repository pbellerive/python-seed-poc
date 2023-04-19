from abc import ABC, abstractmethod
from faker import Faker

class BaseFactory(ABC):
    quantity = 1
    faker = None

    def __init__(self):
        Faker.seed(0)
        self.faker = Faker()

    @abstractmethod
    def create(self):
        pass

    def count(self, quantity):
        self.quantity = quantity
        return self