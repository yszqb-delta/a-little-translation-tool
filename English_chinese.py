import DrissionPage
import time

page = DrissionPage.ChromiumPage()
page.get("https://fanyi.youdao.com/index.html#/")
a = input()
page.ele('#js_fanyi_input').input(str(a))
ele = page.ele(".tgt color_text_1")
time.sleep(1)
result = ele.html[83:-8]
print(result)
