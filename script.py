"""
-------------------------------------------------------------------
-------------------------------------------------------------------
# Documentation Decision - Challenge program LiveRamp
# http://blog.liveramp.com/2013/03/27/documentation-decision/
-----------------------------------------------------
# Developped By Mohammed Elalj - https://github.com/melalj/liveramp-subset
-------------------------------------------------------------------
-------------------------------------------------------------------
"""

import sys,math

	
# Given N and M, write a program to compute the last engineer
def algo1(M,N):
	engineers = range(1,(M+1))
	R = engineers.index(N)
	while len(engineers)>1:
		sys.stdout.write("%d, "%engineers[R])
		engineers.remove(engineers[R])
		R = (R+N-1)%len(engineers)
	sys.stdout.write("%d"% engineers[0])
	print ""
	return engineers[0]

# Find a closed-form equation to find the last engineer when N=2
def algo2(M):
	last_engineer = 1 + ( M - int(math.pow(2,math.floor(math.log(M,2)))) ) * 2
	return last_engineer


M = 8
N = 3
print "Test with M=%d & N=%d" % (M,N)
print "Last engineer: %d " % algo1(M,N)

print ""

M = 50
print "test with M=%d & N=2" % M
print "Last engineer: %d " % algo1(M,2)

print ""
print "Using closed-form equation"
print algo2(M)
