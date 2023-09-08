
from data_define import record
import json
class filereader:

    def read_data(self)->list[record]:
        """每一条转换为record，将它们都封装在list里即可"""
        pass

class textfilereader(filereader):
    def __init__(self,path):
        self.path=path

    def read_data(self)->list[record]:
        f=open(self.path,"r",encoding="UTF-8")
        record_list=[]
        for line in f.readlines():
            line=line.strip()
            # print(line)
            data_list=line.split(",")
            rd=record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(rd)
        f.close()

        return record_list

class jsonfilereader(filereader):
    def __init__(self,path):
        self.path=path

    def read_data(self)->list[record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list = []
        for line in f.readlines():
            data_dict=json.loads(line)
            rd=record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(rd)
        f.close()
        return record_list

if __name__=='__main__':
    tfr=textfilereader("D:/2011年1月销售数据.txt")
    jfr=jsonfilereader("D:/2011年2月销售数据JSON.txt")

    list1=tfr.read_data()
    list2=jfr.read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)