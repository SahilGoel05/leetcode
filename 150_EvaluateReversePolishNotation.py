class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    subtrahend = stack.pop()
                    minuend = stack.pop()
                    stack.append(minuend - subtrahend)
                case "/":
                    divisor = stack.pop()
                    dividend = stack.pop()
                    stack.append(int(dividend/divisor))
                case _:
                    stack.append(int(token))
        return stack.pop()

'''
TC: O(n)
SC: O(n)

Optimal solution is basically same is this
'''
        
