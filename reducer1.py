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
    res=int(res)   
    K=3

    if me is None:
        me = fd1
        simppl[fd2]=[1,res]
    else:
        if me == fd1:
            if simppl.has_key(fd2):
                simppl[fd2][0]=simppl[fd2][0]+1
                simppl[fd2].append(res)
            else:
                simppl[fd2]=[1,res]
        else:
            sortppl=sorted(simppl.items(), key=lambda (k,v): v[0],reverse=True)
            if len(sortppl) > K-1:
                for i in range(0,K):
                    del sortppl[i][1][0]
                    sortppl[i][1].sort()


                    checksum=sum(sortppl[i][1])
                    print '%s: %s, {%s}, %d' % (me,sortppl[i][0],str(sortppl[i][1])[1:-1],checksum)       

            else:
                for i in range(0,len(sortppl)):
                    del sortppl[i][1][0]
                    sortppl[i][1].sort()    


                    checksum=sum(sortppl[i][1])
                    print '%s: %s, {%s}, %d' % (me,sortppl[i][0],str(sortppl[i][1])[1:-1],checksum)
            me = fd1
            simppl={}
            simppl[fd2]=[1,res]
sortppl=sorted(simppl.items(), key=lambda (k,v): v[0],reverse=True)
if len(sortppl) > K-1:
    for i in range(0,K):
        del sortppl[i][1][0]
        sortppl[i][1].sort()


        checksum=sum(sortppl[i][1])
        print '%s: %s, {%s}, %d' % (me,sortppl[i][0],str(sortppl[i][1])[1:-1],checksum)

else:
    for i in range(len(sortppl)):
        del sortppl[i][1][0] 
        sortppl[i][1].sort()


        checksum=sum(sortppl[i][1])
        print '%s: %s, {%s}, %d' % (me,sortppl[i][0],str(sortppl[i][1])[1:-1],checksum)       
    
