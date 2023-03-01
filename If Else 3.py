(9 sloc)  217 Bytes

n = str(input('Username :'))

b=str(input('Password :'))

if n in ['admin']:
   if b in ['Ad13n@23t']:
      print('Welcome,You are Admin')
   else:
      print('You are not admin')
else:
   print('You are not admin')
