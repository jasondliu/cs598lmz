import lzma
lzma_d = lzma.decompress(open(sys.argv[1], 'rb').read())
print(lzma_d.decode('utf-8'))

# systemctl start serial-getty@ttyS0
# systemctl start getty\@tty1
# systemctl start getty\@tty2
# systemctl start getty\@tty3
# systemctl start getty\@tty4
