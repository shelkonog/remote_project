
def ins(*arg):
    res = []
    for i in arg[0]:
        if i in res: continue
        for other in arg[1:]:
            if i not in other: break
        else:
            res.append(i)
    return res
def union(*arg):
    res = []
    for uniq in arg:
        for x in uniq:
            if not x in res:
                res.append(x)
    return res

