# -*- coding:UTF-8 -*-
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for index in range(len(s)):
            if len(stack) == 0:
                stack.append(s[index])
                continue
            
            if self.isClose(stack[len(stack) - 1], s[index]) == False:
                stack.append(s[index])
            else:
                stack.pop()
        
        if len(stack) > 0:
            print 'false'
            return False
        else:
            print 'true'
            return True
            
    
    def isClose(self, a, b):
        if (a == '(' and b == ')'):
            return True
        
        if (a == '{' and b == '}'):
            return True

        if (a == '[' and b == ']'):
            return True

        return False
            
            


if __name__ == "__main__":
    print("Hello World!")
    test = Solution()
    print test.isValid("()")