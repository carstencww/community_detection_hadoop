#!/usr/bin/python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    followers = line.split()
    followee , followers[0] = followers[0].split(':')
    for i in range(len(followers)) :
        for j in range(i+1,len(followers)):
            print(followers[i]+','+ followers[j]+','+followee)
            print(followers[j]+','+ followers[i]+','+followee)
