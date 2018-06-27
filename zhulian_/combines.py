#coding:utf-8
#python3.6

import pandas as pd
import zhulian_.zl_python as usg
import zhulian_.single_p as ltg

List = []
for i in range(1,10):

    url0 = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=653&kw=python&sm=0&p=' + str(i)


    # url0 = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=538&kw=python&sm=0&sg=bfa5343e35474abeb0533325e048b588&p=1'



    urls = usg.urlfs(url0)



    for url in urls:

        try:
            soup = ltg.soup_g(url)
        except:continue

        try:
            list_g = ltg.soup_excel(soup)
        except:continue
        if list_g == []:
            pass
        else:

            List = List + [list_g]

df = pd.DataFrame(List,columns=['web','job','职位月薪','工作地点','工作性质','工作经验','最低学历','职位类别','公司规模','公司地址'])
print(df)

writer = pd.ExcelWriter(r'G:\Crawlers/hangzhou.xlsx')
df.to_excel(writer,'sheet1',index=False)
writer.save()


