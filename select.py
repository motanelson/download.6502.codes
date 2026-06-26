import os
down="https://tutorial-6502.sourceforge.io/specification/opcodes/"
files="down.html"
finds="Sorted by hex code"
select1="Forms"
select2="Operand Stack"
print("\033c\033[47;31m\nfile: "+files)
os.system("curl "+down+" -o "+files)
f1=open(files,"r")
a=f1.read()
f1.close()

b=a.find("<body")
if b<0:
    b=a.find("<BODY")
a=a[b:]
a=a.replace("\n","")
a=a.replace("\r","")




bodys=a.split("<")
c=""
for body in bodys:
    t=body.split(">")
    if len(t)>1:
        c=c+t[1]
b=c.find(finds)
if b<0:
    print("error:")
else:
    d=len(finds)+b
    c=c[d:]
b=c.find(finds)
if b<0:
    print("error:")
else:
    d=len(finds)+b
    c=c[d:]


finds="Sorted alphabetically"
b=c.find(finds)
if b<0:
    print("error:")
else:
    d=len(finds)+b
    c=c[:d]
c=c.replace("          ","\n")

g=c.split("\n")
v=""
for gg in g:
    gg=gg.strip()
    v=v+gg+"|"
    if gg=="":
        v=v+"\n"
v=v.replace("||","")
vv=v.split("\n")

vb=""
for gg in vv:
    gg=gg.strip()
    ggg=gg.split("|")
    if len(ggg)>1:
        vb=vb+ggg[0]+"|"+ggg[1]+"\n"

f1=open(files,"w")
f1.write(vb)
f1.close()
