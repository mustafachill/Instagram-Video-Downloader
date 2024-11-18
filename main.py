from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import time


# for working with Google Chrome
driver = webdriver.Chrome()
# for going for Instagram
driver.get("https://www.instagram.com/accounts/login/")

# waitor is for wait for the current element
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))

# for enter username
def enter_username(personal_username):
    username = driver.find_element(By.NAME, "username")
    username.send_keys(personal_username)


# for enter username
def enter_password(personal_password):
    password = driver.find_element(By.NAME, "password")
    password.send_keys(personal_password)


def login_button_clicker():
    # for wait to button to be clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

    # for click to log-in button
    log_in_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    log_in_button.click()



def dismiss_spam_account():
# for not a spam account
    try:
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div[2]/div/div/div/div/div[1]/div/div/div[2]/div[2]/div")))
        dismiss_account_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div[2]/div/div/div/div/div[1]/div/div/div[2]/div[2]/div")
        dismiss_account_button.click()
    except:
        print("Account is clear. There is no problem.")


def dismiss_save_info():
    # for dismissing save info dialog
    try:
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div")))
        dismiss_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div")
        dismiss_button.click()
    except Exception as e:
        print("Dismiss save info button did not find")
        print(e)


def dismiss_notification():
# for i don't want any notification
    try:
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Şimdi Değil')]")))
        dismiss_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Şimdi Değil')]")
        dismiss_button.click()
    except Exception as e:
        print("Dismiss notification button did not find")
        print(e)


def search_button_clicker():
    # for click to search button
    try:
        time.sleep(5)
        print("trying to find search button")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div")))
        search_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div")
        try:
            print("trying to click search button")
            search_button.click()
        except Exception as e:
            for i in range(4): # i = 0,1,2,3
                if i < 3:
                    print("trying to click search button again")
                    search_button.click()
                else:
                    print("there is huge error for search button")
                    print("An error accrued while trying to click search button. Error is: ")
                    print(e)
    except Exception as e:
        print(e)



def make_a_search(username):
    # for making search
    try:
        time.sleep(5)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")))
        searching_area = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
        searching_area.send_keys(username)
        searching_area.send_keys(Keys.RETURN)
    except Exception as e:
        print("An error accrued while trying to type current username. Error is: ")
        print(e)


def click_first_result():
    # for clicking first result
    try:
        time.sleep(5)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/a[1]/div[1]/div/div/div[2]/div/div")))
        first_searching_result = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/a[1]/div[1]/div/div/div[2]/div/div")
        first_searching_result.click()
    except Exception as e:
        print("An error accrued while trying to click current username. Error is: ")
        print(e)


def scroll_and_collect_images():
    # for scrolling and collecting image URLs
    images = set()
    try:
        for _ in range(10):  # Adjust the range for more or less scrolling
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            img_elements = driver.find_elements(By.CSS_SELECTOR, "img")
            images.update([img.get_attribute('src') for img in img_elements])
    except Exception as e:
        print("An error occurred while scrolling and collecting images:", e)
    return images


def downloading(images, keyword):
    # Display collected image URLs for debugging
    print("Collected image URLs:")
    for img_url in images:
        print(img_url)

    # directory for saving images
    path = os.path.join(os.getcwd(), keyword)
    if not os.path.exists(path):
        os.makedirs(path)

    # for downloading images
    for idx, image_url in enumerate(images):
        if image_url.startswith('data:image'):  # Skip data URLs
            continue
        save_as = os.path.join(path, f"{keyword}_{idx}.jpg")
        try:
            wget.download(image_url, save_as)
        except Exception as e:
            print(f"An error occurred while downloading image {image_url}. Error: {e}")

    print(f"Downloaded {len(images)} images to {path}")
    print("******************************************************************")
    print("process is completed")

def process(keyword):
    while True:
        print("What do you want to do?")
        print("******************************")
        print("Press 1 to start process")
        print("Press 0 to stop to precess")
        print("******************************")
        controller = str(input("Press 1 or 0: "))
        if controller == "1":
            # scrolling in the profile
            images = scroll_and_collect_images()
            # downloading the photos
            downloading(images, keyword)
        elif controller == "0":
            break
        else:
            print("Invalid entrance. Please enter 1 or 0.")


''' FUNCTIONS '''
# enter your own profile
enter_username("your nickname here")
enter_password("your password here")
login_button_clicker()
# dismiss useless things
dismiss_spam_account()
dismiss_save_info()
dismiss_notification()
# searching
search_button_clicker()
keyword = input("please enter the username: ")
make_a_search(keyword)
click_first_result()
# start or stop to process
process(keyword)


# screen open for all time.
while True:
    continue