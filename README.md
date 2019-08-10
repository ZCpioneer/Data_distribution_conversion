# 一维数据转化成以下标区分的多维矩阵
原本是因为在学习tensorflow的时候，看模板里面对结果集数据，是强制以[0,0,1,0]来表示是第三种结果。<br>
但是，在用网上的数据集的时候，数据集不是区分好的，是[1,2,0,1]<br>
我需要使用[[0,1,0][0,0,1][1,0,1][0,1,0]]<br>
所以，我就写了这个脚本函数，来将一维数据转化成以下标区分的多维矩阵
