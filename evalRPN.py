#!/usr/bin/python3
import math

class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in range(0, len(tokens)):
            if (tokens[i].lstrip('-').isnumeric() == True):
                stack.append(tokens[i])
            elif (tokens[i] == "+"):
                x = stack.pop()
                y = stack.pop()
                stack.append(int(x) + int(y))
            elif (tokens[i] == "*"):
                x = stack.pop()
                y = stack.pop()
                stack.append(int(x) * int(y))
            elif (tokens[i] == "/"):
                x = stack.pop()
                y = stack.pop()
                stack.append(math.trunc(int(y) / int(x)))
            elif (tokens[i] == "-"):
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y) - int(x) )
        return stack[0]

s = Solution()
assert 9 == s.evalRPN(["2","1","+","3","*"])
assert 6 == s.evalRPN(["4","13","5","/","+"])
