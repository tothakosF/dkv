import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By


def is_connected_to_wifi():
    result = subprocess.run(
        ["netsh", "interface", "show", "interface"], capture_output=True, text=True, check=True)
    output_lines = result.stdout.split('\n')

    if "Connected" in output_lines[4]:
        return True
    else:
        return False


if __name__ == "__main__":
    stable = True
    while stable:
        if is_connected_to_wifi():
            wifi = subprocess.check_output(
                ['netsh', 'WLAN', 'show', 'interfaces'])
            data = wifi.decode('utf-8')
            if "DKV_Free_Wifi" in data:
                stable = False
                print("Connceted to DKV")
                print("Logging in...")

                geckodriver_path = r'C:\Users\totha\.wdm\drivers\geckodriver\win64\0.33\geckodriver.exe'

                driver = webdriver.Firefox(executable_path=geckodriver_path)

                driver.get('http://www.wifihotspot.hu/dkv/busz/hslogin.php')

                time.sleep(5)

                button = driver.find_element(By.ID, 'submit')

                button.click()

                time.sleep(5)

                driver.quit()
            else:
                print("Connected, but not to DKV")

        else:
            print("Not connected")
        time.sleep(1)
