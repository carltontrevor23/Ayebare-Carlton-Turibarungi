class Animal:
    def sound(self):
        print("Some generic animal sound")

class Goat(Animal):
    def sound(self):  # Overriding the sound method
        print("Bleattt!")

# Test
a = Animal()
a.sound()  # Output: Some generic animal sound

g = Goat()
g.sound()  # Output: Woof!
