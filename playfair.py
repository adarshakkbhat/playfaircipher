# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 20:38:43 2022

@author: Adarsha K K
"""
import string
low=list(string.ascii_lowercase)
pt=list(input("Enter the plain text\n").lower().replace(" ",""))
ic=pt.count('i')
jc=pt.count('j')
if ic>=jc:
   low.remove('j')
   for i in range(len(pt)):
      if pt[i]=='j':
         pt[i]='i'
else:
    low.remove('i')
    for i in range(len(pt)):
      if pt[i]=='i':
         pt[i]='j'
key=list(input("Enter the key\n").lower())
for i in low:
    if i not in key:
        key.append(i)
#Table Creation
table=[]
for i in range(5):
    table.append(key[i*5:i*5+5])
#diagraph
if(len(pt)%2==1):
    pt.append('z')
di=[]
dilist=[]
for i in range(0,len(pt)-1,2):
    if pt[i]==pt[i+1]:
        di.append(pt[i])
        di.append('x')
        dilist.append(di)
        dilist.append(di)
        di=[]
    else:
        di.append(pt[i])
        di.append(pt[i+1])
        dilist.append(di)
        di=[]
#encryption
en=[]
enlist=[]
row1=0
col1=0
row2=0
col2=0
for item in dilist:
    for i in range(5):
        for j in range(5):
            if table[i][j]==item[0]:
                row1=i
                col1=j
            if table[i][j]==item[1]:
                row2=i
                col2=j
    if col1==col2:
        en.append(table[(row1+1)%5][col1])
        en.append(table[(row2+1)%5][col1])
        enlist.append(en)
        en=[]
    elif row1==row2:
        en.append(table[row1][(col1+1)%5])
        en.append(table[row2][(col2+1)%5])
        enlist.append(en)
        en=[]
    else:
        en.append(table[row1][col2])
        en.append(table[row2][col1])
        enlist.append(en)
        en=[]
encrypt=""
for i in enlist:
    encrypt=encrypt+''.join(i)
print("Encrypted message is "+encrypt )
#decryption
dc=[]
dclist=[]
row1=0
col1=0
row2=0
col2=0
for item in enlist:
    for i in range(5):
        for j in range(5):
            if table[i][j]==item[0]:
                row1=i
                col1=j
            if table[i][j]==item[1]:
                row2=i
                col2=j
    if col1==col2:
        dc.append(table[(row1+4)%5][col1])
        dc.append(table[(row2+4)%5][col1])
        dclist.append(dc)
        dc=[]
    elif row1==row2:
        dc.append(table[row1][(col1+4)%5])
        dc.append(table[row2][(col2+4)%5])
        dclist.append(dc)
        dc=[]
    else:
        dc.append(table[row1][col2])
        dc.append(table[row2][col1])
        dclist.append(dc)
        dc=[]
decrypt=""
for i in dclist:
    decrypt=decrypt+''.join(i)
print("Decrypted text is "+decrypt)