# 期中題目六: Stack的定義及其應用（python）
## 11024137 許珀溫     11024121 李偉杰

# Stack 是什麼？
Stack（堆疊）是線性資料結構中的一種主要抽象資料型別，其核心特性是 LIFO（Last In, First Out）後進先出。也就是說，最後放入的資料會最先被取出，這種特性在資料處理上常被稱為「反轉順序」。

# Stack 可以應用在哪些情境？
## Stack 結構在多種演算法與實際應用中扮演重要角色，常見的應用包括：

括號匹配問題 

十進位轉換為其他進位（如二進位）

中綴表達式轉後綴表達式

後綴表達式求值

這些問題都利用 Stack 的 LIFO 特性來有效解決，對於理解資料結構與演算法設計非常重要。

# Stack 的基本操作
## 在 Python 中實作 Stack 類別時，通常會定義以下五種基本功能
| 方法           | 說明         |
| ------------ | ------------ |
| `size()`   | 回傳目前堆疊中元素的數量 |
| `is_empty()`     | 判斷堆疊是否為空      |
| `push(data)	`      | 將資料壓入堆疊頂部    |
| `pop()`     | 	移除並回傳堆疊頂部的資料  |
| `peek()` | 查看堆疊頂部的資料但不移除      |

#  Stack 類別實作（Python 範例）
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
# 使用範例
<pre>
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.peek())
print(s.size())

popped_item = s.pop()
print(popped_item)
print(s.peek())
print(s.is_empty())
</pre>

#輸出結果

![01](https://github.com/XUPOWEN/Stack/blob/main/code.png)

