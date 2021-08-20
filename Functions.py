import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gym_data = pd.read_csv('/Users/isaaccoleman/PycharmProjects/Puregym/data.csv')

'''Producing a pivot table with the days of the week as the index, the times throughout the day as columns, and the mean 
number of people in the gym as the values.'''

days = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mean_members = np.round(gym_data.pivot_table(values='Number', index='Day', columns='Time'), 1)
mean_members = mean_members.reindex(days)
print(mean_members.to_string())

'''Producing a pivot table and bar chart of the average number of people in the gym at different times of the day.'''
average_day = gym_data.pivot_table(index='Time', values='Number')
ax = plt.axes()
#print(average_day.to_string())

plt.bar(x=average_day.index, height=[i[0] for i in average_day.values])
ax.set_xticks(average_day.index)
ax.set_xticklabels(average_day.index, rotation=90)
plt.xlabel('Time')
plt.ylabel('Average Number of People in the Gym')
plt.title('Average Gym Activity throughout the Day')
#plt.show()


def specific_day_graph(day):
    ''' This function accepts a single argument which is a string of a day of the week (e.g. 'Monday'). The function
    returns a bar chart with 'Average Number of People in the Gym' on the y-axis and 'Time' throughout the day on the
    x-axis. The bar chart highlights the times where there are less than 40 people in the gym.'''

    plt.figure()
    ax = plt.axes()

    specific_day_average = gym_data[gym_data['Day'] == day].pivot_table(index='Time', values='Number')

    bar_chart = plt.bar(x=specific_day_average.index, height=[i[0] for i in specific_day_average.values])
    ax.set_xticks(specific_day_average.index)
    ax.set_xticklabels(specific_day_average.index, rotation=90)
    plt.xlabel('Time')
    plt.ylabel('Average Number of People in the Gym on {}'.format(day))
    plt.title('Average Gym Activity throughout {}'.format(day))
    # Highlights the times (bars) where the number of people in the gym is less than 40
    for i in range(len(specific_day_average.values)):
        if specific_day_average.values[i] < 40:
            bar_chart[i].set_color('g')
    plt.show()

specific_day_graph('Monday')

def comparing_days(*args):
    ''' This function accepts multiple strings of the days of the week. It then returns a bar chart of the number
     of people in the gym against time, for each day of the week so that you are able to compare the different days.
    The bar charts highlight the times where there are less than 40 people in the gym.'''

    fig, ax = plt.subplots(len(args), sharex=True, constrained_layout=True)
    for i in range(len(args)):
        specific_day_average = gym_data[gym_data['Day'] == args[i]].pivot_table(index='Time', values='Number')

        bar_chart = ax[i].bar(x=specific_day_average.index, height=[i[0] for i in specific_day_average.values])
        ax[i].set_xticks(specific_day_average.index)
        ax[i].set_xticklabels(specific_day_average.index, rotation = 90)
        ax[i].set_title(args[i])
        # Highlights the times (bars) where the number of people in the gym is less than 40
        for i in range(len(specific_day_average.values)):
            if specific_day_average.values[i] < 40:
                bar_chart[i].set_color('g')
    plt.ylabel('Number of People in Gym')
    ax[len(args)-1].set_xlabel('Time')
    plt.show()

comparing_days('Monday','Tuesday')

def comparing_days_linegraph(*args):
    ''' This function accepts multiple strings of the days of the week. The function returns a line graph with 'Number of
    People in the Gym' on the y-axis' against 'Time' throughout the day on the x-axis. Each plot (for each day) is
    plotted on the same graph so you can easily compare the days.'''

    fig = plt.figure()
    ax = fig.add_subplot()
    # simply to overcome an axes problem I was having
    plt.plot(mean_members.columns,[15 for i in mean_members.columns], color='white')

    for i in range(len(args)):
        specific_day_average = gym_data[gym_data['Day'] == args[i]].pivot_table(index='Time', values='Number')

        plt.plot(specific_day_average.index, [i[0] for i in specific_day_average.values], label = args[i])

    ax.set_xticks(specific_day_average.index)
    ax.set_xticklabels(specific_day_average.index, rotation=90)
    ax.set_xlabel('Time')
    ax.set_ylabel('Number of People in the Gym')
    ax.legend()
    plt.show()

comparing_days_linegraph('Friday','Saturday')





