#!/usr/bin/python3

import subprocess

text = [
"""
import inspect
class Class0:
 def print(self):
  nbases = len(inspect.getmro(self.__class__))-1
  print(f'{self.__class__.__name__} has {nbases} base classes')

class Class1(Class0): pass
class Class2(Class1): pass
class Class3(Class2): pass
class Class4(Class3): pass
class Class5(Class4): pass
class Class6(Class5): pass
class Class7(Class6): pass
class Class8(Class7): pass
class Class9(Class8): pass
class Class10(Class9): pass
class Class11(Class10): pass

Class11().print()
""",

"""10*(10*(10,),)

((10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
 (10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
 (10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
 (10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
 (10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
 (10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
 (10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
 (10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
 (10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
 (10, 10, 10, 10, 10, 10, 10, 10, 10, 10))
""",

"""9*[99*'9']

['999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999',
 '999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999',
 '999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999',
 '999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999',
 '999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999',
 '999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999',
 '999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999',
 '999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999',
 '999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999']
""",


"""
[2**i for i in range(1,9)]

[2, 4, 8, 16, 32, 64, 128, 256]
""",

"""
import random
[[random.randint(1,9) for _ in range(7)]
     for __ in range(7)]

[[6, 6, 9, 3, 3, 7, 2],
 [1, 4, 4, 2, 3, 9, 8],
 [3, 5, 1, 3, 7, 8, 9],
 [4, 3, 2, 2, 7, 2, 3],
 [1, 3, 8, 4, 1, 6, 2],
 [5, 9, 3, 1, 1, 4, 1],
 [5, 3, 5, 4, 2, 2, 3]]
""",

"""
for n1 in (1,2,3,4):
 for n2 in (2,3,4):
  for s in ('colour', 'color'):
   for v in ('is', 'could be', 'might be'):
    for a in ('A crazy', 'A mad', 'An insane', 'A stupid'):
     for c in ('red', 'blue', 'green'):
      print(f"{a} {s}ization of {n1*n2} {v} {'-'.join(n1*n2*[c])}")
""",

"""
u'Ordinary ASCII strings are Unicode'
u'Puedes escribir en espa\\\\u00f1ol'
u'\\\\u6c49\\\\u5b57\\\\u4e5f\\\\u6709\\\\u7528'
u'\\\\u2660\\\\u2665\\\\u2666\\\\u2663'
u'\\\\U0001f384\\\\U0001f381\\\\U0001f385\\\\U0001f98c\\\\u26ea'
""",


"""
def bird(call):
    return lambda: print(call)

hen = bird('quack')
owl = bird('hoot')
hawk = bird('screech')
crow = bird('caw')

while True:
    for bird in (hen, owl, hawk, crow): bird()
""",

"""
str()
int()
float()
""",

"""
\['All', 'Python', 'lists', 'are', 'iterable'\]
\['No', 'Python', 'lists', 'are', 'hashable'\]
""",

"print('Hello me!')"
]

args = 'convert -size 640x480 -background lightblue -pointsize 25 -fill black -gravity West caption:'.split()
args.extend(['-flatten', f'blank.png'])

subprocess.run(args)

args = f'convert -size 640x480 -background lightblue -pointsize 60 -fill black -gravity Center'.split()
args.append('caption:Merry\nChristmas\n2022')
args.extend(['-flatten', f'merry.png'])

subprocess.run(args)

for num,t in enumerate(text):
    if num==0:
        ps = 20
    elif num==2:
        ps = 10
    else:
        ps = 25;
    args = f'convert -size 640x480 -background lightblue -pointsize {ps} -fill black -gravity West'.split()
    args.append(f'caption:{t}')
    args.extend(['-flatten', f'frame{11-num}.png'])

    subprocess.run(args)

# convert image12a.jpg -geometry 640x480! image12a.png
# convert image12b.jpg -geometry 640x480! image12b.png
