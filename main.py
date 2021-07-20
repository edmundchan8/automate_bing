from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

# ENTER YOUR OUTLOOK EMAIL HERE
# EMAIL = ""

# ENTER YOUR OUTLOOK PASSWORD HERE
# PASSWORD = ""

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

bing_sign_in_url = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252fsearch%253fq%253dword%2526search%253d%2526form%253dQBLH%2526wlexpsignin%253d1%26sig%3d1F8B2F1DCF31628B34163F64CE826362&wp=MBI_SSL&lc=1033&CSRFToken=d11ac9cf-3999-4a31-9f2f-c1bb32f4e8d4&aadredir=1"
driver.get(bing_sign_in_url)

# sleep timers added in to delay the speed of logging in
# automat entering email
time.sleep(1)
login = driver.find_element_by_name("loginfmt")
login.send_keys(EMAIL)
enter_login = driver.find_element_by_id("idSIButton9").click()


# automate entering in password
time.sleep(1)
password = driver.find_element_by_name("passwd")
password.send_keys(PASSWORD)
enter_password = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input').click()


# slight delay before outlook returns you to the bing search page
time.sleep(1)

# list of random words
random_words = ["glue",
                "dark",
                "help",
                "snow",
                "preserve",
                "meaty",
                "yard",
                "second",
                "mixed",
                "boorish",
                "tight",
                "bag",
                "fierce",
                "government",
                "flagrant",
                "imperfect",
                "eye",
                "playground",
                "harmony",
                "snakes",
                "follow",
                "romantic",
                "parched",
                "wealthy",
                "hover",
                "abstracted",
                "zesty",
                "interrupt",
                "amazing",
                "growth",
                "company",
                "erratic",
                "sin",
                "exist",
                "quiet",
                "physical",
                "mug",
                "deeply",
                "tour",
                "heat",
                "right",
                "gleaming",
                "society",
                "want",
                "slippery",
                "farm",
                "nutritious",
                "writing",
                "object",
                "wren"]

# for loop that will delay for 1 second, find the search bar, choose a random word and etner it into the search bar, then hit enter.  Afterwards, it clears the search bar.  Repeats 30 times
for clicking in range(1, 30):
    time.sleep(1)
    search = driver.find_element_by_name("q")
    search.send_keys(random.choice(random_words))
    search.send_keys(Keys.ENTER)
    driver.find_element_by_name("q").clear()
