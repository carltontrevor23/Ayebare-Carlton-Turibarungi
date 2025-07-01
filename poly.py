# Polymorphism
# What is polymorphism?

# Example Three: Polymorphism with inheritance
# Superclass
class Bird:
    def fly(self):
        print('Birds flies in the sky')


# derived class
class Eagle(Bird):
    def fly(self):
        print('Eagle flies at high altitude')


class Sparrow(Bird):
    def fly(self):
        print('Sparrow flies at low altitude')


# How we use polymorphism
def flight_test(bird):
    bird.fly()  # Run respective class method based on an object


# Create objects
eagle1 = Eagle()
sparrow1 = Sparrow()

# Call the flight test method with diffrent objects

flight_test(eagle1)
flight_test(sparrow1)