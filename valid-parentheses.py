class Solution:
    def isValid(self, s: str) -> bool:
        list_chars = []
        for char in s:
            if char == '(' or char == '{' or char =='[':
                list_chars.append(char)
            else:
                if list_chars == []:
                    return False
                a = list_chars[-1]
                if a == '(' and char == ')':
                    list_chars.pop()
                elif a == '{' and char == '}':
                    list_chars.pop()
                elif a == '[' and char == ']':
                    list_chars.pop()        
        if list_chars == []:
            return True
        else:
            return False       