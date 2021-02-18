class Node:
    """
    Class of a single node (element) of the linked list
    """
    def __init__(self, word, next=None):
        self.word = word  # field for data storage
        self.count = 1
        self.next = next  # field for linked list in queue


class FreqLinkedList():
    """
    Linked list class constructor
    """
    def __init__(self):
        self.head = None

    def addWord(self, word):
        """
        Add a word to the linked list
        """
        # if no items in the list
        if not self.head:
            self.head = Node(word)
            return True

        # if word should be previous to the head
        if word < self.head.word:
            self.head = Node(word, next=self.head)
            return True

        item = self.head
        # looking for a place of the word
        while item.next:
            if item.word == word:
                # if word is already in the list
                item.count += 1
                return True
            if (item.word < word) & (word < item.next.word):
                # if the place is found
                nd = Node(word, next=item.next)
                item.next = nd
                return True
            item = item.next
        # if the end is reached
        if item.word == word:
            item.count += 1
        else:
            item.next = Node(word, next=item.next)
        return True

    def printList(self):
        """
        Prints the list
        :return:
        """
        item = self.head
        while item.next:
            print('{:s}   {:d}'.format(item.word, item.count))
            item = item.next
        print('{:s}   {:d}'.format(item.word, item.count))

    def filterWords(self, n):
        """
        Filters the words in the list
        :param n: minimum frequency to accept
        :return: None
        """
        # looking for  the first element of the filtered list
        while self.head.count < n:
            self.head = self.head.next

        # main loop of the filtering
        item = self.head
        while item.next:
            if item.next.count < n:
                item.next = item.next.next
            else:
                item = item.next












