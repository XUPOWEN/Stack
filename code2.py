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
