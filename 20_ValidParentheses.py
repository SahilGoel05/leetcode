class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '{[(':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if c == '}' and top != '{' or c == ')' and top != '(' or c == ']' and top != '[':
                    return False
        if len(stack) == 0:
            return True
        return False

'''
TC: O(n)
SC: O(n)

Optimal Solution:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

TC: O(n)
SC: O(n)
'''
           
