#! /usr/bin/env python3
from .base import Base


class OfflineProcessor(Base):
    def __init__(self, factory):
        super(OfflineProcessor).__init__(factory)

    def process(self, data):
        self.history += data

    def fetch(self):
        self.factory.process(self.history)
        return self.factory.output
