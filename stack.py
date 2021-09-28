"""we build the class from scartch without any exterior package."""


class stack:
    """Implemenation of the stack(lifo) using the list python."""

    def __init__(self, data=[]):
        """Inisialtion and creaton of instance."""
        self._data = data

    def __len__(self):
        """Return a number of item in the  stack."""
        return len(self._data)

    def is_empty(self):
        """Test if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Adding new element in the top of the stack."""
        self._data.append(e)

    def top(self):
        """Return the top element in the stack without.

        remove it from the stack
        """
        if self.is_empty():
            raise Empty('stack is empty ')
        return self._data[-1]

    def pop(self):
        """Return the top elemnet in the stack and remove it from the stack."""
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data.pop()

    def __repr__(self):
        """Represt the stack in readable forme."""
        return str(self._data)

# application of the stack in simple example
# for a two given array A = [1,2,3,5,6]   B = [2,4,5,10,2] we have 3 couple
# we count a couple if B[i] = 2 * A[i] we try  apply rhe stack concept
# to find all couple in two given arraa


A = [1, 2, 3, 5, 6]
B = [2, 4, 5, 10, 2]
A = stack(A)

B = stack(B)
count = 0
for i in range(len(A)):
    if B.pop() == 2 * A.pop():
        count = count+1
print("number of couple is ", count)

# implementation of the stack block using  linked list


class stack_linked_list:
    """For this object we want to use linked list inseat the simple list.

    to implement the block stack.
    """

    # the class node used in construction of the stack block
    class _node:
        """A node represent a sequence of a stack have two  proprites.

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
        self._size = 0

    def __len__(self):
        """Return the size of the stack block."""
        return self._size

    def is_empty(self):
        """Test the stack block if is it empty."""
        return self._size == 0

    def push(self, e):
        """Adding the element e to the top of the stack block."""
        self._head = self._node(e, self._head)
        self._size += 1

    def top(self):
        """Return the first element  of the stack without remove it."""
        if self.is_empty():
            raise Empty('the stack block is empty')
        answer = self._head._element
        return answer

    def pop(self):
        """Return the first element and remove it from the srack block."""
        if self.is_empty():
            raise Empty('the stack block is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
