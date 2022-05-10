import lzma
lzma.open(<filename>, mode='w')
```

## How does it work?

It writes the following data in the file.

```
0x04: Version
0x07: 0x00: no encryption
       0x01: AES-128
       0x02: AES-192
       0x03: AES-256
0x08: Number of Filters
0x0A: Filter ID
```

### Filter ID

Filter ID is a 16-bit value. The lower 12-bit identifies the filter.
The upper 4-bit is for the filter options.

#### Filter ID for lzma

```
0x0001: lzma1
0x0401: lzma2
```

#### Filter Options

##### lzma2

```
0x00: no options
0x01: BCJ
0x02: x86
0x03: PPC
0x04: IA64
0x05: ARM
0x06: ARM Thumb
0x07: SPARC
0x08: m68k

