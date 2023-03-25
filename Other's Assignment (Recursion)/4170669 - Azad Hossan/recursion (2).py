 
def head_recursion (n):
    if n == 0:
        return n
    return (n)+ head_recursion(n - 1)
         
print(head_recursion(10))
