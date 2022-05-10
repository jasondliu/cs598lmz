import lzma
lzma.open('test.lzma', 'w').write(b'1234567890')
</code>
and then <code>xxd</code> to get the hex:
<code>0000000: 5d00 0000 04fb 4d05 00fc 2a20 e804 00fc  ].....M...* ....
0000010: 2a20 e804 00fc 2a20 e804 00fc 2a20 e804  * ...* ...* ...*..
0000020: 00fc 2a20 e804 00fc 2a20 e804 00fc 2a20  ..* ...* ...* ..* 
0000030: e804 00fc 2a20 e804 00fc 2a20 e804 00fc  ....* ...* ...*...
0000040: 2a20 e804 00fc 2a20 e804 00fc 2a20 e804  * ...* ...* ...*.
0000050: 00fc 2a20 e804 00fc 2a20 e804 00fc 2a20  ..* ...* ...* ..* 
0000060: e804 00fc 2a20 e804 00fc 2a20 e804 00fc 
