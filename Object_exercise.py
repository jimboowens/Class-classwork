
class Person(object):
    def __init__(self, name, email, phone, friends =[]):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends
        self.greeting_count = 0
    def greet(self, other_person):
        
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1
    def print_contact_info(self):
        print self.name, self.email, self.phone
    def add_friend(self, other_person_name):
        self.friends.append(other_person_name.name)
    def __repr__(self):
        return "%s %s %s " % ( self.name, self.email, self.phone)
# Write code to

# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', 
# and phone of '483-485-4948', store it in the variable sonny.
Sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948", [])

# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of 
# '495-586-3456', store it in the variable 'jordan'.
Jordan = Person("Jordan", "jordan@aol.com", "495-586-3456", [])

# Have sonny greet jordan using the greet method.
Sonny.greet(Jordan)
# Have jordan greet sonny using the greet method.
# Write a print statement to print the contact info (email and phone) of Sonny.
print Sonny.email
print Sonny.phone
# Write another print statement to print the contact info of Jordan.
print Jordan.email
print Jordan.phone

class Vehicle(object):
    # whenever we start making a new car, __init__ will run. 
    # we ALWAYS pass self first
    def __init__(self, make, model, year):
        # self is special. 
        # self refers to THIS object
        self.make = make #this is an instance, or internal variable
        self.model = model
        self.year = year
    def print_info(self):
        print self.year, self.make, self.model

car = Vehicle ("Nissan", "Leaf", "2015")
print car.year, car.make, car.model
car.print_info()
Sonny.print_contact_info()
Sonny.friends.append(Jordan.name)
Jordan.friends.append(Sonny.name)
Sonny.print_contact_info()
print len(Jordan.friends)
print Jordan.friends
Sonny.add_friend(Jordan)
print Sonny.friends
print Sonny.greeting_count
print Jordan