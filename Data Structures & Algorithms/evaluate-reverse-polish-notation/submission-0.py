class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in {"+", "-", "*", "/"}:
                a = stack.pop()   # right operand
                b = stack.pop()   # left operand
                if c == "+": stack.append(b + a)
                elif c == "-": stack.append(b - a)
                elif c == "*": stack.append(b * a)
                else:             # division truncates toward 0
                    stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]
