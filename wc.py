import requests
import csv
import jieba
from lxml import etree
from wordcloud import WordCloud


for page in range(0,226,25):
    url = 'https://movie.douban.com/subject/34779692/comments?start=%d&limit=20&status=P&sort=new_score'%page
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
    response = requests.get(url=url,headers=headers).content.decode('utf-8')
    soup = etree.HTML(response)
    paqu = soup.xpath('//p[@class=" comment-content"]/span[@class="short"]/text()')
    with open('豆瓣.csv',mode='a',encoding='utf-8',newline="") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(paqu)

text = open(r'.\豆瓣.csv',encoding = 'utf_8').read()

cut_text = jieba.cut(text)
result = ' '.join(cut_text)


color_mask = numpy.array(Image.open('p.png'))

wc = WordCloud(
    mask=color_mask,
    font_path = r'.\simhei.ttf',
    background_color = 'white',
    width = 500,
    height = 350,
    max_font_size = 100,
    min_font_size = 10,
)
wc.generate(result)
wc.to_file(r'.\wordcloud.png')


