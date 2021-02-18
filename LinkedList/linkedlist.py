class Node:
    """
    Class of a single node (element) of the linked list
    """
    def __init__(self, word, next=None):
        self.word = word  # field for data storage
        self.count = 1
        self.next = next  # field for linked list in queue


class FreqLinkedList():
    def __init__(self):
        self.head = None

    def addWord(self, word):
        if not self.head:
            self.head = Node(word)
            return True
        if word < self.head.word:
            self.head = Node(word, next=self.head)
            return True

        item = self.head
        while item.next:
            if item.word == word:
                item.count += 1
                return True
            if (item.word < word) & (word < item.next.word):
                nd = Node(word, next=item.next)
                item.next = nd
                return True
            item = item.next
        if item.word == word:
            item.count += 1
        else:
            item.next = Node(word, next=item.next)
        return True

    def printList(self):
        item = self.head
        while item.next:
            print('{:s}   {:d}'.format(item.word, item.count))
            item = item.next
        print('{:s}   {:d}'.format(item.word, item.count))

    def filterWords(self, n):
        while self.head.count < n:
            self.head = self.head.next
        item = self.head
        while item.next:
            if item.next.count < n:
                item.next = item.next.next
            else:
                item = item.next












