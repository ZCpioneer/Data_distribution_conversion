import numpy as np
"""
    目的是分离数据，将一列中的多种数据分离成多列的位置区分数据
    传入一维数据，能转化成以列位置作为数据区分的多维数据
    作者：zc
    时间：2019/8/10
"""


def separation(labels):
    """
    目的是分离数据，将一列中的多种数据分离成多列的位置区分数据
    :param labels: 标签数据
    :return: 拆分好的新数组
    """
    labels_index, kind = separation_kind(labels)
    new_labels = []
    resultArray = getResultArray(len(kind))
    for i in labels_index:
        new_labels.append(resultArray[i])
    return np.asarray(new_labels)


def separation_kind(labels):
    """
    传入标签数据，筛选标签信息
    :param labels: 标签数据
    :return: 标签对应的目标数组的下标数组，种类数组
    """
    kind = []
    labels_index = []
    for i in labels:
        if kind_exist(kind, i):
            pass
        else:
            kind.append(i)
        labels_index.append(kind.index(i))
    return labels_index, kind


def kind_exist(kindList, label):
    """
    通过遍历数组进行扫描，判断当前标签是否存在
    :param kindList: 种类数组
    :param label:
    :return:
    """
    for i in kindList:
        if i == label:
            return True
    return False


def getResultArray(kindLength):
    """
    生成结果数组，就是有几个种类，就生成几种对应的目标数组
    例：有4个种类，生成[[1,0,0,0][0,1,0,0][0,0,1,0][0,0,0,1]]
    :param kindLength: 种类数量
    :return: 目标数组
    """
    answer = []
    for i in range(kindLength):
        newList = []
        for j in range(kindLength):
            if i == j:
                newList.append(1)
            else:
                newList.append(0)
        answer.append(newList)
    return answer
