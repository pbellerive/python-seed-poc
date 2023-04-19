from . import base
from database import connection
from Models.User import User
from sqlalchemy.orm import sessionmaker

engine = connection.Connection.instance()

Session = sessionmaker(bind=engine)
session = Session()

class UserFactory(base.BaseFactory):

    def __init__(self):
        super().__init__()

    def create(self, attributes):
        for i in range(1, self.quantity+1):
            self.default = "first_name": self.faker.first_name(),
                "last_name": self.faker.last_name(),
                "phone": self.faker.phone_number(),
                "birthday": self.faker.date() {

            }
            newUser = User(**self.default)
            session.add(newUser)
            session.commit()

