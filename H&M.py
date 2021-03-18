from selenium.webdriver import Chrome
import time
from urllib.request import urlretrieve
import os

def crawler(url):

    dv.get(url)
    title = url.split("/")[6].split(".")[0]
    dirname = title + "/"
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    number = 1
    a = 0
    while number <= 50:

        c = dv.find_elements_by_class_name("item-link")

        product_name = dv.find_elements_by_class_name("item-heading")[a].text
        product_price = dv.find_elements_by_class_name("item-price")[a].text.split("$")[-1]

        c[a].click()
        time.sleep(1)

        try:
            ps = dv.find_elements_by_class_name("product-detail-thumbnail-image")

            url_2 = ps[-2].get_attribute("src")
            urlretrieve(url_2, dirname + f"第{number}件" + product_name + ".jpg")
            print(f"{title}的 第{a + 1}件 {product_name} 的大圖下載完了")

            url_1 = ps[-1].get_attribute("src")
            urlretrieve(url_1, dirname + f"第{number}件" + product_name + product_price + ".jpg")
            print(f"{title}的 第{a + 1}件 {product_name} 的細部圖下載完了")

            number += 1

        except :
            print(f"{title}的 第{a + 1}件 {product_name} 大圖下載不下來跳過跳過跳過跳過")
        a += 1

        # 上一頁
        dv.back()
        time.sleep(1)

        # 重整頁面
        dv.refresh()
        time.sleep(1)

    print(f"找了{a}件衣服 只有{number - 1}件能用")

category = ["modern-classic", "divided", "logg", "basics"]
dv = Chrome("./chromedriver")

for c in category:
    url = f"https://www2.hm.com/zh_asia3/men/shop-by-concept/{c}.html?sort=stock&image-size=small&image=stillLife&offset=0&page-size=100"
    crawler(url)
