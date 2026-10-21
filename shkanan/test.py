dy5=[5,None]
dy4=[4,dy5]
dy3=[3,dy4]
dy2=[2,dy3]
dy1=[1,dy2]
n=dy1
while n is not None:
  print(f"{n[0]}")
  n=n[1]