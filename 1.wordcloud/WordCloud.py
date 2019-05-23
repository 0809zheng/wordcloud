import jieba  #jieba库用于中文分词
import wordcloud  #wordcloud库用于制作词云
from scipy.misc import imread

mask = imread("chinamap.jpg")  #引入背景图片

f = open("政府工作报告.txt", "r")  #打开文件
t = f.read()  #读入文件内容
f.close()  #关闭文件

ls = jieba.lcut(t)  #分词，返回一个列表
txt = " ".join(ls)  #转换成空格分隔的字符串

#设置词云
w = wordcloud.WordCloud(
        width = 1000, height = 700, #设置宽度和高度
        background_color = "white",  #设置背景颜色
        font_path = "msyh.ttc", #指定字体
        mask = mask #设置背景图片
        )

w.generate(txt) #生成词云
w.to_file("wordcloud1.png") #保存词云图片
