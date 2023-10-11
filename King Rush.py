a,b,c,d,x,y = map(int,input().split())
 
b_dist = max(abs(c - x) , abs(d - y)) 
w_dist = max(abs(a - x) , abs(b - y))
 
 
if(b_dist < w_dist):
    print("Black")
elif(b_dist == w_dist):
    print('White')
else:
    print('White')
