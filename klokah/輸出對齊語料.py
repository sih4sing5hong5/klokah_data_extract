from klokah.補充教材句型篇解析 import 補充教材句型篇解析
from klokah.九階教材解析 import 九階教材解析

方言編號 = 2

上一個標題 = None
for 一筆資料 in 九階教材解析().解析一個方言檔案(方言編號):
    族語標題, 華語標題 = 一筆資料['title'], 一筆資料['titleCh']
    if 上一個標題 != (族語標題, 華語標題):
        print(' '.join(族語標題.split()), 華語標題)
        上一個標題 = (族語標題, 華語標題)
    族語, 華語 = 一筆資料['text'], 一筆資料['chinese']
    print(' '.join(族語.split()), 華語)

for 一筆資料 in 補充教材句型篇解析().解析一個方言檔案(方言編號):
    for 族語, 華語 in 一筆資料['資料']:
        print(' '.join(族語.split()), 華語)
