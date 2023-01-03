from multiprocessing import Pool
from random import choice
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-gpu')
options.add_argument('--disable-infobars')
options.add_argument("--mute-audio")
options.add_argument("--disable-blink-features")
options.add_argument('--profile-directory=Default')
options.add_argument("--mute-audio")
options.add_extension("MetaMask.crx")
options.add_argument("--window-size=1250,900")

f = open('mnemonic.txt', 'r')
i = 0
for line in f:
    i
    i += 1
with open("mnemonic.txt", "r") as f:
    mnemonic = f.read().split('\n')
    i = i - 1


def work(mnemonic):
    try:
        driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
        wait = WebDriverWait(driver, 30)
        driver.switch_to.window(driver.window_handles[0])
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@role="button"]'))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'first-time-flow__button'))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'MuiInput-input'))).send_keys(mnemonic)
        wait.until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys("Papsgpasgpap2125125")
        wait.until(EC.element_to_be_clickable((By.ID, 'confirm-password'))).send_keys("Papsgpasgpap2125125")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'first-time-flow__terms'))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))).click()
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))).click()
        driver.get("https://quokkaswap.com/r/77803") # реф-ка
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='main']/nav/div/ul[2]/li/a"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, 'kvwalletmodal_metamask_btn'))).click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[2])
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))).click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='main']/div[5]/section/div/div/div[2]/div[5]/p"))).click()
        telega = "@" + "".join([choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(8)])
        twitter = "https://twitter.com/rdy_crypto/status/" + "".join([choice("0123456789") for _ in range(8)])
        facebook = "https://www.facebook.com/watch/?v=" + "".join([choice("0123456789") for _ in range(8)])
        youtube = "https://www.youtube.com/@RudyCrypto/videos"
        wait.until(EC.element_to_be_clickable((By.NAME, 'telegram'))).send_keys(telega)
        wait.until(EC.element_to_be_clickable((By.NAME, 'twitter'))).send_keys(twitter)
        wait.until(EC.element_to_be_clickable((By.NAME, 'facebook'))).send_keys(facebook)
        wait.until(EC.element_to_be_clickable((By.NAME, 'youtube'))).send_keys(youtube)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='main']/div[5]/section/div[2]/div[3]/div[2]/a"))).click()
        time.sleep(2)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    p = Pool(processes=2) # кол-во потоков
    p.map(work, mnemonic)