import psutil
output=list(psutil.win_service_iter())
for name in output:
   if 'status'== "running":
       print(output)



s = psutil.win_service_get('alg')
y=s.as_dict()
print(y)
