import sys

# Command line 인자로 전달받은 숫자를 정수로 변환
number = int(sys.argv[1])

# 1부터 number까지 반복하며 약수 찾기
for i in range(1, number + 1):
    # 나머지 연산자(%)를 사용해 나누어떨어지는지(약수인지) 확인
    if number % i == 0:
        print(i, end=" ")

print()  # 줄바꿈