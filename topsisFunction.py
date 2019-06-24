import pandas as pd
import numpy as np
import entropyWeight


def topsis(data, weight=None):
    # 归一化
    data = data / np.sqrt((data ** 2).sum())

    # 最优最劣方案
    Z = pd.DataFrame([data.min(), data.max()], index=['负理想解', '正理想解'])

    # 距离，默认使用熵权法
    weight = entropyWeight.entropyWeight(data) if weight is None else np.array(weight)
    Result = data.copy()
    Result['正距离'] = np.sqrt(((data - Z.loc['正理想解']) ** 2 * weight).sum(axis=1))
    Result['负距离'] = np.sqrt(((data - Z.loc['负理想解']) ** 2 * weight).sum(axis=1))

    # 综合得分指数
    Result['综合得分指数'] = Result['负距离'] / (Result['负距离'] + Result['正距离'])
    Result['排序'] = Result.rank(ascending=False)['综合得分指数']

    return Result, Z, weight
