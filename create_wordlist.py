import pathlib
import sys
from string import ascii_letters


in_path = pathlib.Path(sys.argv[1])
out_path = pathlib.Path(sys.argv[2])


words = sorted(
    {
        word.lower()
        for word in in_path.read_text(encoding="utf-8").split()
        if all(letter in ascii_letters for letter in word)
    },
    key=lambda word: (len(word), word), 
    )
"""
Note: Only allowing the letters A to Z may be too limiting, especially if you want to create a word list in a language other than English.
In that case, you could use a regular expression. The \w special sequence matches most of the characters that can be part of a word in any language.

You get a more permissive filter by replacing line 14 with the following:

if re.fullmatch(r"\w+", word):
If you go this route, remember to import re at the top of your code. 
This filter will also allow underscores, so something like guess_num will be included in your word list. 
You can avoid underscores and numbers by using r"[^\W0-9_]+".
This uses a negative character group, listing characters that aren’t allowed in the words.
"""


out_path.write_text("\n".join(words))

"""
You can use the script to, for example, convert your current version of wyrdl.py to a word list as follows:
$ python create_wordlist.py wyrdl.py wordlist.txt
"""
