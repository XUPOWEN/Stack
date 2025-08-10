class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判斷堆疊是否為空"""
        return len(self.items) == 0

    def push(self, item):
        """將資料壓入堆疊"""
        self.items.append(item)

    def pop(self):
        """移除並回傳堆疊頂部的資料"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """查看堆疊頂部的資料但不移除"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def size(self):
        """回傳堆疊中的元素個數"""
        return len(self.items)
