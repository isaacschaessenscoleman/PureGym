# PureGym

This is a simple data science project which involves collecting, storing and analysing the data from my gym's website in order to find the optimum times to go to 
the gym. In this case, the optimum times are defined by the points in the day where the gym has the least number of people. At times when there aren't many people
in the gym it's more peaceful and there aren't any waiting times to use certain machines/equipment. I currently go to the gym on Monday, Wednesday and Friday 
at about 14:00 - 16:00. However, through this project I hope to find the best times and combinations of days where the gym is most quiet. 

On the gym's website it shows the number of people in the gym at that point in time. As seen in the image below, it shows the number in the bottom left hand
of the screen. This is how I was able to create this project.
[![Screenshot-2021-08-20-at-16-15-41.png](https://i.postimg.cc/sgYvq3Hh/Screenshot-2021-08-20-at-16-15-41.png)](https://postimg.cc/3kw8DQT8)

Below is the order in which you should look through the files:

## 1. CollectingData.py
This file consists of my python code which scraped data from the website and stored it in a csv file. I used Selenium WebDriver to scrape the data which is a
web framework that allows you to interact with the web through your code. The program starts by logging into the website using my details and then continuously 
scraping the value of the number of people in the gym every thirty minutes. As seen in the code, the program runs forever through a 'While True' loop and stops
executing manually. When I first created the program I scraped the data every five minutes but noticed that it was a waste of memory/storage as not much changes
in the gym every five eminutes. From observing the data, it seemed that thirty minute intervals was the best representation of the data. Additionally, the average
gym session for someone is roughly 30-60 minutes, thus collecting data every thirty minutes seemed right. 
The code also shows the process of storing this data in a csv file.

## 2. data.csv
This is the csv file that was created as a result of the 'CollectingData.py' file. It consists of four columns: date, day of the week, time and number of people
in the gym. 


## 3. (JupyterNotebook)AnalysingGymData.ipymb
This file is a Jupyter Notebook which shows the process of my analysis - the aim was to find the optimum times of the gym (when it's most quiet). I used NumPy, 
pandas and matplotlib packages to help gather insights and draw conclusions from the data. Through the manipulation of pandas DataFrames and the data
visualisation tools of matplotlib, it was made clear to me the best times to go to the gym. 
Furthermore, I briefly talk about the limitations of the project with regards to data collection. 


## 4. Functions.py
This is an additional file that is not really a part of the project. It's a file consisting of different functions I created to help with visualising the data.
These functions are not used anywhere in the project and were simply created as an experiment.
