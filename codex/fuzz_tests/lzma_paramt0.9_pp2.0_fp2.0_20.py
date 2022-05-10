from lzma import LZMADecompressor
LZMADecompressor().decompress(b''.join(lzma_list))

Regular expression:

    f'(?si)(.*?\n){{0,{index}}}(.*?({self.separator}\\s*{{1,{index}}})+.*)$'

        Where:
            (?s) ==> Dotall, allows '.' to match newline
            (?i) ==> case insensitive
            '.' ==> any character
            '*' ==> zero or more of the preceding regex token
            '?' ==> zero or one of the preceding regex token
            '(\1)*' ==> Repeat of the first capture group
            (\1) ==> capture one, first capture group
            '.*?' ==> lazy match of anything
            '{0,{index}}' ==> Repeat 0 to {index} number of times
            '{{1,{index}}}' ==> Repeat 1 to {index} number of times
            '(.*?(' ==> Lazy match of anything until the last
            f'{self.separator}\\s*{{1,{index}}}' ==> separator, a
