"""we create a adapter for queue using python."""


class queue:
    """the queue abstract data type defines a.

    collection that keeps objects in a.
    sequence, where element access and deletion.
    are restricted to the first element in.
    the queue, and element insertion is.
    restricted to the back of the sequence. This.
    restriction enforces the rule that items.
    are inserted and deleted in a queue accord.
    ing to the first-in, first-out (FIFO) principle.
    """

    default_length = 10

    def __int__(self):
        """We introduice the parametre of the instance.

        data : the maximue size  of the queue.
        size : the number of item in queue.
        front: index where the queue start.
        """
        self._data = [None]*queue.default_length
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the size of the queue."""
        return self._size

    def is_empty(self):
        """Test if the queue is already empty."""
        return self._size == 0

    def first(self):
        """Return the first element without remove it."""
        if self.is_empty():
            raise Empty('is empty queue')
        return self._data[self._front]

    def dequeue(self):
        """Return the first element and remove it from the queue."""
        if self.is_empty():
            raise Empty('is empty queue')
        answer = self._data[self._front]
        self.data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, item):
        """Add new element to the block queue."""
        if self._size == len(self._data):
            self._data = resize(2 * len(self._data))
        index = (self._front + len(self._size)) % len(self._data)
        self._data[index] = item
        self._size += 1

    def resize(self, cap):
        """Resize the queue."""
        old = self._data
        self._data = [None] * cap
        index = self._front
        for i in range(self._size):
            self._data[index] = old[index]
            index = (index + 1) % len(old)
        self._front = 0


# in the second part we want to implement the queue with linked list


class queue_linked:
    """we implement the queue that have the same.

    behaivor of the first queue but with another .
    aspect.
    """

    # the class node used in construction of the queue block

    class _node:
        """A node represent a sequence of a queuequeue have two  proprites.

        element : is the element of the node.
        and next : is the next element of the current elemenet.
        """

        def __init__(self, element, next):
            """Initilisation of node object's parametre."""
            __slots__ = '_element', '_next'
            self._element = element
            self._next = next

    def __init__(self):
        """Initilisation of parametres s'object."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the size of the queue block."""
        return self._size

    def is_empty(self):
        """Test the queue block if is it empty."""
        return self._size == 0

    def first(self):
        """Return the first element  of the queue without remove it."""
        if self.is_empty():
            raise Empty('the queue block is empty')
        answer = self._head._element
        return answer

    def enqueue(self, e):
        """Adding new element to the queue block."""
        item = queue_linked._node(e, None)
        if self.is_empty():
            self._head = item
        else:
            self._tail._next = item
        self._tail = item
        self._size += 1

    def dequeue(self):
        """Return the last element base on prenncipe of fifo."""
        if self.is_empty():
            raise Empty('the queue block is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
