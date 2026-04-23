more = [x + 1 for x in [1,2,3,4]]     # List, in order, the values that x takes at each step.
                                      # x = 2, x = 3, x = 4, x = 5
print()                               # What is the value of more at this point?
                                      # more = [2, 3, 4, 5]
def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and
                                           # the corresponding return value.
                                           # 1, 4, 9, 16

squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print()                                    # values recorded above?
                                           # squares = [1, 4, 9, 16], it squares each value in the list and creates a new list

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value.
                                             # n = 0 -> false, 1 -> false, 2 -> false, 3-> true, 4-> true

answer = [x for x in range(5) if check(x)]   # What is the value of answer? answer = [false, false, false, true, true]
print()

def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and
                                             # the corresponding return value.
                                             # m = 0->1,1->2, 2->3, 3->4, 4->5

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value.
                                             # n = 1, 2, 3, 4, 5

answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? answer = [4, 5]
print()