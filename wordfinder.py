"""Word Finder: finds random words from a dictionary."""

from random import randrange

class WordFinder:
    """
    >>> w = WordFinder('test.txt')
    4 words read

    >>> w.random() in ['kale', 'parsnips', 'apple', 'mango']
    True


    >>> w.random() in ['kale', 'parsnips', 'apple', 'mango']
    True


    >>> w.random() in ['kale', 'parsnips', 'apple', 'mango']
    True


    >>> w.random() in ['kale', 'parsnips', 'apple', 'mango']
    True

    """

    def __init__(self, path):
        """Initializes an instance of WordFinder"""
        self.path = path
        self.word_list = []
        self.words_read = 0

        self.read_file(path)
        print(f"{self.words_read} words read")
        
    def __repr__(self):
        return f"{self.words_read} words read"

    def random(self):
        """Returns a random word that has already been read"""
        return self.word_list[randrange(0, len(self.word_list),1)]

    def read_file(self, path):
        """Reads the input file and stores every word into a list"""
        file = open(path, "r")

        for line in file:
            line = line.rstrip()
            self.word_list.append(line)
            self.words_read+=1
        
        file.close()
