"""
My datastructure to optimize the circuit inside the problem set. Using a profiler like cProfile, 
we could see that the initial performance bottleneck came from the min() function, which needed O(n) time to find the minimum. 
So using the minheap datastructure you could bring the cost to O(1).
"""

class PriorityQueue:
    """Array-based priority queue implementation."""

    def __init__(self):
        """Initially empty priority queue."""
        self.array = []
        self.min_index = None
        self.last_index = 0

    def __len__(self):
        # Number of elements in the queue.
        return len(self.array)

    # cost(O(n))
    def min_heapify(self, index_node):
        # aka trickleDown, this method works to correct a max heap when there is ONE violation  exactly (or zero).
        # we define our index as beginning at 0 for the 2 formulas below to hold.
        children1 = 2 * index_node + 1
        children2 = 2 * index_node + 2

        if children1 > self.last_index:
            pass

        elif children1 <= self.last_index < children2:
            if self.array[index_node] > self.array[children1]:
                self.array[index_node], self.array[children1] = self.array[children1], self.array[index_node]
                self.min_heapify(children1)
            else:
                pass
        elif children1 <= self.last_index and children2 <= self.last_index:
            min_child = min(self.array[children1], self.array[children2])
            if self.array[index_node] > min_child:
                min_child_index = 2 * index_node + 1 + [self.array[children1], self.array[children2]].index(min_child)
                self.array[index_node], self.array[min_child_index] = self.array[min_child_index], self.array[
                    index_node]
                self.min_heapify(min_child_index)
            else:
                pass

    # cost(O(n))
    def buildMinHeap(self):
        for i in range(int(((self.last_index - 1) / 2)), -1, -1):
            self.min_heapify(i)

    # cost O(1)
    def min(self):
        if len(self.array) > 0:
            return self.array[0]
        else:
            print("Your heap is empty")
            return None

    # cost O(lg(n)) and remove min element
    def pop(self):
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        min_element = self.array[-1]
        self.array.pop()
        self.last_index = len(self.array) - 1
        self.min_heapify(0)
        return min_element

    # cost O(lg(n)) as we need to ''trickle up'' the value added, if it is the biggest element.
    def append(self, element):
        self.array.append(element)
        self.trickle_up(len(self.array) - 1)

    def trickle_up(self, index):
        if index == 0:
            return
        index_parent = int((index - 1) / 2)
        if self.array[index] < self.array[index_parent]:
            self.array[index], self.array[index_parent] = self.array[index_parent], self.array[index]
            self.trickle_up(index_parent)
