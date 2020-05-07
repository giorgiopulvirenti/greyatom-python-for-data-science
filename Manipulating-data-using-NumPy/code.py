# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path,delimiter=",", skip_header=1)
print("\nData: \n\n", data)
#New record

new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

census=np.concatenate((data,new_record))
#Code starts here



# --------------
#Code starts here
age=census[:,0]
print(age)
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)


# --------------
#Code starts here
race=census[:,2]
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
x=999999
len_0=len(race_0)
if len_0<x:
    x=len_0
    minority_race=0
len_1=len(race_1)
if len_1<x:
    x=len_1
    minority_race=1
len_2=len(race_2)
if len_2<x:
    x=len_2
    minority_race=2
len_3=len(race_3)
if len_3<x:
    x=len_3
    minority_race=3
len_4=len(race_4)
if len_4<x:
    x=len_4
    minority_race=4




# --------------

senior_citizens=census[census[:,0]>60]
print(senior_citizens)
working_hours_sum=np.sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])
print(avg_pay_high>avg_pay_low)



