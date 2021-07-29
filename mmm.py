import csv
from collections import Counter

with open('hw.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
    
file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    n_num=file_data[i][2]
    new_data.append(float(n_num))

n=len(new_data)
total=0
for j in new_data:
    total+=j

mean=total/n
print('mean: '+str(mean))

new_data.sort()

if(n%2==0):
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median=(median1+median2)/2
else:
    median=new_data[n//2]

print('median: ',str(median))

data=Counter(new_data)
mode_data_for_range={
    "90-100":0,
    "100-110":0,
    "110-120":0,
    "120-130":0,
    "130-140":0,
    "140-150":0,

}

for weight,occurence in data.items():
    if(90<float(weight)<100):
        mode_data_for_range["90-100"]+=occurence
    elif(100<float(weight)<110):
        mode_data_for_range["100-110"]+=occurence
    elif(110<float(weight)<120):
        mode_data_for_range["110-120"]+=occurence
    elif(120<float(weight)<130):
        mode_data_for_range["120-130"]+=occurence
    elif(130<float(weight)<140):
        mode_data_for_range["130-140"]+=occurence
    elif(140<float(weight)<150):
        mode_data_for_range["140-150"]+=occurence

mode_range,mode_occurence=0,0

for range,occurence in mode_data_for_range.items():
        if(occurence>mode_occurence):
            mode_range,mode_occurence=[int(range.split('-')[0]),int(range.split('-')[1])],occurence

mode=float((mode_range[0]+mode_range[1])/2)
print(f'mode: {mode:2f}')