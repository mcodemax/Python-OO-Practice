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

    def __init__(self, start=100):
        """Create a serial generator with given start count"""
        self.start = start - 1
        self.start_original = start - 1
        

    def generate(self):
        """Increases the serial generator's start count"""
        self.start+=1
        return self.start

    def reset(self):
        """Reset serial geneator to the original start count"""
        self.start = self.start_original