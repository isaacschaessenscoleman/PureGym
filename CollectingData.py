import caffeine
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import date

week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(time.localtime().tm_min)

driver = webdriver.Chrome(executable_path="/Users/isaaccoleman/Documents/Python/chromedriver")
driver.get('https://www.puregym.com/members/')
username_element = driver.find_element_by_name("username")
username_element.send_keys('isaaccoleman35@gmail.com')
password_element = driver.find_element_by_name("password")
# When the program was active I would've had my password in the argument below rather than '####'
password_element.send_keys("####")
login_button = driver.find_element_by_xpath("/html/body/div/main/div/form[2]/div[4]/button").click()
accept_cookies = driver.find_element_by_xpath('//*[@id="coiPage-1"]/div[2]/button[2]').click()

while True:

    if time.localtime().tm_min == 0 or time.localtime().tm_min == 30:
        driver.refresh()
        text = driver.find_element_by_xpath('//*[@id="people_in_gym"]/span').text

        # This is the message the website gives when the gym is closed
        if text == '10 OR FEWER PEOPLE':
            # sleeps for 60 seconds so that the program doesn't continuously loop through this block of code for the
            # entire 30th/60th minute
            time.sleep(60)
            continue

        else:
            number = int(text.replace(' PEOPLE',''))

            with open('/Users/isaaccoleman/PycharmProjects/Puregym/data.csv', 'a') as file:
                today_date = date.today()
                current_time = time.localtime()
                file.write('\n{},{},{},{}'.format(today_date,week_days[today_date.weekday()],time.strftime("%H:%M", current_time),number))
            time.sleep(60)

    else:
        continue



current_time = time.localtime()
print(current_time, type(current_time))
#print(current_time.tm_)
