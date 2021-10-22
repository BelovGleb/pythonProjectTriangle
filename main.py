a=[i+1 for i in range(50)][::-1]
print(a)
for i in range(50-2):
 a1=a[i]
 b=a[i+1]
 c=a[i+2]
 if a1+b>c or a1+c>b or b+c>a1:
  p=(a1+b+c)/2
  s=(p*(p-a1)*(p-b)*(p-c))**(1/2)
  print(s)