from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def time_to_sec(time):
    return int(time[:2])*60 + int(time[3:])

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


f = open('login.txt', 'r')
ID = f.readline()
PASSWORD = f.readline()
f.close()


driver = webdriver.Chrome(options=chrome_options)
url = 'https://www.kifin.or.kr/login/loginpage.do?agreementYn=&memberStatusCd=&error=&pwdErrCode=&currentMenuId=008001&signature=&tp='
print("=====================================================================================================================")
print("====================================== 로그인 페이지 열었음 ===========================================")
print("=====================================================================================================================")
driver.get(url)
driver.implicitly_wait(time_to_wait=2)

id_box = driver.find_element(By.NAME, "j_username")
pw_box = driver.find_element(By.NAME, "j_password")
id_box.send_keys(ID)
pw_box.send_keys(PASSWORD)

btn = driver.find_element(By.CLASS_NAME, "btn_login")
btn.click()

sleep(1)
print("====================================== 로그인 완료했음 ===========================================")
print("=====================================================================================================================")
btn = driver.find_element(By.CLASS_NAME, "ico_my")
btn.send_keys(Keys.ENTER)
print("1111")

print("====================================== 마이페이지 열었음 ===========================================")
print("=====================================================================================================================")
btn = driver.find_elements(By.CLASS_NAME, "btn_status")[0]
btn.send_keys(Keys.ENTER)
print("2222")
sleep(1)

print("====================================== 수강목록 열었음 ===========================================")
print("=====================================================================================================================")
# 첫 번째 과정(내 기준 파생)
# btn = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[2]/div[2]/div[2]/ul/li[1]/div[1]/p")
# 두 번째 과정(내 기준 펀드)
btn = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[2]/div[2]/div[2]/ul/li[2]/div[1]/p")
print("3333")
btn.click()
sleep(1)

while True: # 무한루프 돌건데, 어차피 다음 목록 없으면 프로그램 종료하겠지 뭐...
    print("====================================== 선택한 과정 목록 열었음 ===========================================")
    print("=====================================================================================================================")
    print("4444")
    sleep(10)
    btns = driver.find_elements(By.CLASS_NAME, "btn-primary")
    print(btns[0])
    btns[0].click()

    print("====================================== 안 들은 강의 열었음 ===========================================")
    print("=====================================================================================================================")
    main = driver.window_handles
    print("5555")
    # driver.switch_to.window(main[1])
    # driver.close()
    driver.switch_to.window(main[2])
    driver.find_element(By.XPATH, '/html/body/div/div/section/div[3]').click()
    print("6666")
    sleep(1)
    full_cnt = int(driver.find_element(By.XPATH, '/html/body/div/div/section/div[2]/div[3]/div/span').text[2:])
    print(full_cnt)
    while True:
        # 동영상 시간을 받아 온다
        t = driver.find_element(By.XPATH, '/html/body/div/div/section/div[2]/div[2]/span').get_attribute("play_time")
        cnt = int(driver.find_element(By.XPATH, '/html/body/div/div/section/div[2]/div[3]/div/em').text)
        print(t, time_to_sec(t)+5, cnt)
        # 혹시나 있을 상황을 대비해 시간 + 8초를 기다린다
        sleep(time_to_sec(t)+8)
        btn = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/button')
        # "다음" 버튼을 클릭한다
        btn.click()
        print("7777")
        print(str(cnt), "/", str(full_cnt))
        if cnt == full_cnt:
            break
        # 클릭하고 다음 동영상 로딩 시간을 위해 7초 슬립
        sleep(7)
    sleep(5)
    driver.switch_to.window(main[0])
print("Bye Bye!!")