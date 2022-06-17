import keyboard
import time
    
#Version-1
# a=a.split(" ")
# print(a)
# time.sleep(2)
# for i in a:
#     for j in i:
#         keyboard.write(j)
#         time.sleep(0.05)
#     keyboard.write(" ")
#     time.sleep(0.2)

#Version-2
def acttyping(a):
    a=a.split(" ")
    print(a)
    for i in a:
        i=i.replace('\n',' ')    
        print(i)
        for j in i:
            keyboard.write(j)
            time.sleep(0.03)
        keyboard.write(" ")
        time.sleep(0.3)