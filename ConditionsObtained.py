A = int(input("Enter first number :"))
B = int(input("Enter second number :"))

def is_valid(A,B):
    return A<10 and A>B

print(is_valid(A,B))
