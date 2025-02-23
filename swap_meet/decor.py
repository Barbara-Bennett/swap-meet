# create large unique numbers to the ids
import uuid
from swap_meet.item import Item

class Decor(Item):
    
    def __init__(self, id=None, condition=0, age=0, width=0, length=0):
        super().__init__(id, condition, age)
        self.width = width
        self.length = length

    def get_category(self):
        return "Decor"
    
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."