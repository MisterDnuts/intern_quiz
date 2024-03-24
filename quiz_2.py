# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/24 14:33
# @Author : Atem
# @Email : atem.jetson@gmail.com
# @File : quiz_2
# @Project : intern_quiz
# @LastEdit : 2024/3/24


# 转义字典
num_dict = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
unit_dict = {'十': 10, '百': 100, '千': 1000}
# 测试用例
test_list = ["一百三十九", "九十一"]


def num_trans(cn_num: str):
    # 总值计数
    nums = 0
    # 数组下标定位
    count = 0
    while count < len(cn_num):
        if cn_num[count] in num_dict:
            try:
                # 下标未越界，后一位为单位（万以内）
                if cn_num[count + 1] in unit_dict:
                    nums = nums + (num_dict[cn_num[count]] * unit_dict[cn_num[count + 1]])
            # 下标越界，为个位数
            except IndexError:
                nums = nums + num_dict[cn_num[count]]
        count += 1
    # 反转数字
    return int(str(nums)[::-1])
    pass


if __name__ == '__main__':
    for t in test_list:
        print(num_trans(t))
