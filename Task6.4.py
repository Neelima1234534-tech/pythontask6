
  def my_gen():
      n = 1
      print('This is printed first')
    # Generator function contains yield statements
        yield n
        n += 1
      print('This is printed second')
        yield n
  def reverseGenerator(my_gen):
        new = [i for i in my_gen]
        yield new[::-1][0]
        new.pop()
        yield from reverseGenerator(i for i in new)
