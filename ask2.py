import math
import itertools
def find_auto(prob):
    auto1={}
    for i in prob:
        auto1[i]=math.log(1/prob[i])
    return auto1

def find_2_min(dict1):
    a=dict1.copy()
    min1=min(a,key=a.get)
    del a[min1]
    min2=min(a,key=a.get)

    return [min1,min2]
def find_H(prob):
    H_x=0
    for i in prob:
         H_x=H_x-prob[i]*math.log(float(prob[i]),2)

    return H_x

    

prob={'a1':0.5,'a2':0.35,'a3':0.15}
#erwtima_a
auto1=find_auto(prob)
H_x1=find_H(prob)


#erwtima_b
keys=list(prob.keys())
keys2=keys+keys
pairs2=list(itertools.combinations(keys2, 2))
p2={}
for i in pairs2:
    p2[i[0]+i[1]]=prob[i[0]]*prob[i[1]]
prob2={}
while(len(p2)!=0):
    max_key=max(p2,key=p2.get)
    prob2[max_key]=p2[max_key]
    del p2[max_key]


auto2=find_auto(prob2)
H_x2=find_H(prob2)

#huffman
print('Huffman for 2 pairs')
p2=prob2.copy()
psi={}
new1={}
keys1={}
a=1
for i in prob2:
    keys1[a]=i
    a=a+1
p2={}
for i in p2:
    psi[i]=''
for i in keys1:
    p2[i]=prob2[keys1[i]]

for i in range(len(p2)-1):
    min2=find_2_min(p2)
    new_key=str(min2[0])+'|'+str(min2[1])
    print(i,min2[0],p2[min2[0]],min2[1],p2[min2[1]])
    #print(i,p2)
    new_value=p2[min2[0]]+p2[min2[1]]

    

    
    if(p2[min2[0]]>=p2[min2[1]]):
        psi[min2[0]]=0
        psi[min2[1]]=1
    else:
        psi[min2[0]]=1
        psi[min2[1]]=0

    del p2[min2[0]]
    del p2[min2[1]]

    p2[new_key]=new_value
    if(len(p2)==1):
        break
        
for i in psi:
    for j in [1,2,3,4,5,6,7,8,9]:
        if(str(j) in str(i)):
            if(j not in new1.keys()):
                new1[j]=str(psi[i])
            else:
                new1[j]=str(psi[i])+str(new1[j])
    
psi1={}
for i in keys1:
    psi1[keys1[i]]=new1[i]
R1=0
for i in psi1:
    R1=R1+len(psi1[i])*prob2[i]

apodo1=H_x2/R1
print('h apodosi tis kodikopoihshs 2 zeugariwn einai:',apodo1)
    
print('\n')
print('\n')
print('huffman for 3 pairs')
#erwtimac
keys=list(prob.keys())
keys3=keys+keys+keys
pairs3=list(itertools.combinations(keys3, 3))
p3={}
for i in pairs3:
    p3[i[0]+i[1]+i[2]]=prob[i[0]]*prob[i[1]]*prob[i[2]]
prob3={}
while(len(p3)!=0):
    max_key2=max(p3,key=p3.get)
    prob3[max_key2]=p3[max_key2]
    del p3[max_key2]
#huffman
p3=prob3.copy()
psi2={}
keys2={}
a=1
for i in prob3:
    keys2[a]=i
    a=a+1
p3={}
for i in p3:
    psi2[i]=''
for i in keys2:
    p3[i]=prob3[keys2[i]]

for i in range(len(p3)-1):
    min3=find_2_min(p3)
    new_key2=str(min3[0])+'|'+str(min3[1])
    new_value2=p3[min3[0]]+p3[min3[1]]

    print(i,min3[0],p3[min3[0]],min3[1],p3[min3[1]])
    #print(i,p3)
    
    if(p3[min3[0]]>=p3[min3[1]]):
        psi2[min3[0]]=0
        psi2[min3[1]]=1
    else:
        psi2[min3[0]]=1
        psi2[min3[1]]=0

    del p3[min3[0]]
    del p3[min3[1]]

    p3[new_key2]=new_value2
    if(len(p3)==1):
        break

new2={}
d1=[]
b1=[]
c=''
for i in list(psi2.keys()):
	if('|' not in str(i)):
		d1.append(i)
	else:
		for j in i:
			if(j!='|'):
				c=c+j
			else:
				b1.append(int(c))
				c=''
		b1.append(int(c))
		d1.append(b1)
		b1=[]
		c=''


new_psi={}
for (i,j) in zip(psi2,d1):
    a=type(j)==list
    if(a==True):
        new_psi[tuple(j)]=psi2[i]
    else:
        new_psi[j]=psi2[i]

for i in new_psi:
    for j in list(keys2.keys()):
        if(type(i)==tuple):
            #print(i)
            if(j in i):
                if(j not in new2.keys()):
                    new2[j]=str(new_psi[i])
                else:
                    new2[j]=str(new_psi[i])+str(new2[j])
        else:
            if(j==i):
                if(j not in new2.keys()):
                    new2[j]=str(new_psi[i])
                else:
                    new2[j]=str(new_psi[i])+str(new2[j])

psi2={}
for i in keys2:
    psi2[keys2[i]]=new2[i]
R2=0
for i in psi2:
    R2=R2+len(psi2[i])*prob3[i]
auto3=find_auto(prob3)
H_x3=find_H(prob3)
apodo2=H_x3/R2
print('h apodosi tis kodikopoihshs 3 zeugariwn einai:',apodo2)
