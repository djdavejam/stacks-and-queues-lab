# Stacks and Queues Lab

A Python implementation of stack and queue data structures with practical applications.

## Features

### Stack Implementation
- **Parentheses Validator**: Checks if parentheses `()`, `{}`, `[]` are properly balanced
- Uses LIFO (Last-In, First-Out) principle

### Queue Implementation  
- **Customer Raffle System**: Manages customer entries and selects random winners
- Uses FIFO (First-In, First-Out) principle
- Methods: `enqueue()`, `dequeue()`, `peek()`, `is_empty()`, `select_and_announce_winner()`

## Files

- `custom_stack.py` - Stack-based parentheses validator
- `custom_queue.py` - Queue class with raffle functionality  
- `test_structures.py` - Test suite for both implementations

## How to Run

### Run Tests
```bash
python test_structures.py
```

### Example Usage

```python
# Stack - Parentheses Validator
from custom_stack import is_valid_parentheses

print(is_valid_parentheses("({[]})"))  # True
print(is_valid_parentheses("([)]"))    # False

# Queue - Customer Raffle
from custom_queue import Queue

q = Queue()
q.enqueue("Alice")
q.enqueue("Bob") 
q.enqueue("Charlie")

winner = q.select_and_announce_winner()
print(f"Winner: {winner}")
```

## Requirements

- Python 3.x
- No external dependencies required

## Status

✅ All tests passing  
✅ Ready for submission