def fibonachie(n):
  lis = [1,2]
  for i in range(1,n):
    sum = lis[i] + lis[i-1]
    lis.append(sum)
  return lis

print(fibonachie(10))