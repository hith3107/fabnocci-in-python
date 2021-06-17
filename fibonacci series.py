a=int(input('enter no of terms:',))
x=0;y=1;n=0;
if a<0:
    print('enter a positive number')
elif a>0:
    while n<a:
      print(x)
      p=x+y
      x=y
      y=p
      n+=1
