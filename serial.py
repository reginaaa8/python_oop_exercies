"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start = 100):
        """create new generator, initialized at start"""
        self.start = self.next = start
    
    def __repr__(self):
        """show representation to more easily read terminal output"""
        return f"<SerialGenerator start = {self.start}, next = {self.next}>"
    
    def generate_next(self):
        """return next number"""
        self.next += 1
        return self.next -1
    
    def reset(self):
        """reset start value back to start"""
        self.next = self.start
      
serial = SerialGenerator(9002)
print(serial.generate_next())        


    
