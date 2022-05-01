#! /usr/bin/env python3
from .base import Base


class OnlineProcessor(Base):
    def __init__(self, factory):
        super(OnlineProcessor).__init__(factory)

    def process(self, data):
        self.history += [data]
        self.factory.process(data)
        self.results += [self.factory.output]

    def fetch(self):
        return self.results
