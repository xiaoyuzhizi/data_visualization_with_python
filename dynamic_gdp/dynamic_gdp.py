from pyecharts.charts import *
from pyecharts.options import *
from pyecharts.globals import *
f=open("D:/1960-2019全球GDP数据.csv","r",encoding="GB2312")
data_lines=f.readlines()

f.close()
data_lines.pop(0)
data_dict={}
for line in data_lines:
    year=int(line.split(",")[0])
    country=line.split(",")[1]
    gdp=float(line.split(",")[2])
    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year]=[]
        data_dict[year].append([country,gdp])

# print(data_dict)

sorted_year=sorted(data_dict.keys())
# print(sorted_year)
timeline=Timeline({"theme": ThemeType.LIGHT})

for year in sorted_year:
    data_dict[year].sort(key=lambda x:x[1],reverse=True)
    year_data=data_dict[year][0:8]
    x_data=[]
    y_data=[]
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/100000000)

    bar=Bar()
    x_data.reverse()
    y_data.reverse()

    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8的GDP国家")
    )
    timeline.add(bar,str(year))
"""
    
        
print(type(year))
print(type(country))
print(type(gdp))
"""
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
timeline.render("dynamic_gdp.html")