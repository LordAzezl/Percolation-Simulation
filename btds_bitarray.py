import numpy as np

class btds_bitarray():
    size=0
    def __init__(self, string):
        if type(string) == type(10):
            self.size = string
        else:
            self.size = len(string)
        if self.size%8==0 or self.size < 8 :
            if self.size < 8:
                self.store = np.zeros(1, np.byte)
            else:
                self.store = np.zeros(self.size//8, np.byte)
        else:
            self.store = np.zeros(self.size//8 + 1, np.byte)    
        self._bp = np.array([0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80], np.byte)
        if type(string) == type(10):
            return
        for i in range(len(string)):
            if string[i] == False or string[i] == '' or string[i] == '0' or string[i] == None:
                self[i] = False
            else:
                if type(string[i]) == type({}) and len(string[i]) == 0:
                    self[i] = False
                else:
                    self[i] = True
    def __getitem__(self, key):
        return self.store[key // 8] & self._bp[key % 8]
    def __setitem__(self, key, value):
        if value:
            self.store[key // 8] = self.store[key // 8] | self._bp[key % 8]
        else:
            self.store[key // 8] = self.store[key // 8] & ~self._bp[key % 8]
    def btds_any(self):  #True when any bit in the array is True	bool
        for i in range(self.size):
            if self.store[i]:
                return True
    def all(self):	#True when all bits in the array are True	bool
        pass
    def append(self, item): #	Append the truth value bool(item) to the end of the bitarray	–
        pass
    def bytereverse(self):	#   Reverses the bit order in place	–
        pass
    def clear(self):        #	Empties the bitarray	–
        pass
    def copy(self):         #	Copies the bitarray	bitarray
        pass    
    def count(self, value=True, start=0, stop=-1):  #	Counts the frequency of a bool value	int
        pass    
    def extend(self, obj):	#Extends the bitarray	–
        pass    
    def fill(self): #	Adds 0s to the end of bitarray to make it a multiple of 8	int
        pass    
    def index(self, value, start=0, stop=-1):    #	Finds the index of the first occurrence of the given bool value	int
        pass    
    def insert(self, index, value): #	Inserts a bool value in the given index	–
        pass    
    def invert(self, index):    #	Inverts all bits in place	–
        pass    
    def itersearch(self, bitarray):	#Searches for the given bitarray	iterartor
        pass    
    def length(self):   #	Gives the length of the bitarray	int
        return len(self.store)    
    def pop(self, index=-1):    #	Deletes and returns the ith element	item
        pass    
    def remove(self, value):    #	Remove the first occurrence of given bool value	–
        pass    
    def reverse(self):          #	Reverses the order of bits in place	–
        pass    
    def sort(self, reverse=False):  #	Sorts the bits in place
        pass       