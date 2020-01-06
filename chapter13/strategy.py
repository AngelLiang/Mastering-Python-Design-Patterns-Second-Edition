"""策略模式

在Python中，我们可以把函数看作是普通的变量，这就简化了策略模式的实现。

问题
假设我们要实现一个算法来检测在一个字符串中是否所有字符都是唯一的。
例如，如果输入字符串dream，算法应返回true，因为没有字符是重复的。
如果输入字符串pizza，算法应返回false，因为字母z出现了两次。

实现
对字符串进行排序并逐对比较所有字符。


优化
通常，我们想要使用的策略不应该由用户来选择。策略模式的要点是可以透明地
使用不同的算法。

优化提示
考虑在一个共用类（例如，AllUnique）中封装两个函数。这样，其他开发人员
只需要创建一个AllUnique类实例，并执行单个方法，例如test()。
"""

import time


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


SLOW = 3                        # in seconds
LIMIT = 5                       # in characters
WARNING = 'too bad, you picked the slow algorithm :('


def allUniqueSort(s):
    """
    假设这个算法伸缩性不好，对于不超过5个字符串才能工作良好。
    对于更长的字符串，通过插入一条 sleep 语句来模拟速度减缓。
    """
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    srtStr = sorted(s)
    for (c1, c2) in pairs(srtStr):
        if c1 == c2:
            return False
    return True


def allUniqueSet(s):
    """
    假设由于一些奇怪的原因，这个函数检测短字符串性能比 allUniqueSort() 更差。
    """
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)

    return True if len(set(s)) == len(s) else False


def allUnique(word, strategy):
    return strategy(word)


def main():

    WORD_IN_DESC = 'Insert word (type quit to exit)> '
    STRAT_IN_DESC = 'Choose strategy: [1] Use a set, [2] Sort and pair> '

    while True:
        word = None
        while not word:
            word = input(WORD_IN_DESC)

            if word == 'quit':
                print('bye')
                return

            strategy_picked = None
            # 策略映射
            strategies = {'1': allUniqueSet, '2': allUniqueSort}
            # 选择策略
            while strategy_picked not in strategies.keys():
                strategy_picked = input(STRAT_IN_DESC)

                try:
                    # 从策略映射中获取策略
                    strategy = strategies[strategy_picked]
                    # 执行策略
                    result = allUnique(word, strategy)
                    # 打印结果
                    print(f'allUnique({word}): {result}')
                except KeyError as err:
                    print(f'Incorrect option: {strategy_picked}')


if __name__ == "__main__":
    main()
