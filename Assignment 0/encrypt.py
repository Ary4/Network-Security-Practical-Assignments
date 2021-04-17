import string
p = string.printable

### creating maps for atbash cipher for [A-Z][a-z]
k = [(x,y) for x in p[10:36] for y in p[35:9:-1]][0::27]
c = [(x,y) for x in p[36:62] for y in p[61:35:-1]][0::27]
k=k+c

def solution(x):
    r = []
    for i in x:
        flag=1
        for k1,k2 in k:
            if i==k1:
                flag=0
                r.append(k2)

        if flag:
            r.append(i)

    return(str(''.join(r))) 


if __name__ == '__main__':
    myInput = input('Enter the text to be encrypted')
    print(solution(myInput))
    