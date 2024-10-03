# python

## 安裝
- 到 python 官網下載安裝包，一路下一步即可
- 安裝完成後，在 cmd 輸入 `python --version` 確認是否安裝成功
> 安裝檢查確認備註
> `python -v` 會進入 python 交互模式
> 進入後要輸入 `exit()` 退出交互模式
> `python --version` 才會顯示 python 版本
> 註解 `#` 單行註解 `'''` 多行註解

## 變數
- 變數命名規則
    - 只能包含字母、數字和底線
    - 不能以數字開頭
    - 不能包含空格
    - 不能使用保留字
    - 可中文
- 變數類型
    - 整數
    - 浮點數
    - 字串
    - 布林值
    - 列表
    - 字典
    - 集合
    - 元組
    - 日期時間
    - 文件
    
> 語法糖
> `round(數字, 小數位數)` 四捨五入
> `數字 // 數字` 絕對值
> `max(數字1, 數字2, 數字3)` 最大值
> `min(數字1, 數字2, 數字3)` 最小值
> `sum(數字1, 數字2, 數字3)` 總和
> `len(數字1, 數字2, 數字3)` 長度
> `type(變數)` 變數類型
> `int(變數)` 轉換為整數
> `float(變數)` 轉換為浮點數
> `str(變數)` 轉換為字串
> `list(變數)` 轉換為列表
> `tuple(變數)` 轉換為元組
> `dict(變數)` 轉換為字典
> `set(變數)` 轉換為集合
> `bool(變數)` 轉換為布林值

### print() 函數
- 檢查通常使用 `print()` 函數 -> 檢查型別 `print(type(變數))`
- 輸出多個變數 `print(變數1, 變數2, 變數3)`
- 輸出多行 
print("""
第一行
第二行
第三行
""")
- f-string 格式化字串 `print(f"字串{變數}")` 不需要管資料型態

### 與使用者互動
- 輸入使用者資訊 `email = input("請輸入 email:")`
- 輸出使用者資訊 `print(email)`
- 兩個 input 連續輸入 `print("請輸入 email: " + email + "請輸入密碼: " + input("請輸入密碼:"))`
- 等同於 `print(f"請輸入 email: {email} 請輸入密碼: {input("請輸入密碼:")}")`

## 判斷式
- 等於 `==`
- 不等於 `!=`
- 大於 `>`
- 小於 `<`
- 大於等於 `>=`
- 小於等於 `<=`
- 且 `and`
- 或 `or`
- 非 `not`
- 如果 `if`
- 如果 否 `else`
- 如果 否 如果 `elif`

### 格式
> if 後的邏輯執行需要縮排
```python
if a > b:
    print("a > b")
elif a > c:
    print("a > c")
else:
    print("a < b")
```

### 清單 ( 陣列 )
基本查詢
```python
students = ["John", "Mary", "Tom", "Jerry"]
```
正向索引值 `[  0   ,   1   ,   2  ,    3   ]`
逆向索引值 `[  0   ,  -3   ,  -2  ,   -1   ]`
> students[-2] = Tom
> students[1:3] = ["Mary", "Tom"] // 1 到 3 之間的元素
> students[1:] = ["Mary", "Tom"] // 1 到最後的元素
> students[:3] = ["John", "Mary", "Tom"] // 0 到 3 之間的元素
> students[:] = ["John", "Mary", "Tom", "Jerry"] // 全部的元素

- 清單的長度 `len(list)`
- 清單的加總 `sum(list)`
- 清單的最大值 `max(list)`
- 清單的最小值 `min(list)`
- 清單的平均值 `sum(list) / len(list)`
- 清單的排序 `list.sort()`

### 清單 ( 陣列 ) 方法
- 新增元素 `list.append(元素)`
- 新增元素 `list.insert(index, 元素)`
- 繼承清單 `list.extend(清單)`
- 刪除元素 `list.remove(元素)`
- 刪除元素 `list.pop(index)` 預設不給 index 值會刪除最後一個元素
- 清空清單 `list.clear()`
- 清單的複製 `list.copy()`
- 清單的反轉 `list.reverse()`
- 清單分割 `list.split(元素)`
- 清單合併 `list.join(元素)`
- 清單排序 `list.sort()`
- 清單排序 `list.sort(reverse=True)`
- 清單排序 `list.sort(key=lambda x: x[1])`
- 清單排序 `list.sort(key=lambda x: x[1], reverse=True)`

### 清單 ( 陣列 ) 確認元素是否在陣列 
```python
if "Tom" in students:
    print("Tom 在陣列中")
```
###  清單 ( 陣列 ) 確認元素 index
```python
students.index("Tom")
```

## 迴圈
- 基本迴圈
```python
for 變數 in 清單:
    print(變數)
```
### 及時中斷
```python
for 變數 in 清單:
    if 變數 == "Tom":
        break
    print(變數)
```
### 跳過迴圈
```python
for 變數 in 清單:
    if 變數 == "Tom":
        continue
    print(變數)
```

#### range() 函數
```python
for i in range(5):
    print(i)
```
> 0 1 2 3 4
```python
for i in range(5, 10):
    print(i)
```
> 5 6 7 8 9
```python
for i in range(5, 10, 2):
    print(i)
```
> 5 7 9

