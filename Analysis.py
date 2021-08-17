import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

''' Firstly I'll import the csv file of the gym data which I've scraped from the PureGym website. This file simply 
shows the number of people in the gym at certain times throughout the day. The aim is to gather a large enough data set
to be able to decipher when the optimum gym times are (least number of people in the gym). '''

gym_data = pd.read_csv('/Users/isaaccoleman/PycharmProjects/Puregym/data.csv')

''' Below, we produce a pivot table with the days of the week as the index, the times throughout the day as columns and 
the mean number of people in the gym as the values. There are NaN values on Saturday and Sunday as the opening times on 
the weekends differ from the weekdays (Weekdays 06:00 - 22:00 / Weekends 08:00 - 20:00). '''

days = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mean_members = np.round(gym_data.pivot_table(values='Number', index='Day', columns='Time'), 1)
mean_members = mean_members.reindex(days)
print(mean_members.to_string())

''' Now I'm going to plot a graph of the number of people in the gym against the time throughout the day. This will be
a general graph of all the data (not day-specific). '''

average_day = gym_data.pivot_table(index='Time', values='Number')
ax = plt.axes()

bar_chart = plt.bar(x=average_day.index, height=[i[0] for i in average_day.values])
ax.set_xticks(average_day.index)
ax.set_xticklabels(average_day.index, rotation=90)
plt.xlabel('Time')
plt.ylabel('Average Number of People in the Gym')
plt.title('Average Gym Activity throughout the Day')

# Highlighting the bars at the times where the number of people in the gym is less than 40
for i in range(len(average_day.values)):
    if average_day.values[i] < 40:
        bar_chart[i].set_color('g')
plt.show()

''' The graph above represents the average number of people at the gym throughout a generic day. We would like to look 
at the data in relation to specific days in order to find the optimum times (least number of people in the gym). Most
people at the gym tend to have a schedule and go to the gym at the same day/times each week. Using the data, I can find 
 the times on each day of the week where the gym is most empty. '''
column = ['Best', 'Second', 'Third', 'Fourth', 'Fifth']
times = [i for i in mean_members.columns]

optimum_times = pd.DataFrame(columns=column)
print(optimum_times)

for i in days:
    df_nan = mean_members.loc[i]
    df = df_nan.dropna()
    #print(lst)
    #print(df_nan[1])
    #print((max(df)))
    # ordered (list) number of people in the gym
    lst=[]
    for j in range(len(df_nan)):
        pair = [times[j], df_nan[j]]
        lst.append(pair)
        lst = sorted(lst, key=lambda x: x[1])
    # sorting the times in order of least number of people in the gym
    lst = sorted(lst, key=lambda x: x[1])
    print(i)
    # Taking into account the different opening times
    if i != 'Saturday' and i != 'Sunday':
        new_row = {'Best':lst[0], 'Second':lst[1], 'Third':lst[2], 'Fourth':lst[3], 'Fifth':lst[4]}
        optimum_times = optimum_times.append(new_row, ignore_index=True)
    else:
        new_row = {'Best':lst[4], 'Second':lst[5], 'Third':lst[6], 'Fourth':lst[7], 'Fifth':lst[8]}
        optimum_times = optimum_times.append(new_row, ignore_index=True)

optimum_times['Days'] = days
optimum_times = optimum_times.set_index('Days')
print(optimum_times.to_string())

''' My schedule consists of going to the gym three times a week with a day in between. I tend to go to between
14:00-16:00. I currently go to the gym on Monday, Wednesday and Friday (for no particular reason). I'd like to see if 
Tuesday, Thursday, Saturday are a better combination of days with regards to the number of people in the gym. 
I'm going to compare Monday with Tuesday, Wednesday with Thursday and Friday with Saturday.  '''


# MONDAY VS TUESDAY

''' (20/08/2001) I've noticed that for most of the day, Monday has less people
in the gym than on Tuesday, however the only times when Tuesday has (about 10) fewer people is 14:00 - 17:00 which is my 
preferred time to go - Thus, Tuesday wins. '''

fig = plt.figure()
ax = fig.add_subplot()

