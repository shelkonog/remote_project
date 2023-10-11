def mymap(func1, *seq):
    return (func1(*arg) for arg in zip(*seq))
def myzip(*seq):
    minlen = min(len(S) for S in seq)
    return (tuple(S[i] for S in seq) for i in range(minlen))
def mymappad(*seq, pad = None):
    seq = [list(S) for S in seq]
    res = []
    while any(seq):
        res.append(tuple(S.pop(0) if S else pad for S in seq))
    return res
def myzip2( *seq):
    iters = list(map(iter, seq))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)
print(list(myzip2('abc', 'qwert')))
