#I took help from google sorry
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**o.5)+1):
        if num%i==0:
            return False
    return True
num=int(input('enter the number upto you want:'))
for i in range(2,n+1):
    if is_prime(i):
        print(i,end='')
        
