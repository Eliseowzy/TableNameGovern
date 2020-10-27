from utils.check import TableNameCheck
from utils.get_test_tablename import get_test_tablename


if __name__ == '__main__':
    tablename_list = get_test_tablename()
    for tablename in tablename_list:
        tool = TableNameCheck(tablename)
        tool.check()