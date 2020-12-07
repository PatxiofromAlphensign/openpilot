from tempfile import mkstemp
from os import fdopen, remove
from shutil import move, copymode
import os, sys

def replaceinfile(fn):
    with open(fn, "r") as r:
        lines = r.readlines()
        for i,line in enumerate(lines):
            linesp = line.split()
            for i,k in enumerate(linesp):
                if "" in k:
                    linesp[i] = k.replace("", "")
            line = " ".join(linesp)
            lines[i] = line

        return " ".join(lines)

def write(dirn):
    for fi in os.listdir(dirn):
          content = replaceinfile(fi)
          with open(fi, "w") as w:
              w.write(content)
       
def writetmp(dirn):
    for fn in os.listdir(dirn):
        fi, absph = mkstemp()
        with fdopen(fi, "w") as w:
            with open(fn, "r") as r:
                for line in r:
                    w.write(line.replace("", ""))
        copymode(fn, absph)
        remove(fn)
        move(absph, fn)
        print("%s moved to %s" % (absph, fn)) 

writetmp(sys.argv[1])
