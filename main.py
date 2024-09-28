# This is a sample Python script.
import time

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from celery import group

from tasks import add, set_level
from itertools import repeat

# add.apply_async(args=[4, 4], queue='broadcast_tasks',routing_key='broadcast_tasks')
# add.apply_async(args=[4, 4], queue='broadcast_tasks')
# broadcast_fn.delay(4, 4)
import random

group_numbers = 10
numbers = repeat((random.Random().randint(0, 10), random.Random().randint(0, 10)), group_numbers)
res = group(add.s(i, j) for i, j in numbers).apply_async()

time.sleep(3)
group(set_level.s("DEBUG") for i in range(2)).apply_async()
time.sleep(3)
numbers = repeat((random.Random().randint(0, 10), random.Random().randint(0, 10)), group_numbers)
group(add.s(i, j) for i, j in numbers).apply_async()


time.sleep(3)
group(set_level.s("WARNING") for i in range(2)).apply_async()
time.sleep(3)
numbers = repeat((random.Random().randint(0, 10), random.Random().randint(0, 10)), group_numbers)
group(add.s(i, j) for i, j in numbers).apply_async()


time.sleep(3)
group(set_level.s("INFO") for i in range(2)).apply_async()
time.sleep(3)
numbers = repeat((random.Random().randint(0, 10), random.Random().randint(0, 10)), group_numbers)
group(add.s(i, j) for i, j in numbers).apply_async()


