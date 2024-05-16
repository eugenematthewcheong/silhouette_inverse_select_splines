# -*- coding:utf-8 -*-

from fx import *
import os

from tools.objectIterator import ObjectIterator

class gatherNonselected(ObjectIterator):
    def __init__(self):
        self.selectedObjects = []
    
    def visit(self, object):
        if isinstance(object, Shape):
            if object.selected:
                pass
            else:
                #print object
                self.selectedObjects.append(object)
        ObjectIterator.visit(self, object)


class inverseSelectionsplines(Action):

    def __init__(self):
        Action.__init__(self, 'EM Tools | Invert Selection')

    def execute(self):
        try:
            node = activeNode()
            c = gatherNonselected()
            c.iterate(node.children)

            select(c.selectedObjects)
        except:
            pass
        
        
addAction(inverseSelectionsplines())