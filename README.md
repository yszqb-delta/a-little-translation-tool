# a-little-translation-tools
一个基于DrissionPage的翻译工具
A DrissionPage-based translation tool


中文:    
  Translation Test.py是一个测试用的程序。其原理是使用DrissionPage打开有道翻译的网页(https://fanyi.youdao.com/index.html#/) ，找到id为"js_fanyi_input"的div并输入要翻译的文本(尽量是单词之类的短语)，等到翻译之后，再找到class为"tgt color_text_1"的span并将信息通过语法糖(也就是常用的字符分割)提取出来。    
  注意:    
    电脑需要下载Google浏览器，并有对应的chromedriver.exe才可运行。如果想要切换输入、输出的语言，请先行打开浏览器设置后，再运行该程序。


English:    
  "Translation Test.py"is a testing program.The principle is to use DrissionPage to open the web page of Youdao Translation(https://fanyi.youdao.com/index.html#/),find the div with the ID "js_fanyi_input" and enter the text you want to translate.After the translation, find the span with class "tgt color_text_1" and extract the information through syntactic sugar (i.e., commonly used character segmentation).    
  Attention!!!:    
    The computer needs to download Google Chrome and have the corresponding "chromedriver.exe" to run.If you want to switch the input and output languages, please open your browser settings before running the program.
