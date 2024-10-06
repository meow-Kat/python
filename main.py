# 購票腳本
import requests
import re
import json
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup

area_url_list = {}

def getAreaUrl(id):
    script_tags = soup.find_all('script')
    for script in script_tags:
        if 'areaUrlList' in script.text:
            # 使用正則表達式提取 areaUrlList 的內容
            match = re.search(r'var areaUrlList = ({.*?});', script.text, re.DOTALL)
            if match:
                area_url_list = json.loads(match.group(1))  # 使用 json.loads 轉成字典
            break
    return area_url_list.get(id, "查無資料")  # 使用 get 方法以避免 KeyError

url = "https://tixcraft.com"



# target = input("輸入購票網址：")
# budget = input("輸入購買預算：")
# budget = int(budget)
# target = target.split('/')[-1]
# newUrl = url + target

headers = {
    "Cookie": "SID=h8dfslnsfbicgfoqiujc845i3j; _csrf=481b0961c9b8376dd89be3b6ee45b767c772697faf141b0a0bd40d6d7c9a5d4fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%222zb2bvwKOHCbgJguW0kFgIdckbPsXxMi%22%3B%7D",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

newUrl = url + "/activity/game/" + "24_wubaiopr"
budget = 2500
ticket_num = 4

response = requests.get(newUrl)

soup = BeautifulSoup(response.text, 'html.parser')
tickets = soup.find_all('button', class_='btn btn-primary text-bold m-0')

# 取得最後一筆資料的 data-href
if tickets:  # 確保 tickets 陣列不為空
    last_ticket = tickets[-1]  # 取得最後一筆資料
    last_href = last_ticket.get('data-href')  # 取得 data-href
    print(last_href)  # 輸出最後一筆資料的 data-href

ticketSiteList = requests.get(last_href)

soup = BeautifulSoup(ticketSiteList.text, 'html.parser')

liTags = soup.find_all('li', class_='select_form_b')

first_area_url = ''

for li in liTags:
    a_tag = li.find('a')  # 在每個 li 標籤中找到 a 標籤
    if a_tag:
        id = a_tag.get('id')  # 獲取 a 標籤的 id
        text = a_tag.get_text()  # 獲取 a 標籤的文本
        price = int(text.split()[0][-4:]) # 取得價格
        if "remaining" in text:  # 檢查文本中是否包含 "剩餘"
            if price <= budget:
                first_area_url = getAreaUrl(id)
                break
        else:
            print('已售完')

response = requests.get(first_area_url)

soup = BeautifulSoup(response.text, 'html.parser')

TicketForm_verifyCode_image = soup.find('img', id='TicketForm_verifyCode-image')
ticketNum = soup.find('select', class_='form-select mobile-select')
ticket_num = len(ticketNum.find_all('option')) - 1
formTicket = ticketNum.get('name').split('[')[-1].split(']')[0]
src = TicketForm_verifyCode_image.get('src') if TicketForm_verifyCode_image else None

# 驗證碼圖片
image_url = url + src

while True:
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))  # 打開圖片
    image.show()
    if input("驗證碼是否理解？(y/n)") == 'y':
        break

verifyCode = input("輸入驗證碼：")
csrf_token = soup.find('input', {'name': '_csrf'}).get('value') if soup.find('input', {'name': '_csrf'}) else ''

# 獲取表單動作 URL
form = soup.find('form', id='form-ticket-ticket')
if form:
    action_url = url + form['action']
else:
    print("找不到表單")
    exit()

# 表單資料
formData = {
    "_csrf": csrf_token,
    f"TicketForm[ticketPrice][{formTicket}]": str(ticket_num),  # 購買數量
    f"TicketForm[priceSize][{formTicket}]": "1",
    "TicketForm[verifyCode]": verifyCode,  # 驗證碼
    "TicketForm[agree]": "1"  # 同意條款
}

headers['Content-Type'] = 'application/x-www-form-urlencoded'

response = requests.post(action_url, data=formData, headers=headers)  # 發送 POST 請求
print(response.text)

# 失敗 應該有 WAF 會擋掉
