from file_define import *
from data_define import *
from pyecharts.charts import *
from pyecharts.options import *
from pyecharts.globals import *

tfr=textfilereader("D:/2011年1月销售数据.txt")
jfr=jsonfilereader("D:/2011年2月销售数据JSON.txt")

list1:list[record]=tfr.read_data()
list2:list[record]=jfr.read_data()
all_data=list1+list2

data_dict={}
for rd in all_data:
    if rd.date in data_dict.keys():
        data_dict[rd.date]+=rd.money
    else:
        data_dict[rd.date]=rd.money

print(data_dict)
# 进行可视化开发

bar=Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("每日销售额.html")