monday = gym_data[gym_data['Day'] == 'Monday'].pivot_table(index='Time', values='Number')
plt.plot(monday.index, [i[0] for i in monday.values], label='Monday')

tuesday = gym_data[gym_data['Day'] == 'Tuesday'].pivot_table(index='Time', values='Number')
plt.plot(tuesday.index, [i[0] for i in tuesday.values], label='Tuesday')

ax.set_xticks(monday.index)
ax.set_xticklabels(monday.index, rotation=90)
ax.set_xlabel('Time')
ax.set_ylabel('Number of People in the Gym')
ax.legend()
plt.show()



# WEDNESDAY VS THURSDAY

''' (20/08/2001) From 13:30-14:30 Wednesday has fewer people than Thursday, but from 14:30-18:00 Thursday prevails. However, the 
difference in numbers is very small (3-5) for my preferred times. What stands out to me is that, for both days, 15:00 is
the sweet spot where there are less than 40 people in the gym. It is also notable that, on a Wednesday from 9:00-12:00, 
there are usually less than 40 people in the gym (sometimes reaching 30). We can check this by comparing bar charts:'''

fig = plt.figure()
ax = fig.add_subplot()

monday = gym_data[gym_data['Day'] == 'Wednesday'].pivot_table(index='Time', values='Number')
plt.plot(monday.index, [i[0] for i in monday.values], label='Wednesday')

tuesday = gym_data[gym_data['Day'] == 'Thursday'].pivot_table(index='Time', values='Number')
plt.plot(tuesday.index, [i[0] for i in tuesday.values], label='Thursday')

ax.set_xticks(monday.index)
ax.set_xticklabels(monday.index, rotation=90)
ax.set_xlabel('Time')
ax.set_ylabel('Number of People in the Gym')
ax.legend()
plt.show()

# Bar Chart Comparison
fig, ax = plt.subplots(2, sharex=True, constrained_layout=True)

wednesday = gym_data[gym_data['Day'] == 'Wednesday'].pivot_table(index='Time', values='Number')
bar_chart = ax[0].bar(x=wednesday.index, height=[i[0] for i in wednesday.values])
ax[0].set_xticks(wednesday.index)
ax[0].set_xticklabels(wednesday.index, rotation=90)
ax[0].set_title('Wednesday')
# Highlights the times (bars) where the number of people in the gym is less than 40
for i in range(len(wednesday.values)):
     if wednesday.values[i] < 40:
            bar_chart[i].set_color('g')

thursday = gym_data[gym_data['Day'] == 'Thursday'].pivot_table(index='Time', values='Number')
bar_chart = ax[1].bar(x=thursday.index, height=[i[0] for i in thursday.values])
ax[1].set_xticks(thursday.index)
ax[1].set_xticklabels(thursday.index, rotation=90)
ax[1].set_title('Thursday')
# Highlights the times (bars) where the number of people in the gym is less than 40
for i in range(len(thursday.values)):
    if thursday.values[i] < 40:
        bar_chart[i].set_color('g')


plt.ylabel('Number of People in Gym')
ax[1].set_xlabel('Time')
plt.show()



# FRIDAY VS SATURDAY

''' (20/08/2001)                         s'''

fig = plt.figure()
ax = fig.add_subplot()

monday = gym_data[gym_data['Day'] == 'Friday'].pivot_table(index='Time', values='Number')
plt.plot(monday.index, [i[0] for i in monday.values], label='Friday')

tuesday = gym_data[gym_data['Day'] == 'Saturday'].pivot_table(index='Time', values='Number')
plt.plot(tuesday.index, [i[0] for i in tuesday.values], label='Saturday')

ax.set_xticks(monday.index)
ax.set_xticklabels(monday.index, rotation=90)
ax.set_xlabel('Time')
ax.set_ylabel('Number of People in the Gym')
ax.legend()
plt.show()


''' (20/08/2001) After looking at the comparisons of Mon/Wed/Fri vs Tues/Thurs/Fri, I can say that they follow very 
similar trends throughout the day with small differences. '''

