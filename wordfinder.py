"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:    
    """Class to get words from file and have the functionality to return
        a random word.
    >>> wf = WordFinder(file = "words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    
    
    """
    

    def __init__(self, filename):
        self.words = self.get_words(filename)
        self.word_count = len(self.words)
        print(f"{self.word_count} words read")

    def get_words(self, filename):
        """gets words from file"""
        lines = self.get_file_lines(filename)
        return self.remove_line_break(lines)

    def get_file_lines(self, filename):
        """reads file and saves lines in an a list"""
        file = open(filename)
        lines=[]
        for word in file:
            lines.append(word)
        file.close()
        return lines    
    
    def remove_line_break(self, lines):
        """removes line break from every string in list"""
        words = []
        for word in lines:
            word = word.replace("\n", "")
            words.append(word)
        return words
    
    def random(self):
        """returns a random word from list"""
        return self.words[random.randint(0,self.word_count)]

class SpecialWordFinder(WordFinder):
    """Class for word documents that have comments and blank lines"""
    def __init__(self, filename):
        super().__init__(filename)
    
    def get_words(self, filename):
        """gets valid words from file"""
        lines = super().get_words(filename)
        return self.filter_words(lines)
        
    def filter_words(self, lines):
        """filters out invalid lines (empty or comments) from list"""
        words = []
        for word in lines:
            if word != "" and '#' not in word:
                words.append(word)
        return words
                    
                
            

