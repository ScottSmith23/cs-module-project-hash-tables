class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.slots = capacity * [None]
        self.stored = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return (self.stored / self.capacity)


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        FNV_offset = 14695981039346656037
        FNV_prime = 1099511628211

        hashed_var = FNV_offset

        string_bytes = key.encode()

        for b in string_bytes:
            hashed_var = hashed_var * FNV_prime
            hashed_var = hashed_var ^ b

        return hashed_var


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # slot = self.hash_index(key)
        # self.slots[slot] = HashTableEntry(key,value)

        #if slot is empty
        slot = self.hash_index(key)
        
        if not self.slots[slot]:
            self.slots[slot] = HashTableEntry(key,value)
            self.stored += 1
        #else update value for existing key or create new entry
        else:
            current_node = self.slots[slot]

            while current_node.key != key and current_node.next:
                current_node = current_node.next
            # if key exists update value
            if current_node.key == key:
                current_node.value = value

            #no key found add new entry
            else:
                current_node.next = HashTableEntry(key,value)
                self.stored += 1
        
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)







    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # self.put(key,None)

        slot = self.hash_index(key)

        current_node = self.slots[slot]

        #no value at index
        if not current_node:
            print("No value at slot")

        elif not current_node.next:
            self.slots[slot] = None
            self.stored -= 1

        else:

            prev_node = None

            while current_node.key != key and current_node.next:
                prev_node = current_node
                current_node = current_node.next

            if not current_node.next:
                prev_node.next = None
                self.stored -= 1

            else:
                prev_node.next = current_node.next
                self.stored -= 1

        if self.get_load_factor() < 0.2:
            new_capacity = self.capacity // 2

            if new_capacity < MIN_CAPACITY:
                new_capacity = MIN_CAPACITY

            self.resize(new_capacity)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # slot = self.hash_index(key)
        # hash_entry = self.slots[slot]

        # if hash_entry is not None:
        #     return hash_entry.value

        # return None

        slot = self.hash_index(key)

        if self.slots[slot]:
            current_node = self.slots[slot]
            #move to next node if key not matching
            while current_node.key != key and current_node.next:
                current_node = current_node.next
            #reach end without matching key
            if not current_node.next:
                return current_node.value
            #returns node value when key matches
            else:
                return current_node.value
        #no match found returns none
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        getslots = self.slots

        #create new table
        self.capacity = new_capacity
        self.slots = [None] * new_capacity

        #add old data to new hash
        for slot in getslots:
            if slot:
                current_node = slot

                while current_node:
                    self.put(current_node.key,current_node.value)

                    current_node = current_node.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
