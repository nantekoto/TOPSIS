# 将各类型指标转换为极大型指标


# 转换极小型指标，offset为指标可能取值的最大值
def dataDirection_1(datas, offset=0):
    def normalization(data):
        return 1 / (data + offset)

    return list(map(normalization, datas))


# 转换中间型指标，min和max为指标可能取值的最小/最大值
def dataDirection_2(datas, x_min, x_max):
    def normalization(data):
        if data <= x_min or data >= x_max:
            return 0
        elif x_min < data < (x_min + x_max) / 2:
            return 2 * (data - x_min) / (x_max - x_min)
        elif x_max > data >= (x_min + x_max) / 2:
            return 2 * (x_max - data) / (x_max - x_min)

    return list(map(normalization, datas))


# 转换区间型指标，min和max为指标最佳稳定区间，minimum和maximum为最大容忍区间
def dataDirection_3(datas, x_min, x_max, x_minimum, x_maximum):
    def normalization(data):
        if x_min <= data <= x_max:
            return 1
        elif data <= x_minimum or data >= x_maximum:
            return 0
        elif x_max < data < x_maximum:
            return 1 - (data - x_max) / (x_maximum - x_max)
        elif x_min > data > x_minimum:
            return 1 - (x_min - data) / (x_min - x_minimum)

    return list(map(normalization, datas))
