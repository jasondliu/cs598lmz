import select
# Test select.select()
from select import select
# Test select.poll()
from select import poll, POLLIN
# Test select.epoll()
from select import epoll, EPOLLIN
from select import EPOLLOUT
from select import EPOLLHUP
from select import EPOLLERR
from select import EPOLL_CLOEXEC
from select import EPOLLET
from select import EPOLLONESHOT
# Test select.kqueue()
from select import kqueue, KQ_EV_ADD, KQ_EV_ENABLE, KQ_EV_EOF, KQ_EV_ERROR, KQ_EV_ONESHOT, KQ_EV_SUB, KQ_EV_UDATA, KQ_NOTE_LINK, KQ_NOTE_RENAME, KQ_NOTE_WRITE
# datetime
from datetime import datetime
from datetime import timedelta
from datetime import timezone
# syslog
from syslog import LOG_AUTH
from syslog import LOG_AUTHPRIV
from syslog import LOG_CRON
from syslog import LOG_
