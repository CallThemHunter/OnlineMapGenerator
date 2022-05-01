#! /usr/bin/python3

class Base():
    def __init__(self, factory):
        self.factory = factory

        self.history = []
        self.results = []

    def process(self, data):
        pass

    def fetch(self):
        pass
    
