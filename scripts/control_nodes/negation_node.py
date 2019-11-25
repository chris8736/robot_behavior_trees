#! /usr/bin/env python
import rospy

"""
todo: node that returns the negation of its child (like NOT)
"""

class RepeaterNode():

    def __init__(self, name):
        self.child = None
        self.name = name

    def tick(self):
        if self.child:
            return self.child.tick()

    def reset(self):
        if self.child:
            self.child.reset()

    def add_child(self, node):
        self.child = node