# Gadaguer Leon Student ID: 001012434
class HashMap:
    def __init__(self):
        # Set the size of the default array to 64 in order to avoid collisions
        self.size = 64
        # Initialized the map array to none for each cell so that Python would construct a list with a fixed length
        self.map = [None] * self.size

    # Private _get_hash function takes in a key to calculate the index for the key and will return the index
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    # The insert function takes in a key and a value in order to add key-value pairs into the Hash Map
    def insert(self, key, value):
        # The index value that the key will be inserted into is calculated using the _get_hash function above
        key_hash = self._get_hash(key)
        # The key_value is what will be inserted into the calculated index's cell. Essentially, it constructs a list
        # from the key and the value that are passed in
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def update(self, key, value):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('There was an error with updating on key: ' + key)

    # The get function gets the key hash when given a key in order to return the value within the cell
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # The delete function gets the key hash when given a key in order to return the index for the key and remove the
    # value from the cell
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    # The print function is used to print out the contents of the hash map to the console when called upon
    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))
