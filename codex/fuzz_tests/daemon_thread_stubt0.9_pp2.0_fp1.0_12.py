import sys, threading

def run():

  ranges = {}
  with open('/proc/vmstat') as vmstat:
    for line in vmstat:
      if line.startswith('nr_hugepages'):
        hugepagecount = int(line.split()[1])
        break

  with open('/proc/iomem') as iomem:
    for line in iomem:
      if line.startswith('HugeTLB'):
        (name, range, rest) = line.split(None, 2)
        (start, dash, size) = range.partition('-')
        range = long(size, 16) - long(start, 16) + 1
        ranges[name] = range

  hugepagesize = ranges['HugeTLB'] / hugepagecount

  def print_hugepage_info():
    while True:
      print '\n'
      print 'Hugepage size:', hugepagesize, 'bytes'
      print 'Number of hugepages:', hugepagecount

      total = 0
      with open('/proc/meminfo') as meminfo:
        for line
