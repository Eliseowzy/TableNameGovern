## 表名治理

### todo list

* [x] 利用sample数据，设计有限自动机
* [ ] 理解业务、数据、形式化描述命名规则
* [ ] 和业务、数分对接，确保词根、语法的一致性
* [x] 构造有限自动机（原型）
* [ ] 化简有限自动机（原型）
* [ ] 正则表达式
  + [ ] 日期：理解日期命名规范
  + [ ] 和业务数分对接，设计、调整正规式
* [ ] 开发
  + [ ] 实现有限自动机（原型）
    + [ ] 发现的问题：
      + 对于不同输入的处理，鲁棒性较差
      + 不够灵活、不能扩展
      + 对于不同日期格式的处理不够精细
  + [ ] 实现networkx + 配置文件，构造图结构的有限自动机
  + [ ] 检测错误位置
  + [ ] 动态修改错误
  + [ ] 扩展性和灵活性
    + [ ] 扩展性：配置文件+源代码，后期开辟新的需求、业务等，需要建表，可以将新的命名规范添加到配置文件当中，源代码无需修改
    + [ ] 灵活性：对配置文件进行curd即可修改规则。
  + [ ] 鲁棒性
    + [ ] 输入的字符串：字母数字下划线、空串如何处理： `r'[a-zA-Z0-9][a-zA-Z0-9_]+[a-zA-Z0-9]$'`
    + [ ] 常见的日期模式（字段、表名都可用）
        ```python
        import re
        pattern_1 = r'[a|b]*[1-9]+[0-9]*[y|m|w|d]'  # x年、月、日以后       （前）
        pattern_2 = r'[c|f|hf][y|q|m|w|d]'  #自然年、财年
        pattern_3 = r'[s|y|q|m|w|f]td'  #历史、年、季度、月、周、财年截     止到当前日
        pattern_4 = r'[1-9]+[h|m|s]'  #最近x小时、分钟、秒
        pattern_5 = r'[y|q|m|f]t[d]'  #年、季度、月、财年截止到当日
        pattern_6 = r'dt[Nm|h|r]'  #零点截止到当前分钟、小时、当前时刻
        pattern_7 = r'[h|m]tr'  #小时、分钟截止到当前
        pattern_8 = r'at[d|h|r]'  # 活动开始截止到当前天、小时、当前时间
        pattern_9 = r'[rw|rm|ry|qh]'  #上周四到本周三（）报表周、一刻钟
        pattern_10 = r'[p|f]?[1-9][0-9]*t[1-9][0-9]*[d|w|m|y]'# 日期        f1t10y未来1到10年
        pattern_11 = r'[p|f]*[1-9]+[0-9]*[d|w|m|y]' #f10d未来10天
        # 模式拼接
        pattern = re.compile(r'{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.       format(
            pattern_1, pattern_2, pattern_3, pattern_4, pattern_5,      pattern_6,pattern_7, pattern_8, pattern_9,pattern_10,       pattern_11))
        # 测试用例
        cases = [
            '1d', '3d', '1w', '2w', '3m', '6m', 'b6m', 'a6m', 'cw',         'cm', 'cq', 'fy',
            'hfy', 'std', 'ytd', 'qtd', 'mtd', 'wtd', 'ftd', '1h',      '2w', 'dtNm', 'dth',
            'dtr', 'htr', 'mtr', 'atd', 'ath', 'atr', 'p1w', 'p1m',         'rw', 'qh'
        ]
        
        # 需要观察已经匹配的用例和所有用例的数量是否一样多，输出不匹配的用例
        is_match = [] # 存储已经匹配的用例
        print(len(cases))
        for case in cases:
            if not pattern.match(case):
                print(case)
            else:
                is_match.append(case)
        print(len(is_match))

                ```