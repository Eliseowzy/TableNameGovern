def get_test_tablename():
    file = open('./data/test_tablename','r+')
    res = []
    for line in file:
        res.append(line.strip('\n').strip('\t'))
    return res