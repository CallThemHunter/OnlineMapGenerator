#! /usr/bin/env python3


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.children = {
            0: None, # top left, y >= border and x < border
            1: None, # top right, x >= border and y > border
            2: None, # bottom right, y <= border and x > border
            3: None  # bottom left, x <= border and y < border
        }

        self.prev = None
        self.next = None
        


class QuadTree:
    def __init__(self):
        self.children = []
        self.value = None


