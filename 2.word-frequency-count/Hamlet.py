#文本读取函数
def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt

hamletTxt = getText()
words  = hamletTxt.split() #返回一个列表
counts = {}

#使用字典计数，如果字典中没有对应的key则创建一个
for word in words:			
    counts[word] = counts.get(word,0) + 1
    
items = list(counts.items()) #把字典转化成列表
items.sort(key=lambda x:x[1], reverse=True) #把列表中的value由大到小排序

#打印出现次数最多的前10个词
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))