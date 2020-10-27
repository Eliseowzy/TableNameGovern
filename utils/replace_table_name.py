def replace_table_name(row_string, index, word):
    name_list = row_string.strip('\n').strip('\t').strip('_').split('_')
    name_list[index] = word
    res = ''
    for i in name_list:
        res += i
        res += '_'
    res = res.strip('_')
    return res
