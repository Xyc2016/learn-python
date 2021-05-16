loc = {}
from collections import deque


def inner_gen():
    # dq = deque([None, None], maxlen=2)
    store_1, store_2 = None, None
    a = yield
    while True:
        store_1, store_2 = store_2, (yield store_1)
        loc["locals"] = locals()


def learn_yield_from(gen):
    while True:
        o = yield from gen
        print(o)


gen = inner_gen()
outer_gen = learn_yield_from(gen)
