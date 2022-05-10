import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os

class LinkedList(object):
  __slots__ = ['head', 'tail', 'lock']
  def __init__(self):
    self.head = None
    self.tail = None
    self.lock = threading.Lock()
  def remove(self, elem):
    prev = elem.prev
    next = elem.next
    if prev: prev.next = next
    if next: next.prev = prev
  def add_to_tail(self, elem):
    if self.head is None:
      self.head = elem
    else:
      self.tail.next = elem
    elem.prev = self.tail
    elem.next = None
    self.tail = elem
  def remove_from_head(self):
    if self.head is None:
      return None
    elif self.head == self.tail:
      result = self.head
      self.head = self.tail = None
      return result
    else:
      result = self.head
