#! /usr/bin/env python3
from .base import Base


class MixedProcessor(Base):
    step = 0
    buff = []
    def __init__(self, factory, period=5):
        super(MixedProcessor).__init__(factory)
        self.period = period

    def process(self, data):
        self.buff += data
        self.step = (self.step + 1)%self.period
        if self.step == 0:
            self.factory.process(self.buff)
            self.history += [self.buff]
            self.buff = []
            self.results += [self.factory.output]

    def fetch(self):
        return self.results
