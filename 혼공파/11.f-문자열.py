# 파이썬 3.1 부터 추가된 기능으로 format을 더 쉽게 사용할 수 있음 
a = 52
b = 10

print("{} + {} = {}".format(a, b, a + b))
print(f"{a} + {b} = {a+b}")

=> 결과는 똑같다! 

취향에 따라 쓰면 되지만 
전개연산자를 사용할 시에는 format함수를 사용할 때 더 좋다. 