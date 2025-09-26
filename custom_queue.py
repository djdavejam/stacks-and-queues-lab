import random

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the end of the queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the item from the front of the queue"""
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        return self.items.pop(0)
    
    def peek(self):
        """Return the item at the front of the queue without removing it"""
        if self.is_empty():
            raise IndexError("Cannot peek empty queue")
        return self.items[0]
    
    def is_empty(self):
        """Return True if the queue is empty"""
        return len(self.items) == 0
    
    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            raise IndexError("Cannot select winner from empty queue")
        
        # Select a random index from the current queue
        winner_index = random.randint(0, len(self.items) - 1)
        winner = self.items[winner_index]
        
        # Dequeue all customers up to and including the winner
        for _ in range(winner_index + 1):
            self.dequeue()
        
        return winner