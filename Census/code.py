# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#Code starts here
census = np.concatenate((new_record,data),axis = 0)
print(np.shape(data))
print(np.shape(census))

age = census[:,0]
print(age)
max_age = age.max()
print(max_age)
min_age = age.min()
print(min_age)
age_mean = age.mean()
print(age_mean)
age_std = np.std(age)
print(age_std)

race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = np.size(race_0)
len_1 = np.size(race_1)
len_2 = np.size(race_2)
len_3 = np.size(race_3)
len_4 = np.size(race_4)

if len_0 == min(len_0,len_1,len_2,len_3,len_4):
    minority_race = 0
elif len_1 == min(len_0,len_1,len_2,len_3,len_4):
    minority_race = 1
elif len_2 == min(len_0,len_1,len_2,len_3,len_4):
    minority_race = 2
elif len_3 == min(len_0,len_1,len_2,len_3,len_4):
    minority_race = 3
else:
    minority_race = 4

print(minority_race)

senior_citizens = census[census[:,0]>60]
working_hours_sum = senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len = senior_citizens.size
print(senior_citizens_len)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = high.mean(axis=0)[7]
avg_pay_low = low.mean(axis=0)[7]
print(avg_pay_high)
print(avg_pay_low)




