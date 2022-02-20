from faker import Faker
faker = Faker()
for i in range(700000):
    print( str(i) +""+faker.name())