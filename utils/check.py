import networkx as nx
from utils.read_graph import read_graph
import re


class TableNameCheck:
    def __init__(self, table_name):
        self.__index = None
        self.__start_node = None
        self.__table_name = table_name
        self.__keywords = None
        self.__error_type = None
        self.__graph = read_graph()
        self.__is_correct = self.__check_graph()


    def __get_key_words(self, row_string):
        return row_string.strip('\n').strip('\t').strip('_').split('_')


    def __check_if_stop(self, G, start_node):
        next_nodes = [i for i in G.neighbors(start_node)]
        for next_node in next_nodes:
            if 'STOP' in G.edges[start_node, next_node]['names']:
                return True
        return False


    def __check_regex(self, name, res):
        ll = re.findall(name.strip('REGEX'), res, flags=0)
        return len(ll) != 0


    # 字符串匹配的三种情况
    # 第一种 有一个字符子串完全没有匹配到 失败
    # 第二种 字符串没有匹配到图的终点 失败
    # 第三种 字符串完全匹配并走到终点 成功

    def __check_graph(self):
        row_string = self.__table_name
        G = self.__graph
        key_words = self.__get_key_words(row_string)
        self.__keywords = key_words
        start_node = 0
        index = 0
        if_find = False
        while index < len(key_words):
            if_find = False
            next_nodes = [i for i in G.neighbors(start_node)]
            for next_node in next_nodes:
                flag = 0
                for name in G.edges[start_node, next_node]['names']:
                    if key_words[index] == name or 'REGEX' in name and self.__check_regex(name, key_words[index]):
                        start_node = next_node
                        if_find = True
                        flag = 1
                        break
                if flag:
                    break
            if not if_find and index < len(key_words):
                self.__start_node = start_node
                self.__index = index
                return False
            index += 1
        if not self.__check_if_stop(G, start_node):
            self.__start_node = start_node
            return False
        return index == len(key_words) and if_find and self.__check_if_stop(G, start_node)

    def __get_neighbor_names(self,start_node):
        next_nodes = [i for i in self.__graph.neighbors(start_node)]
        res = []
        for next_node in next_nodes:
            for name in self.__graph.edges[start_node, next_node]['names']:
                res.append(name)
        return res


    def is_correct(self):
        return (self.__is_correct, self.__index, self.__error_type)

    def check(self):
        #第一种 有一个字符子串完全没有匹配到 失败
        if not self.__is_correct and self.__index and self.__start_node:
            self.__error_type = 1
            print('输入错误！您输入的第 {} 个单词: {} 不合法'.format(self.__index + 1, self.__keywords[self.__index]))
            print('该词可替换为: ')
            for name in self.__get_neighbor_names(self.__start_node):
                print(name)
            print('*' * 20)
                
        # 第二种 字符串没有匹配到图的终点 失败
        elif not self.__is_correct and self.__start_node:
            self.__error_type = 2
            print('输入错误！您输入的表名不完整，您还可以继续输入以下单词: ')
            for name in self.__get_neighbor_names(self.__start_node):
                print(name)
            print('*' * 20)
        
        else:
            print('当前的表名为：' + self.__table_name)
            print('匹配成功！')
            print('*' * 20)

