class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self, *args):
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
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            node = self.current
            self.current = self.current.next_node
            return node
        else:
            raise StopIteration

    def __len__(self):
        return self.size

    def __contains__(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next_node
        return False

    def append(self, *args):
        self.size += len(args)
        for i in args:
            self.tail.next_node = Node(data=i)
            self.tail = self.tail.next_node

        return self

    def prepend(self, *args):
        self.size += len(args)
        for i in args[::-1]:
            current = Node(data=i)
            current.next_node = self.head
            self.head = current

        return self

    def reverse(self):
        temp = SinglyLinkedList()
        current = self.head
        while current:
            temp.prepend(current)
            current = current.next_node
        self.head = temp.head

        return self

    def clear(self):
        self.head = None
        self.size = 0
        self.tail = None

        return self

    def copy(self):
        return SinglyLinkedList(*[i for i in self])

    def count(self, value):
        count = 0
        current = self.head
        while current:
            if type(current.data) == type(value):
                if current.data == value:
                    count += 1
            current = current.next_node
        return count

    def index(self, value):
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
        if not isinstance(obj, SinglyLinkedList):
            raise TypeError('Object is not SinglyLinkedList')
        else:
            self.append(*[i for i in obj])

    def insert(self, index, data):
        current = self.head
        current_index = 0
        if index > self.size - 1:
            raise ValueError('Index exceeds size of SinglyLinkedList')
        while current:
            if current_index + 1 == index:
                temp = current.next_node
                current.next_node = Node(data=data)
                current.next_node.next_node = temp
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
    print(ll.insert(3, 't'))
