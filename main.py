from selenium import webdriver
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

class InternetSpeedBot:
    def __init__(self, chrome_driver_path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(60)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        print(self.up.text)
        print(self.down.text)
        with open('internet_test.txt', 'w') as file:
            file.write(f"Download speed: {self.down.text} Mbps \nUpload speed: {self.up.text} Mbps")


test = InternetSpeedBot(CHROME_DRIVER_PATH)
test.get_internet_speed()