from factories import UserFactory

class UserSeeder : 
    def execute(self):
        print('execute user seed')
        (UserFactory.UserFactory()).count(60).create([])