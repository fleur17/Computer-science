#print("Soleil")

import sys
mode=None
if (len(sys.argv)<3):
    sys.exit(0)
if(sys.argv[1]=="cypher"):
    mode="cypher"
    d=[]
    for i in sys.argv[3]:
        k=ord(i)
        j=k+int(sys.argv[2])
        d.append(j)
        
    print(d)

    dech=''
    for a in d:
        dech+=chr(a)
    print(dech)


elif (sys.argv[1] =="decypher"):
    print('a')
    
else:
    print(f"commande non supportee: {sys.argv[1]}")
    sys.exit(0)
key = sys.argv[2]
msg = sys.argv[3]


first_char=msg[0]
print(ord(first_char))










