class Math:
  @staticmethod
  def add(a, b):
    return a+b
  
  @staticmethod
  def sub(a, b):
    return a-b

  @staticmethod
  def div(a, b):
    return a/b

  @staticmethod
  def mul(a, b):
    return a*b

  @staticmethod
  def abs(a):
    return a * -1 if a < 0 else a

  @staticmethod
  def min(a,b):
    return a if a < b else b

  @staticmethod
  def max(a,b):
    return a if a > b else b

  @staticmethod
  def clamp(a,min,max):
    if a < min:
        return min
    elif a > max:
        return max
    else:
        return a
 