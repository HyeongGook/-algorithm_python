n = int(input())
result = 0

while n > 2:
  if n % 5 == 0:
    result += 1
    n -= 5
  else:
    result += 1
    n -= 3

if n == 0:
  print(result)
else:
  print(-1)