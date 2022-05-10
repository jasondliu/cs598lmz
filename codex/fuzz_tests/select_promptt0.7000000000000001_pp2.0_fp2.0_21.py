import select
# Test select.select
import select_tests

# Test select.kqueue
import kqueue_tests

# Test select.poll
import poll_tests

# Test select.epoll
import epoll_tests

# Test select.devpoll
import devpoll_tests

print 'Test select'
select_tests.start()

print 'Test select.kqueue'
kqueue_tests.start()

print 'Test select.devpoll'
devpoll_tests.start()

print 'Test select.poll'
poll_tests.start()

print 'Test select.epoll'
epoll_tests.start()
