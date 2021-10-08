class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return str(self.data)


class DoublyLinkedNode(Node):
    def __init__(self, data=None, next_node=None, prev_node=None):
        super.__init__(self, data=data, next_node=next_node)
        self.prev_node = prev_node


class SinglyLinkedList:
    def __init__(self, *args):
        '''
        Initialises the SinglyLinkedList. If any arguments are passed they will be added to the list
        '''
        self.head = None
        self.tail = None
        self.size = 0
        if args:
            self.head = Node(data=args[0])
            self.tail = self.head
            self.size = 1
            if len(args) > 1:
                self.append(*args[1:])

    def __repr__(self):
        '''
        Traverses the list and return a simple illustration of all its items
        '''
        current = self.head
        result = ''
        if self.size == 0:
            return '[]'
        while current:
            result += f'[{current.data}]'
            if current.next_node:
                result += ' -> '
            current = current.next_node
        return result

    def __add__(self, data):
        pass

    def __iter__(self):
        '''
        Returns itself and sets 'self.current' to 'self.head'
        '''
        self.current = self.head
        return self

    def __next__(self):
        '''
        Returns the next node
        '''
        if self.current:
            node = self.current
            self.current = self.current.next_node
            return node
        else:
            raise StopIteration

    def __len__(self):
        '''
        Returns the number of items the list holds
        '''
        return self.size

    def __contains__(self, value):
        '''
        Checks if a value exists within the list
        '''
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next_node
        return False

    def append(self, *args):
        '''
        Appends all arguments passed
        '''
        self.size += len(args)
        for i in args:
            self.tail.next_node = Node(data=i)
            self.tail = self.tail.next_node

        return self

    def prepend(self, *args):
        '''
        Prepends all arguments passed
        '''
        self.size += len(args)
        for i in args[::-1]:
            current = Node(data=i)
            current.next_node = self.head
            self.head = current

        return self

    def reverse(self):
        '''
        Reverses itself 
        '''
        temp = SinglyLinkedList()
        current = self.head
        while current:
            temp.prepend(current)
            current = current.next_node
        self.head = temp.head

        return self

    def clear(self):
        '''
        Sets the properties back to the default
        '''
        self.head = None
        self.size = 0
        self.tail = None

        return self

    def copy(self):
        '''
        Returns a copy of this list with the class of 'SinglyLinkedList'
        '''
        return SinglyLinkedList(*[i for i in self])

    def count(self, value):
        '''
        Traverses the list to find the amount of time a value occurs
        '''
        count = 0
        current = self.head
        while current:
            if type(current.data) == type(value):
                if current.data == value:
                    count += 1
            current = current.next_node
        return count

    def index(self, value):
        '''
        Returns the index of the first matching value
        '''
        index = 0
        current = self.head
        if value not in self:
            raise ValueError('Value not in SinglyLinkedList')
        while current:
            if type(current.data) == type(value):
                if current.data == value:
                    return index
            index += 1
            current = current.next_node

    def pop(self):
        '''
        Removes and returns the last item
        '''
        node = self.tail
        current = self.head
        if self.head is self.tail:
            self.head, self.tail = None, None
            self.size -= 1
            return node
        while current:
            if current.next_node is self.tail:
                current.next_node = None
                self.size -= 1
                return node
            current = current.next_node

    def extend(self, obj):
        '''
        Adds all items of another SinglyLinkedList to this one
        '''
        if not isinstance(obj, SinglyLinkedList):
            raise TypeError('Object is not SinglyLinkedList')
        else:
            self.append(*[i for i in obj])

    def insert(self, index, *args):
        '''
        Inserts all arguments starting at the index given.
        '''
        current = self.head
        current_index = 0
        if index > self.size - 1:
            raise ValueError('Index exceeds size of SinglyLinkedList')
        while current:
            if current_index + 1 == index:
                temp = current.next_node
                for i in args:
                    current.next_node = Node(data=i)
                    current = current.next_node
                current.next_node = temp
                break
            current = current.next_node
            current_index += 1
        return self


if __name__ == '__main__':
    ll = SinglyLinkedList(1, True, 'Hello', [1, 2, 3], {
        '2': 3, '4': 4}, None, 12.2)
    ll.append(*[1, 2, 3, 4])
    ll.prepend(*{1, 2, 3, 4})

    print(dir([1, 2, 3]))
    # lst = [1, 2, 3]
    # lst += [1]
    # print(lst)
    # print(ll)
    # print(ll.pop())
    # print(ll)
    print(ll)
    print(ll.insert(3, *['w', 0, None, [1, 2, 3], 12.1]))
