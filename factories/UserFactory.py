from . import base
from Models.User import User
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="dev",
    host="localhost",
    database="poc-seed"
)

engine = create_engine(url)
connection = engine.connect()

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

class UserFactory(base.BaseFactory):
    
    def __init__(self):
        super().__init__()        
    
    def create(self, attributes):
        for i in range(1, self.quantity+1):
            self.default = {
                "first_name": self.faker.first_name(),
                "last_name": self.faker.last_name(),
                "phone": self.faker.phone_number(),
                "birthday": self.faker.date()
            }
            newUser = User(**self.default)
            session.add(newUser)
            session.commit()

