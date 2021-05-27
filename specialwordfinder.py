import wordfinder

class SpecialWordFinder(wordfinder.WordFinder):
    """
    >>> w = SpecialWordFinder('foods.txt')
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

        super().__init__(path)

    def read_file(self, path):
        """Reads the input file and stores every word into a list"""
        file = open(path, "r")

        for line in file:
            line = line.rstrip()
            
            if line != '' and line[0] != '#': #python will throw error if line[0] is
                #put 1st b/c it evals ''[0] empty string as not existing
                self.word_list.append(line)
                self.words_read+=1

        file.close()


