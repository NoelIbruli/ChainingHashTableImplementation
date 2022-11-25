class ChainingHash:

    # This is a single record in a chaining hash table.  You can
    # change this in anyway you wish (including not using it at all)
    class Record:
        def __init__(self, key = None, value=None):
            self.key = key
            self.value = value

    # You cannot change the function prototypes below.  Other than that
    # how you implement the class is your choice (but it must be a hash
    # table that use chaining for collision resolution)

    def __init__(self, cap=32):
        self.cap = cap
        self.size = 0
        self.arr = [[] for i in range(self.cap)]

    def insert(self,key, value):
        if (self.search(key)!=None): 
            return False

        if(len(self) >= self.cap):
            self.resize()   
        index = self.hash(key)
        self.arr[index].append(self.Record(key,value)) 
        self.size+=1
        return True
        


    def modify(self, key, value):
        index = self.hash(key) 

        for i in self.arr[index]: 
            if i.key == key:
                i.value = value
                return True

        return False

    def remove(self, key):
        temp = self.cap  
        
        while temp > 0 : 
            index = hash(key) % temp  
            i=0
            while i < len(self.arr[index]): 
                if self.arr[index][i].key == key: 
                    self.arr[index].pop(i)
                    self.size-=1

                    return True
                i+=1
            temp //=2

        return False

    def search(self, key):
        temp = self.cap  
        while temp > 0 : # loop until the capacity of the hash table is 0
            index =  hash(key)  % temp   
            for i in self.arr[index]: # loop through the list of the index
                if i.key == key:
                    return i.value 	# return the found key
            temp //= 2

        return None

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.size

    def resize(self):
        temp = [[] for i in range(self.cap*2)]
        for i in range(self.cap):
            temp[i]=self.arr[i]
        self.arr = temp
        self.cap *= 2	

    def hash(self,key):
        return hash(key) % self.cap
