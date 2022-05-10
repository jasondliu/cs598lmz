import _struct as _struct
import re

class _ParseObject:
    def __init__(self):
        self.value = None
        self.type = None
        self.text = None
        self.element_map = {}
        self.attribute_map = {}
    def __repr__(self):
        return str(self.value)
    def getValue(self):
        return self.value
 
class Optional(_ParseObject):
    
    def parse(self, text, itr):
        start = itr.copy()
        self.element_map.clear()
        self.attribute_map.clear()
        self.text = text
        result = None
        while True:
            try:
                result = self.element_map['_'].parse(text, start)
            except ParserElementException as e:
                if result is not None:
                    if not result:
                        self.element_map.clear()
                        self.attribute_map.clear()
                        break
                    else:
                        self.element_map.clear()
                        self.attribute_
