
import numpy as np
import warnings


def generatormatrix(transcount, statetime, toltime=1e-8):
    # deep copy
    tmp = transcount.copy()

    # get matrix dimension
    n = tmp.shape[0]

    # reset diagonal elements to zero
    # same as "tmp[np.eye(n) == 1] = 0"
    for i in range(n):
        if tmp[i, i] != 0:
            tmp[i, i] = 0
            warnings.warn(
                ("transcount({0:d},{0:d})={1:d} is not Zero. "
                 "There is bug in the way you count transitions"
                 ).format(i, tmp[i, i]))

    # subtract the row sum from the diagonal element
    # same as "tmp -= np.diag(np.sum(tmp, axis=1))"
    rowsum = np.sum(tmp, axis=1)
    for i in range(n):
        tmp[i, i] = -rowsum[i]

    # divide transitions counts by the state idle times
    genmat = np.zeros(shape=(n, n), dtype=float)
    for i in range(n):
        if statetime[i] >= toltime:
            genmat[i, :] = tmp[i, :] / statetime[i]
        else:
            warnings.warn(
                ("The state i={:d} has a cumulated state time "
                 "of less than toltime").format(i))

    # done
    return genmat
