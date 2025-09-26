def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    
    Uses a stack to track opening brackets and match them with closing ones.
    """
    # Stack to keep track of opening brackets
    stack = []
    
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.append(char)
        # If it's a closing bracket
        elif char in ')}]':
            # Check if stack is empty (no matching opening bracket)
            if not stack:
                return False
            # Check if the top of stack matches the current closing bracket
            if stack.pop() != bracket_map[char]:
                return False
    
    # If stack is empty, all brackets were properly matched
    return len(stack) == 0