#### 應用
```python
truePassword = "a123456"
for time in range(3):
    password = input("請輸入密碼:")
    if password == truePassword:
        print("登入成功")
        break
    elif password != truePassword and time < 2:
        print("密碼錯誤，還有", 2 - time, "次機會")
    else:
        print("帳號已鎖定")
```

## function 
```python
# 定義函數 `def 函數名稱(參數):`
def printHello():
    print("Hello")

# 呼叫函數 `函數名稱()`
printHello()

# 定義函數 `def 函數名稱(參數):`
def printHello(name = 'tom', age = 19):
    print("Hello", name, "今年", age, "歲")

# 呼叫函數 `函數名稱(參數)`
printHello("John", 20)

# 回傳值 `return 回傳值`
def add(a, b):
    return a + b

# 呼叫函數 `函數名稱(參數)`
print(add(1, 2))
```

### 全域變數與區域變數
- 全域變數 `global 變數名稱`
- 區域變數 `local 變數名稱`

```python
a = 1 # 全域變數
def printA():
    global b # 區域變全域 `global 變數名稱`
    b = 3
    a = 2 # 區域變數
    print(a)

printA()
print(a)
```

### 範例應用
```python
def 加法(x, y):
    return x + y

def 減法(x, y):
    return x - y

def 乘法(x, y):
    return x * y

def 除法(x, y):
    商數 = x // y
    餘數 = x % y
    return 商數, 餘數

while True:
    計算類型 = input("請輸入計算類型 (1)加 (2)減 (3)乘 (4)除 (或按其他任意鍵關閉程式): ")
    
    if 計算類型 in ("1", "2", "3", "4"):
        數字1 = int(input("請輸入第一個整數："))
        數字2 = int(input("請輸入第二個整數："))
        
        if 計算類型 == "1":
            print(f"{數字1} 加 {數字2} 等於 {加法(數字1, 數字2)}")
        elif 計算類型 == "2":
            print(f"{數字1} 減 {數字2} 等於 {減法(數字1, 數字2)}")
        elif 計算類型 == "3":
            print(f"{數字1} 乘 {數字2} 等於 {乘法(數字1, 數字2)}")
        elif 計算類型 == "4":
            if 數字1 % 數字2 == 0:
                print(f"{數字1} 除以 {數字2} 等於 {除法(數字1, 數字2)[0]}") # 可整除
            else:
                print(f"{數字1} 除以 {數字2} 等於 {除法(數字1, 數字2)[0]} 餘 {除法(數字1, 數字2)[1]}") # 不可整除顯示餘數
    else:
        print("程式關閉")
        break
```

## 字典 ( object )
```python
students = {
    "name": "John",
    "age": 20,
    "gender": "male"
}
```
- 字典的查詢 `字典名稱[key]` 或使用 `字典名稱.get(key, "查無資料")`
```python
print(students["name"]) # John
print(students.get["name", "查無資料"]) # John
```
- 字典新增
```python
students["color"] = ["red", "blue"] # 新增一個陣列
students["address"] = "台北市" # 新增一個 key
```
- 字典的修改
```python
students["name"] = "Tom"
```
- 字典的刪除
```python
students.pop("name") # 刪除 name 的 key
students.popitem() # 刪除最後一個項目
```

- key value 應用
```python
for data in students.keys(): # 取得 key
    print(data)
for data in students.values(): # 取得 value
    print(data)
for key, value in students.items(): # 取得 key 和 value
    print(key, value)
```

## 模組
```python
# 模組的引入
`import 模組名稱` # 可用該模組全部資源

# 模組的暱稱
`import 模組名稱 as 新模組名稱`

# 特定模組的 function
`from 模組名稱 import 函數名稱`
```

### 引入第三方套件
`pip install requests` 擷取伺服器資料
擷取天氣資料
```python
import requests

city = input("請輸入城市名稱：")
api = "7f1a9376d21b282af01bda4bc8f83244"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"

weather = requests.get(url)
temp = int(weather.json()["main"]["temp"] - 273.15)

print(f"{city} 目前的氣溫是 {temp} 度")
```

## class 類別
- 定義類別 `class 類別名稱:`
```python
class Game:
    def __init__(self, 參數):
        self.屬性 = 參數
```

#### 範例
```python
class GamePlayer:
    level = 1
    exp = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

player1 = GamePlayer("小明", 24)
player2 = GamePlayer("小華", 22)

print(player1.name)
print(player2.age)
```

### Method 方法
- 定義方法 `def 方法名稱(self, 參數):`
```python
class GamePlayer:
    level = 1
    exp = 0

    def __init__(self, name, age):
        self.姓名 = 姓名
        self.年齡 = 年齡

    def truck(self):
        print(f"{self.姓名} 一個箭步衝向了敵人！")

    def watch(self):
        print(f"{self.姓名} 用敏銳眼光環顧四周。")

player1 = 遊戲角色("小明", 24)
player2 = 遊戲角色("小華", 22)

player1.truck()
player2.watch()
```

#### 繼承
- 定義繼承 `class 子類別名稱(父類別名稱):`
```python
class GamePlayer:
    level = 1
    exp = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def truck(self):
        print(f"{self.name} 一個箭步衝向了敵人！")

    def watch(self):
        print(f"{self.name} 用敏銳眼光環顧四周。")

class fighter(GamePlayer):
    def action(self):
        print(f"{self.name} 一個箭步衝向了敵人！")

player1 = 遊戲角色("小明", 24)

player1.truck()
player2.watch()
```

