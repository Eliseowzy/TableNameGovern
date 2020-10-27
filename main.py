from utils.check import TableNameCheck
from utils.replace_table_name import replace_table_name


if __name__ == '__main__':
    print('请输入表名: (输入exit退出程序)')
    while True:
        table_name = input()
        if table_name == 'exit':
            break
        tool = TableNameCheck(table_name)
        tool.check()
        while not tool.is_correct()[0]:
            print('当前表名为: ' + table_name)
            if tool.is_correct()[2] == 1:
                print('请输入你想替换的词: ')
                word = input().strip('\n')
                table_name = replace_table_name(table_name, tool.is_correct()[1], word)
                tool = TableNameCheck(table_name)
                tool.check()
            if tool.is_correct()[2] == 2:
                print('请输入你想添加的词: ')
                word = input().strip('\n')
                table_name = table_name.strip('_') + '_' + word
                tool = TableNameCheck(table_name)
                tool.check()