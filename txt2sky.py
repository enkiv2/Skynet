#!/usr/bin/env python

import sys

table={}
itable={}
filename=sys.argv[1]
f=open(filename, 'r')
for line in f.readlines():
	x=line[:len(line)-1].split('\t')
	if(len(x)>1):
		if (not (x[0] in table)):
			table[x[0]]=[]
		table[x[0]].append(x[1])

for x in table.keys():
	for y in table[x]:
		itable[y]=x
print("puts %{")
for line in sys.stdin.readlines():
	for x in itable.keys():
		line=line.replace(x, itable[x])
	print(line[:len(line)-1])
print("}")

