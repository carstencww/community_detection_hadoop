#!/usr/bin/python
import sys
from operator import itemgetter
import collections
me = None
simppl = {}

# input comes from STDIN
for line in sys.stdin:

    line = line.strip()
    key, res  = line.split()
    fd1,fd2=key.split(',')
    
    K=3

    if me is None:
        me = fd1
        simppl[fd2]=1
    else:
        if me == fd1:
            if simppl.has_key(fd2):
                simppl[fd2]= simppl[fd2] + 1
            else:
                simppl[fd2]= 1
        else:
            sortppl=sorted(simppl.items(), key=itemgetter(1),reverse=True)
            if len(sortppl) > K-1:
                print '%s: %s %s %s' % (me,sortppl[0][0],sortppl[1][0],sortppl[2][0])
            else:
                out=me+':'
                for i in range(len(sortppl)):
                    out+=' '+ sortppl[i][0]
                print(out)
            me = fd1
            simppl={}
            simppl[fd2]=1
sortppl=sorted(simppl.items(), key=itemgetter(1),reverse=True)
if len(sortppl) > 2:
    print '%s: %s %s %s' % (me,sortppl[0][0],sortppl[1][0],sortppl[2][0])
else:
    out=me+':'
    for i in range(len(sortppl)):
        out+=' '+ sortppl[i][0]
    print(out)
  
   
                
       
        
    
