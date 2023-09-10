def factorial(n):
  if (n == 0 or n == 1):

    return 1

  else:
    return n * factorial(n - 1)


num = 10
print("number:", num)
print("factorial:", factorial(num))
