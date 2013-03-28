Documentation Decision - Challenge program LiveRamp
============

Problem
---

A group of software engineers are nearing completion on an important project. Only one task remains: writing the documentation. Nobody wants to do this chore, so the group decides on a procedure for choosing the unlucky dev. The M engineers will stand in a circle. One engineer will be randomly choosen to be engineer 1, and the others will be numbered consecutively around the circle. The group will then choose some number N, and eliminate every Nth engineer from the circle until only one remains.

For example:

If M is 8 and N is 3, then the engineers will be eliminated in this order:
3,6,1,5,2,8,4
with engineer 7 being assigned to write documentation.

Your challenge:

CS101: Given N and M, write a program to compute the last engineer
Easy: Given N and M, write a program to compute the last engineer which uses only O(1) space
Medium/Hard: Given N and M, write a program to compute the last engineer which uses O(1) space and takes O( lognm ) time
Medium/Hard: Find a closed-form equation to find the last engineer when N=2

