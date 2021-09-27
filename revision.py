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
