from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.counter = 0

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_head(item)
        elif self.storage.length == self.capacity:
            self.counter += 1
            self.storage.remove_from_tail()
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        if self.storage.length < self.capacity:
            temp = 0
            while temp < self.storage.length:
                list_buffer_contents.append(self.storage.tail.value)
                self.storage.move_to_front(self.storage.tail)
                temp += 1
        elif self.storage.length == self.capacity:
            temp = 0
            temp2 = 0
            temp3 = 0
            while temp2 < self.counter:
                self.storage.move_to_end(self.storage.head)
                temp2 += 1
            while temp < self.storage.length:
                list_buffer_contents.append(self.storage.tail.value)
                self.storage.move_to_front(self.storage.tail)
                temp += 1
            while temp3 < self.counter:
                self.storage.move_to_front(self.storage.tail)
                temp3 += 1

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
