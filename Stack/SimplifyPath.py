# -*- coding:UTF-8 -*
'''
给定一个文档 (Unix-style) 的完全路径，请进行路径简化。

例如，
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

边界情况:

你是否考虑了 路径 = "/../" 的情况？
在这种情况下，你需返回 "/" 。
此外，路径中也可能包含多个斜杠 '/' ，如 "/home//foo/" 。
在这种情况下，你可忽略多余的斜杠，返回 "/home/foo" 。
'''


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        file = path.split("/")
        stack = []
        for f in file:
            if f == '..':
                if len(stack) > 0:
                    stack.pop()
            elif f != '.' and f.strip() != '':
                stack.append(f)
        
        s = ""
        for fpath in stack:
            s = s + "/" + fpath
        
        if s.strip() == '':
            s = "/"

        return s


if __name__ == "__main__":
    print("Hello World!")
    test = Solution()
    print test.simplifyPath("/abc/...")