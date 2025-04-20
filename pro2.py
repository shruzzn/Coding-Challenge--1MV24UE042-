n=int(input("Enter the number you want to check"))
for i in range(2,n):
    if n%i==0:
        print("not a prime number")
        break
else:
        print('a prime number')
