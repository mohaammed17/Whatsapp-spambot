import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/mohammed/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

# Wait for the user to scan the QR code and proceed manually
input("Enter anything after scanning QR code and waiting for WhatsApp to load")

name = input("Enter the name here: ")
msg = input("Enter the message here: ")
count = int(input("Enter the count here: "))

try:
    user = driver.find_element(by=By.XPATH, value="//span[@title='{}']".format(name))
    user.click()

    for index in range(count):
        msg_box = driver.find_element(by=By.XPATH, value="//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
        msg_box.send_keys(msg)

        # Give a small delay before clicking send to avoid WhatsApp detecting it as spam
        time.sleep(0.5)

        # Click the send button to send the message
        send_button = driver.find_element(by=By.XPATH, value="//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span")
        send_button.click()

    print("Success")
except Exception as e:
    print("Error:", e)
finally:
    driver.quit()
