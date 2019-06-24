import ahpWeight
import pandas as pd
import topsisFunction
import dataDirection

# 原始数据
data = pd.DataFrame(
        {'人均专著': [0.1, 0.2, 0.4, 0.9, 1.2], '生师比': [5, 6, 7, 10, 2], '科研经费': [5000, 6000, 7000, 10000, 400],
         '逾期毕业率': [4.7, 5.6, 6.7, 2.3, 1.8]}, index=['院校' + i for i in list('ABCDE')])

# 同向化
data['生师比'] = dataDirection.dataDirection_3(data['生师比'], 5, 6, 2, 12)  # 师生比为区间型指标
data['逾期毕业率'] = dataDirection.dataDirection_1(data['逾期毕业率'])  # 逾期毕业率为极小型指标

# 输入权重，不输入则默认熵权法计算
weight = [0.2, 0.3, 0.4, 0.1]

# 或者使用AHP方法计算权重
A = [[1, 4, 2, 8, 2], [1 / 4, 1, 1 / 2, 2, 1 / 2], [1 / 2, 2, 1, 4, 1], [1 / 8, 1 / 2, 1 / 4, 1, 1 / 4],
     [1 / 2, 2, 1, 4, 1]]  # 专家打分矩阵
b = ahpWeight.ahp(A)

# TOPSIS综合排序
result = topsisFunction.topsis(data, weight)
