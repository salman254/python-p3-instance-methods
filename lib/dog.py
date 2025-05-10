#!/usr/bin/env python3

# lib/dog.py

class Dog:
    def bark(self):
        print("Woof!")
    
    def sit(self):
        print("The dog is sitting.")

# Testing the methods
if __name__ == "__main__":
    fido = Dog()
    fido.bark()  # Should print "Woof!"
    fido.sit()   # Should print "The dog is sitting."
