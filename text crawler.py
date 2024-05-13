import subprocess
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import asyncio
import sys
from selenium.common.exceptions import TimeoutException
import subprocess
import pyperclip
import keyboard
import shutil
yy = """

% ·····································································································
% : __    __       ___      .__   __.         ___      .__   __.  __    __     .___________. __    __ :
% :|  |  |  |     /   \     |  \ |  |        /   \     |  \ |  | |  |  |  |    |           ||  |  |  |:
% :|  |__|  |    /  ^  \    |   \|  |       /  ^  \    |   \|  | |  |__|  |    `---|  |----`|  |  |  |:
% :|   __   |   /  /_\  \   |  . `  |      /  /_\  \   |  . `  | |   __   |        |  |     |  |  |  |:
% :|  |  |  |  /  _____  \  |  |\   |     /  _____  \  |  |\   | |  |  |  |        |  |     |  `--'  |:
% :|__|  |__| /__/     \__\ |__| \__|    /__/     \__\ |__| \__| |__|  |__|        |__|      \______/ :
% :                                                                                                   :
% :  ___     ___    ____     ___     ___     ___    ___    _  _       __    _____                     :
% : / _ \   / _ \  |___ \   / _ \   / _ \   / _ \  |__ \  | || |     / /   | ____|                    :
% :| | | | | (_) |   __) | | (_) | | (_) | | (_) |    ) | | || |_   / /_   | |__                      :
% :| | | |  \__, |  |__ <   > _ <   > _ <   > _ <    / /  |__   _| | '_ \  |___ \                     :
% :| |_| |    / /   ___) | | (_) | | (_) | | (_) |  / /_     | |   | (_) |  ___) |                    :
% : \___/    /_/   |____/   \___/   \___/   \___/  |____|    |_|    \___/  |____/                     :
% ·····································································································

"""
print(f"\033[92m{yy}\033[0m")
time.sleep(5)
user_name = os.getlogin()
so_video = int(input(f'Số Video cần Crawl text : '))
chromium_binary_path = 'C:\\Program Files\\Chromium\\Application\\chrome.exe'
chromium_driver_path = 'C:\\chromedriver\\chromedriver.exe'
service = Service(executable_path=chromium_driver_path)
options = webdriver.ChromeOptions()
options.binary_location = chromium_binary_path
options.add_argument('--disable-features=AutoUpdate')
options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-running-insecure-content")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--disable-dev-shm-usage")
# options.add_argument('--headless')
# Chỉ định đường dẫn đến thư mục profile
user_data_dir = f'C:\\Users\\{user_name}\\AppData\\Local\\Chromium\\User Data\\'
options.add_argument(f'--user-data-dir={user_data_dir}')
script_path = os.path.abspath(__file__)
current_directory = os.path.dirname(script_path)
mp4_files = [filename for filename in os.listdir(current_directory) if filename.endswith(".mp4")]

def edit_file_conten(folder_path):
	for filename in os.listdir(folder_path):
		if filename.endswith(".txt"):
			file_path = os.path.join(folder_path, filename)
			with open(file_path, "r") as file:
				lines = file.readlines()
			
			with open(file_path, "w") as file:
				for line in lines:
					file.write(line.rstrip() + " \n")
	for filename in os.listdir(folder_path):
		if filename.endswith(".txt"):
			file_path = os.path.join(folder_path, filename)
			with open(file_path, "r") as file:
				lines = file.readlines()
			
			with open(file_path, "w") as file:
				for line in lines:
					for i in line:
						if i == "\n":
							line = line.replace(i, "")
					file.write(line)
	for filename in os.listdir(folder_path):
		if filename.endswith(".txt"):
			file_path = os.path.join(folder_path, filename)
			with open(file_path, "r") as file:
				text = file.read()
			modified_text = text.replace(". ", ".")
			with open(file_path, "w") as file:
				file.write(modified_text)

driver = webdriver.Chrome(service=service, options=options)
for x in mp4_files[0:so_video]:
	
	name_folder = x.split('.')[0]
	if name_folder.endswith(" "):
		name_folder = name_folder[:-1]
		if name_folder.endswith(" "):
			name_folder = name_folder[:-1]
			if name_folder.endswith(" "):
				name_folder = name_folder[:-1]
				if name_folder.endswith(" "):
					name_folder = name_folder[:-1]
	if name_folder.endswith("."):
		name_folder = name_folder[:-1]
		if name_folder.endswith("."):
			name_folder = name_folder[:-1]
			if name_folder.endswith("."):
				name_folder = name_folder[:-1]
				if name_folder.endswith("."):
					name_folder = name_folder[:-1]
					if name_folder.endswith("."):
						name_folder = name_folder[:-1]
						if name_folder.endswith("."):
							name_folder = name_folder[:-1]
	print(f'Tên thư mục sẽ tạo: {name_folder}')
	des = f'{current_directory}\{name_folder}'
	if not os.path.exists(des):
		os.makedirs(des)
		print(f'Đã tạo thư mục {name_folder}')
	else:
		pass
	driver.get("https://www.veed.io/workspaces/")

	create_project_button = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[action="create"].sc-YnwpJ.ehdbHS')))
	create_project_button.click()

	try:
		button_popup = WebDriverWait(driver, 100).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="@editor/close-btn"]'))
		)
		button_popup.click()
	except Exception as e:
		pass

	upload_file_button = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="@upload-file"]')))
	upload_file_button.click()
	pyperclip.copy(f'{current_directory}\{x}')
	time.sleep(0.5)
	keyboard.press_and_release('ctrl+v')
	time.sleep(0.5)
	pyautogui.press("enter")
	time.sleep(15)
	try:
		button_error = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="@workspace-settings/invite-collaborator-confirmation"]'))
		)
		button_error.click()
	except Exception as e:
		pass

	subtitles_button = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="@editor/subtitles"]')))
	subtitles_button.click()

	subtitles_options = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="@editor/subtitles-option/automatic"]')))
	subtitles_options.click()

	subtitles_options_start = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="@editor/subtitles/create-subtitles-button"]')))
	subtitles_options_start.click()

	element_wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-contents="true"]')))

	span_elements = driver.find_elements(By.XPATH, '//span[@data-text="true"]')
	all_text_content = ""
	
	for span_element in span_elements:
		text_content = span_element.text.strip()
		all_text_content += text_content + '\n'
	output_file_path = os.path.join(f'{current_directory}\{name_folder}', f'{name_folder}.txt')

	with open(output_file_path, 'w', encoding='utf-8') as file:
		file.write(all_text_content)
	folder_path = des
	edit_file_conten(folder_path)
	file_path = f'{current_directory}\{x}'
	shutil.move(file_path, des )
	print(f'Đã Crawl {name_folder} thành công rồi nhé')
	print('Done!')
	time.sleep(5)
driver.quit()
sys.exit()