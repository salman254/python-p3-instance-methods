#!/usr/bin/env python3

# lib/person.py

class Person:
    def talk(self):
        print("Hello World!")
    
    def walk(self):
        print("The person is walking.")

# Testing the methods
if __name__ == "__main__":
    john = Person()
    john.talk()  # Should print "Hello World!"
    john.walk()  # Should print "The person is walking."
