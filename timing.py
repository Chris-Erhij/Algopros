import timeit
from timeit import Timer
from typing import List, Dict
import random


def test1() -> List[int]:
    z = []
    for ii in range(1000):
        z += [ii]
    return z


def test2() -> List[int]:
    z = [ii for ii in range(1000)]
    return z


def test3() -> List[int]:
    return list(range(1000))


def test4() -> List[int]:
    x: List = []
    for ii in range(1000):
        x.append(ii)
    return x


def empty():
    pass


timer_empty: Timer = timeit.Timer('empty()', "from __main__ import empty")
time_empty = timer_empty.timeit(number=1000)
print("Time it takes to run an empty function", time_empty)

timer_test1: Timer = timeit.Timer('test1()', "from __main__ import test1")
# print("Concatenation: {:>5.17f}".format(timer_test1.timeit(number=1000) + time_empty))

timer_test2: Timer = timeit.Timer('test2()', "from __main__ import test2")
# print(f"List comprehension: {timer_test2.timeit(number=1000) + time_empty}")

# import test3 from the timing module into the Timer environment
timer_test3: Timer = timeit.Timer('test3()', "from __main__ import test3")
# print("List constructor: %10.17f" % (timer_test3.timeit(number=1000) + time_empty))

timer_test4 = timeit.Timer('test4()', "from __main__ import test4")
# print("Append" + ':' + ' ' + str(float(timer_test4.timeit(number=1000) + time_empty)))

xl: List[int] = list(range(2000000))

pop_end0: Timer = timeit.Timer('xl.pop()', "from __main__ import xl")
# print(F"Pop end: {pop_end0.timeit(number=1000) + time_empty}")

pop_start0: Timer = timeit.Timer('xl.pop(0)', "from __main__ import xl")
# print('Pop start: %10.17f' % (pop_start0.timeit(number=1000) + time_empty))

pop_end: Timer = timeit.Timer('xf.pop()', "from __main__ import xf")
pop_start: Timer = timeit.Timer('xf.pop(0)', "from __main__ import xf")

js: str = 'for J'
lts: str = "For lt"
dts: str = "for dt"
si: str = "For i"
ranger: List[int] = [x for x in range(10000, 1000001, 20000)]

print("%10s %10s %10s %10s" % (js, si, lts, dts))
for j, i in enumerate(range(len(ranger) - 1, 0, -1)):
    l_time: Timer = timeit.Timer("random.randrange(%d) in lo" % ranger[j],
                                 "from __main__ import random, lo")

    d_time: Timer = timeit.Timer("random.randrange(%d) in do" % ranger[i], "from __main__ import random, do")

    lo: List[int] = list(range(ranger[j]))
    lt: float = l_time.timeit(number=1000)

    do: Dict = {n: None for n in range(ranger[i])}
    dt: float = d_time.timeit(number=1000)

    print("%10d %10d %10f %10f" % (ranger[j], ranger[i], lt, dt))
