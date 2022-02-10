
def MultiplicaFG(fx: str,gx: str):
    result= "00000000"
    for i in range(len(gx)):
        if gx[i] == '1':
            partial = fx
            for j in range(7-i):
                aux= multiplica(partial)
                partial = aux
            subresult=""
            for j in range(8):
                subresult+= "0" if (partial[j]=='1' and result[j]=='1') else "1" if(partial[j]=='1' or result[j]=='1') else "0"
            result=subresult
    return result
    

def multiplica(partial:str):
    subpartial = partial[1:]+"0"
    if partial[0] == '1':
        aux = subpartial
        subpartial = subpartial[:6]
        subpartial+= "0" if aux[3] == '1' else "1"
        subpartial+= "0" if aux[4] == '1' else "1"
        subpartial+= "0" if aux[6] == '1' else "1"
        subpartial+= "0" if aux[7] == '1' else "1"
    return subpartial
"""
table = open("table.txt","w")
inverse = open("inverse.txt","w")
inv={}
out='   |'
for i in range(2**8):
    f=format(i,"b")
    while(len(f)<8):
        f='0'+f
    out=out+" "+hex(int(f,2))+"|"
table.write(out)
for i in range(2**8):
    out="|"
    f=format(i,"b")
    while(len(f)<8):
        f='0'+f
    out=hex(int(f,2))+out
    for j in range(2**8):
        g=format(j,"b")
        while(len(g)<8):
            g='0'+g
        aux = MultiplicaFG(f,g)
        if(aux=="00000001"):
            inv[f]=g
        out=out+" "+hex(int(aux,2))+"|"
    table.write("\n=====================================================================\n")
    table.write(out)

for i in inv:
    inverse.write("Inverse of "+hex(int(i,2))+" is: "+hex(int(inv[i],2))+"\n")

table.close()
inverse.close()
"""

print(hex(int(MultiplicaFG("00000001","10000111"),2)))
print(hex(int(MultiplicaFG("00000001","01101110"),2)))
print(hex(int(MultiplicaFG("00000010","01000110"),2)))
print(hex(int(MultiplicaFG("00000011","10100110"),2)))