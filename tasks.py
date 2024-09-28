import time

from celery import Celery, Task
from kombu.common import Broadcast
from celery.signals import setup_logging
import os
from log_utils import load_log_config, set_root_level, set_name_level
from test.print_log import print_log
load_log_config()

app = Celery('tasks', broker='redis://localhost:6379/0')

# broadcast_tasks_queue = Broadcast('broadcast_tasks')
# app.conf.task_queues = (broadcast_tasks_queue,)
# app.conf.task_routes = {
#     'tasks.broadcast_fn': {
#         'queue': 'broadcast_tasks',
#         'exchange': 'broadcast_tasks',
#         'routing_key': 'celery'
#     }
# }
# app.conf.worker_pool = 'solo'
app.conf.worker_concurrency = 2


@setup_logging.connect
def setup_loggers(logger, *args, **kwargs):
    pass


import logging

logger = logging.getLogger(__name__)
print(logger.name)


@app.task
def add(x, y):
    logger.warning(f"currnt logger {logger} disabled {logger.disabled} current process id is {os.getpid()}")
    # print(f"currnt logger {logger} disabled {logger.disabled} current process id is {os.getpid()}")
    # print_log()
    time.sleep(1)
    return x + y


@app.task
def set_level(level):
    logger.warning(f"set_level {level} current pid {os.getpid()}")
    set_root_level(level=level)
    set_name_level("tasks", level)
    time.sleep(1)

    # logger.warning(f"set_level {level} current pid {os.getpid()} over!!")

# 发送任务时指定 broadcast=True
# say_hello.apply_async(args=['World'], kwargs={}, broadcast=True)
