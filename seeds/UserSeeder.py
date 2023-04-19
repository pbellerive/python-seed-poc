from factories import UserFactory

class UserSeeder :
    def execute(self):
        print('execute user seed')
        (UserFactory.UserFactory()).create(['name': 'Patrick'])
        (UserFactory.UserFactory()).create(['name': 'Patricia'])
        (UserFactory.UserFactory()).create([])
        (UserFactory.UserFactory()).create([])
        (UserFactory.UserFactory()).create([])
        (UserFactory.UserFactory()).create([])
        (UserFactory.UserFactory()).create([])