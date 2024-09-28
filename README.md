# celery-logging-test

a workaround to control logging level in multiple celery workers
using builtin logging module for logger, using group tasks to change the logger level in every worker node.

### setup redis
> docker run -p 6379:6379 redis

### setup celery worker
> celery -A tasks worker

### send tasks to celery and view log level in celery console or output file
> python main.py 