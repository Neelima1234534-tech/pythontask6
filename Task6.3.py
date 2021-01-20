# YIELD,GENERATORS,NEXT
YIELD:

yield is a keyword in Python that is used to return from a function without destroying
the states of its local variable and when the function is called, the execution starts
from the last yield statement. Any function that contains a yield keyword is termed as generator.
Hence, yield is what makes a generator. yield keyword in Python is less known off but has 
a greater utility which one can think of.

GENERATORS:

Generators are very easy to implement, but a bit difficult to understand.
Generators are used to create iterators, but with a different approach.
Generators are simple functions which return an iterable set of items, one at a time, in a special way.
When an iteration over a set of item starts using the for statement, the generator is run.
Once the generator's function code reaches a "yield" statement, 
the generator yields its execution back to the for loop, returning a new value from the set.
The generator function can generate as many values (possibly infinite) as it wants,
yielding each one in its turn.

NEXT:

The next () function returns the next item from the iterator. If the iterator is exhausted, 
it returns the default value passed as an argument. If the default parameter is omitted and the iterator
is exhausted, it raises StopIteration exception. A list is an iterable and you can get its iterator
from it by using the iter () function in Python.

