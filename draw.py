import pandas as pd
import matplotlib.pyplot as plt

def getData():
    '''
    主要包括3大功能：
    ①从原始excel表格中，获取数据，做最小生成树
    ②对最小生成树剪枝，剪枝条件为3/4位。得到out矩阵，在out矩阵中，-1即代表对应的两个城市没有连接
    ③根据out生成图，使用networkx库进行节点属性的计算。最后把结果放到excel中。
    in：
        原始excel表格
    out：
        每个年份：含各个节点的3个属性的excel，以及1张简易的剪枝后的图。（3个属性：节点的度（归一化），近性中心度（主中心城市），介性中心度（节点枢纽城市））
    :return:
    '''

    # 导入数据
    file_path = r"C:\Users\420\Desktop\J1939sheet6.xlsx"
    # df = pd.read_excel(file_path,sheet_name='工作表6')  # 选取工作表
    df = pd.read_excel(file_path,usecols=["帧ID","数据2","数据3"])
    ## df相关操作
    # print(df.iat[1,0])   # 定位df获取数据
    # print(df.shape[0])  # df的总行数
    # print(type(df.iat[0,0]))  # 判断数据类型
    # a = hex(int(df.iat[0,0],16))  # 把字符'a'转换成16进制0xa
    # df2 = df[df.帧ID == '0x18febf0b']  # df的筛选，通过字段。同样存在序号不连续问题
    df2 = df.loc[df['帧ID'] == '0x18fef100'].reset_index(drop=True)   # 通过.reset_index()来重置序号，这时候会在第一列处多一列，这一列是原来的index的内容。若不要这列的话改为.reset_index(drop=True)
    v =[]
    for i in range(df2.shape[0]):
        md = (int(str(df2.iat[i,2]),16) * 256 + int(str(df2.iat[i,1]),16)) / 256
        v.append(md)
    df3 =pd.DataFrame(v)
    df3.name='速度'
    df4 = pd.concat((df2,df3), axis=1)
    df4.to_excel(r"C:\Users\420\Desktop\J1939out3.xlsx")


    # plt绘图
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title('速度')
    plt.ylabel('km/h')
    plt.plot(v)
    plt.show()


if __name__ == '__main__':
    getData()
