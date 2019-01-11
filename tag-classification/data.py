import string
import glob
import unicodedata


def findfiles(path): return glob.glob(path)


# Turn a Unicode string to plain ASCII, thanks to http://stackoverflow.com/a/518232/2809427
def unicodetoascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )


# Read a file and split into lines
def readlines(file):
    with open(file, encoding="utf-8") as f:
        filelines = f.readlines()
        filelines = list(map(lambda line: line.strip(), filelines))

    # lines = open(filename).read().strip().split('\n')
    return [unicodetoascii(line) for line in filelines]

