#! /usr/bin/env python3
import numpy as np
from scipy.spatial import KDTree


class PointSegmenter:
    def __init__(self, data):
        self.data: KDTree = KDTree(
        
