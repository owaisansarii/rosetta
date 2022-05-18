from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def login(username, password):
    time.sleep(2)
    # find input[data-qa='Email']
    # find_element(by=By.XPATH, value=xpath)
    driver.find_element(
        by=By.XPATH, value='//input[@data-qa="Email"]').send_keys(username)
    # find input[data-qa='Password']
    driver.find_element(
        by=By.XPATH, value='//input[@data-qa="Password"]').send_keys(password)
    # setTimeout(() => {
    #   driver.findElement(By.css("div[data-qa='SignInButton']")).click();
    # }, 2000);
    time.sleep(2)
    driver.find_element(
        by=By.XPATH, value='//div[@data-qa="SignInButton"]').click()
    time.sleep(2)


def clickLaunchpad():
    # launch-pad
    # wait for launch-pad to load
    time.sleep(10)
    # find launch-pad
    driver.find_element(
        by=By.XPATH, value='//div[@data-qa="launch-pad"]').click()
    time.sleep(2)


def clickonLeasson3():
    # lesson-number-2
    # wait for lesson-number-2 to load
    time.sleep(1)
    # find lesson-number-2
    driver.find_element(
        by=By.XPATH, value='//div[@data-qa="lesson-number-2"]').click()
    time.sleep(2)


def clickOnLesson3Button():
    # PathButtonCourseMenu-PATH_123387265
    # wait for PathButtonCourseMenu-PATH_123387265 to load
    time.sleep(3)
    # find PathButtonCourseMenu-PATH_123387265
    driver.find_element(
        by=By.XPATH, value='//button[@data-qa="PathButtonCourseMenu-PATH_123387265"]').click()
    time.sleep(2)


if __name__ == "__main__":
    opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=opt)
driver.get("https://login.rosettastone.com/#/login")
login("neelam30rawat@gmail.com", "rosetta@1234")
clickLaunchpad()
time.sleep(5)
# allow microphone access

clickonLeasson3()
time.sleep(5)
clickOnLesson3Button()
time.sleep(10)
# PromptButton
driver.find_element(
    by=By.XPATH, value='//button[@data-qa="PromptButton"]').click()
time.sleep(20)
while True:
    # ActComponent-0
    try:
        driver.find_element(
            by=By.XPATH, value='//div[@data-qa="ActComponent-0"]').click()
        time.sleep(5)
    except NoSuchElementException:
        break
time.sleep(2)
