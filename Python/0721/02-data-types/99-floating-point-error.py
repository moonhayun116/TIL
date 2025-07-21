# 부동소수점 에러
result = 0.1 + 0.2
print(result == 0.3)  # False
print(result)  # 0.30000000000000004


# 해결 전
a = 3.2 - 3.1
b = 1.2 - 1.1

print(a)  # 0.10000000000000009
print(b)  # 0.09999999999999987
print(a == b)  # False

# 해결 후
from decimal import Decimal

a = Decimal('3.2') - Decimal('3.1')
b = Decimal('1.2') - Decimal('1.1')

print(a)  # 0.1
print(b)  # 0.1
print(a == b)  # True
