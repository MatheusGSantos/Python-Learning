"""
    Classes: this is a summary of OOP in python
"""

class My_Class: # class definition
    my_attr = 0 # a class variable, that can be shared with all instances of the class
    def __init__(self,attr1, attr2): # constructor
        """ instance variables """
        self.a = attr1
        self.b = attr2

    # a regular method
    def my_method(self):
        print("this is a class method")

    """
        A method that takes a class as an argument and change a class variable's value. Is like a regular method outside the class, but has some relation with the class
    """
    @classmethod
    def set_my_attr(cls, val): # equivalent to My_Class.myattr = val
        """
            Outside the class is used like this:
                Example: My_Class.set_my_attr(3)
                *Same as: My_Class.my_attr(3)
        """
        cls.my_attr = val

    # Usually class methods are used to create alternative constructors, like this:
    @classmethod
    def from_string(cls, string): # create an object from string like "name,age"
        """
        Usage example:
            new_obj = My_class.from_string("Ana,21")
        """
        name, age = string.split(',')
        return My_Class(name, age)

    """
        Static Methods: a method that doesn't rely on instances or the class, but has some relation with the class
    """
    @staticmethod
    def is_odd(n):
        if n % 2 == 0:
            return False
        return True
    

"""
    Inheritance
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("I'm talking")
    
class Developer(Person):
    def __init__(self, name, age, sallary):
        super().__init__(name, age) # parent constructor
        self.sallary = sallary
    
    
"""
    Dunder methods (magic methods or double underscore methods)
"""

class New_Class:
    # __init__ is a dunder method
    def __init__(self, number, letter):
        self.number = number
        self.letter = letter

    # __repr__ is a dunder method (representation print format)
    def __repr__(self):
        return "New_Class({}, {})".format(self.number, self.letter)
    
    # __str__ is a dunder method (string print format)
    def __str__(self):
        return "{}, {}".format(self.number, self.letter)
    
    # __add__ is a dunder method (instance + instance operation)
    def __add__(self, other):
        return self.number + other.number


"""
    Property decorators: similar to selector methods in other languages
"""

class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        """
            Eg.: print(obj.fullname)
        """
        return self.first + self.last

    @fullname.setter
    def fullname(self, name):
        """
            obj.fullname = "some name"
        """
        f, l = name.split(' ')
        self.first = f
        self.last = l
    
    @fullname.deleter
    def fullname(self):
        """
            del obj.fullname
        """
        self.first = None
        self.last = None