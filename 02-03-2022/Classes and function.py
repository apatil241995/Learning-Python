class Calculator:

  def add(self, *args):
   sum = 0
   for i in args:
     sum += i
   return sum

  def sub(self, a,b):
   if a > b:
     return a - b
   else:
     return b - a
  def mul(self, *args):
   ans = 1
   for i in args:
     ans *= i
   return ans

  def div(self, a, b):
   return a/b
