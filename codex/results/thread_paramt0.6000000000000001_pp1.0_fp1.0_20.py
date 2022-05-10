import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello World\n")).start()

# del_stmt ::=  "del" target_list

# dict_comp ::=  expression ":" expression comp_for

# dict_display ::=  "{" [key_datum_list] "}"
#                   | "{" key_datum_list "," "}"

# dict_key ::=  expression
#               | "**" expression

# dict_key_datum ::=  dict_key ":" expression

# dict_key_datum_list ::=  dict_key_datum ("," dict_key_datum)* [","]

# dict_key_list ::=  dict_key ("," dict_key)* [","]

# dict_keys ::=  dict_keys "," dict_key
#                | dict_key

# dict_keys_list ::=  dict_keys ("," dict_keys)* [","]

# dict_literal ::=  "{" [key_datum_list] "}"
#                   | "{" key_datum_
