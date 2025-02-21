#!/usr/bin/env python3

class Person:
    # Class body goes here

    #Instance method definition
    def __init__(self, name):
        self.name = name


    def walk(self,):
        print (f"{self.name} is walking.")

    def talk (self):
        print ("Hello World!")



michell = Person("Michell")
michell.walk()

michell= Person("Michell")
michell.talk()

