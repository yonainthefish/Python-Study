# 파괴적이다 : 연 산 후 피연산자가 변형되는 것 
# print(a) = 10
# print(a) = 20

# 비파괴적이다.: 연산 후 피연산자가 변형되지 않는 것 
a =10
b = a + 10
# print(a) => 10

# 리스트는 원본배열도 남긴다면 크기가 클 때 메모리를 많이 잡아 먹기 때문에
# 원본배열은 남겨두지 않는다. 즉 존재 확인을 제외하고는 파괴적으로 작동

# 1. 요소 추가 : append(), insert(), extend()
a = [1,2,3,4]
#  a.append() => 가장 마지막에 요소 하나 추가 
#  a.insert() => 원하는 위치에 요소를 하나 추가 
insert(원하는위치,추가를 원하는요소) => insert(0,20)
#  a.extend([1,2,3,4]) => 가장 마지막에 요소 여러개 추가
# a = a + [1,2,3,4] => [1,2,3,4,1,2,3,4] 와 같음

# 2. 요소 제거 : del, pop(), remove(), clear()
a = [1,2,3,4]
# 1) del a[0] : 제거하고 싶은 인덱스 입력
# 2) pop(0) : 리스트의 맨 마지막 원소를 리턴하고 해당 원소는 삭제
#  pop(0) => 1번째 원소를 리턴하고 리스트에서 삭제 
# 3) remove(3) : 제거하고 싶은 요소를 입력 동일한 여러개라면 가장 처음 x만 삭제
# 4) clear() : 모든 요소를 제거

# 3. 요소 정렬 : sort()
a = [12,23,3,423,54]
# 1) a.sort() : 오름차순으로 정렬
# 2) a.sort(reverse=True) : 내림차순 정렬

# 요소 존재를 확인  : in, not in 
# 52 in a => True
# 2 in a => False
# 52 not in a => False