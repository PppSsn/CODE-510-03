n = int( input (' ระบุรายได้ของคุณ' ) )
if(n<=15000) :
 print('Not Approve')
elif(n<=70000):
 print('Approve Silver Class')
elif(n<=100000) :
 print('Approve Gold Class')
else :
 print('Approve Platinum Class')