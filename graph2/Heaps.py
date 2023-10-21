import csv
import numpy as np
import DSALinkedList

class DSAHeapEntry:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def getPriority(self):
        return self.priority

    def setPriority(self, priority):
        self.priority = priority

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value


class DSAHeap:
    def __init__(self, capacity):
        self.heap = np.empty(capacity, dtype=object)
        self.count = 0

    def add(self, priority, value):
        if self.count >= len(self.heap):
            raise Exception("Heap is full")

        self.heap[self.count] = DSAHeapEntry(priority, value)
        self.trickleUp(self.count)
        self.count += 1

    def remove(self):
        if self.count == 0:
            raise Exception("Heap is empty")

        removed_entry = self.heap[0]
        self.count -= 1
        self.heap[0] = self.heap[self.count]
        self.trickleDown(0, self.count) #-1
        return removed_entry
    
    def is_empty(self):
        return self.count == 0
    
    def add_shop(self, shop):
        self.add(shop.get_rating(), shop)
    
    def get_sorted_shops(self):
        sorted_shops = DSALinkedList()
        while not self.is_empty():
            sorted_shop = self.remove().getValue()
            sorted_shops.append(sorted_shop)
        return sorted_shops




    def trickleUp(self, currIdx):
        parentIdx = (currIdx - 1) // 2
        while currIdx > 0 and self.heap[currIdx].getPriority() > self.heap[parentIdx].getPriority():
            self.heap[currIdx], self.heap[parentIdx] = self.heap[parentIdx], self.heap[currIdx]
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2

    def trickleDown(self, currIdx, numItems):
        lChildIdx = currIdx * 2 + 1
        rChildIdx = lChildIdx + 1

        while lChildIdx < numItems:
            largeIdx = currIdx

            if self.heap[lChildIdx].getPriority() > self.heap[largeIdx].getPriority():
                largeIdx = lChildIdx

            if rChildIdx < numItems and self.heap[rChildIdx].getPriority() > self.heap[largeIdx].getPriority():
                largeIdx = rChildIdx

            if largeIdx != currIdx:
                self.heap[currIdx], self.heap[largeIdx] = self.heap[largeIdx], self.heap[currIdx]
                currIdx = largeIdx
                lChildIdx = currIdx * 2 + 1
                rChildIdx = lChildIdx + 1
            else:
                break

    def heapify(self):
        for ii in range((self.count // 2) - 1, -1, -1):
            self.trickleDown(ii, self.count)

    def heapSort(self):
        self.heapify()
        numItems = self.count
        for ii in range(numItems - 1, 0, -1):
            self.heap[0], self.heap[ii] = self.heap[ii], self.heap[0]
            self.trickleDown(0, ii)

    def display(self):
        for i in range(self.count):
            print(self.heap[i].getPriority(), self.heap[i].getValue())



def read_from_csv(filename):
    entries = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            entries.append(DSAHeapEntry(int(row[0]), row[1]))
    return np.array(entries)


if __name__ == '__main__':
    entries = read_from_csv('RandomNames7000.csv')
    heap = DSAHeap(len(entries))
    for entry in entries:
        heap.add(entry.getPriority(), entry.getValue())
    heap.heapSort()
    heap.display()

    
    heap = DSAHeap(10)

    heap.add(10, "Alice")
    heap.add(15, "Bob")
    heap.add(5, "Charlie")
    heap.add(20, "David")

    
    heap.display()

    removed_entry = heap.remove()
    print(f"Removed entry with priority {removed_entry.getPriority()} and value {removed_entry.getValue()}")

    heap.display()

