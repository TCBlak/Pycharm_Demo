from dog import Dog
from cat import Cat
from pet import Pet

print()
my_dog = Dog('Black', 'Labrador', 67)
print(my_dog)
my_dog.make_noise()
my_dog.do_yo_thang(item='rings')
print()
her_cat = Cat('Orange', 'Tabbie', 14)
print(her_cat)
her_cat.make_noise()
her_cat.chase()
her_cat.do_yo_thang()
print()
if my_dog == her_cat:
    print('Trouble')
else:
    print('We are okay')

# my_pet = Pet('Nibbles', 'Black', 'Lhasa Apsa') YOU CAN NOT instantiate an object in an abstract class
# An abstract class can only be used as a parent class
# print(f'My pet is {my_pet.name} he is {my_pet.color} and he is a {my_pet.breed}')

# *args is a tuple
# this allows the user to pass a variable amount of arguments
def sum_them_up(args):
    total = 0
    for i in args:
        total += i
    return total

# positional arguments must come first (required arguments with names)
# *args after positional arguments
# **kwargs after *args
def about_me(fname, lname, *args, **kwargs):
    print(f'My name is {fname} {lname}')
    print('I have worked at:')
    for jobs in args:
        print(f'\t{jobs}')
    if 'spouse' in kwargs:
        print(f'I am married to {kwargs["spouse"]}')
    if 'pet' in args:
        print(f'My pet is named {kwargs["pet"].name}')

about_me('Todd', 'Blakley', 'Retail Manager', 'Restaraunt Manager', spouse='Nicole', pet=my_dog)
