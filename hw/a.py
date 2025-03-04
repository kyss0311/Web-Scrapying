import requests
from pyquery import PyQuery as pq

# 發送 HTTP GET 請求以獲取 HTML 內容
url = 'https://goodinfo.tw/tw/StockDetail.asp?STOCK_ID=2330'
response = requests.get(url)

# 使用 PyQuery 解析 HTML
doc = pq(response.content)

# 畫面上的 HTML 內容
print(doc.html())
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# # 設定瀏覽器選項（無頭模式）
# chrome_options = Options()
# chrome_options.add_argument('--headless')  # 無頭模式，不顯示瀏覽器介面
# chrome_options.add_argument('--disable-gpu')  # 如果有 GPU 問題，可加上這行
# chrome_options.add_argument('--incognito')  # 無痕模式
# chrome_options.add_argument('--blink-settings=imagesEnabled=false')  # 不載入圖片，加速效率
#
# # 初始化 Chrome 瀏覽器
# driver = webdriver.Chrome(options=chrome_options)
#
# # 瀏覽器請求目標網站
# driver.get('https://goodinfo.tw/tw/StockDetail.asp?STOCK_ID=2330')
#
# # 等待頁面加載完成，可以設定隱式等待
# driver.implicitly_wait(10)  # 最長等待 10 秒
#
# # 獲取渲染後的頁面源代碼
# html_content = driver.page_source
#
# # 關閉瀏覽器
# driver.quit()
#
# # 使用 PyQuery 解析渲染後的 HTML
# from pyquery import PyQuery as pq
# doc = pq(html_content)
# print(doc)
#
# # 提取你需要的資訊，例如股票名稱和價格
# stock_name = doc('title').text()
# current_price = doc('.stt-row0 td:nth-child(2)').text()
#
# print(f"股票名稱：{stock_name}")
# print(f"目前股價：{current_price}")
#
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # 等待指定元素出現
# wait = WebDriverWait(driver, 10)
# target_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.你的目標元素')))
