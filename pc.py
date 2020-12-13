import time
starttime=time.time()
for i in range(1,100):
    print(i)
endtime=round(time.time()-starttime,2)
print(f'Finshed [{endtime}]')
