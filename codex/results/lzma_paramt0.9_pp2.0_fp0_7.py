from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed) top56.paf_lzma

# binwalk: a file signature analyzer
# locates and extract embedded files from a given file
# from binary file
# https://aircrack-ng.org/doku.php?id=comprehensive_explanation_of_the_wordlists
# $ wpaclean -r top56.paf_lzma | aspell -l en dump master > top56.paf

# Commonly used wordlists:
# Rockyou
# (14.854.956 words, 3,999kb gzip)
# https://sourceforge.net/projects/crackpassword/files/rockyou.txt.gz/download
#
# Openwall's super small wordlist (1253 words, 14kb gzip)
# https://www.openwall.com/passwords/wordlists-big-mirrors/
#
# Seclists SecLists RockYou wordlist :
# https://github.com/danielmiessler/SecLists/blob/master/Passwords/rockyou.txt.gz

