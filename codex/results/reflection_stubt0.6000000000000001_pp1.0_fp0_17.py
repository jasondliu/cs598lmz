fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


def func():
    pass


func.__code__ = 1
func()


def func():
    pass


func.__code__ = "a"
func()


def func():
    pass


func.__code__ = [1, 2, 3]
func()


def func():
    pass


func.__code__ = {1, 2, 3}
func()


def func():
    pass


func.__code__ = {1: 2}
func()


def func():
    pass


func.__code__ = None
func()


def func():
    pass


func.__code__ = 'a'
func()


def func():
    pass


func.__code__ = (1, 2, 3)
func()


def func():
    pass


func.__code__ = {i for i in range(10)}
func()


def func():
    pass


func.__code__ = {i: i for i in range(10)}
func()


def func():

