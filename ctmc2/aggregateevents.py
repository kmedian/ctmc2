
import scipy.sparse
import numpy as np
import warnings


def aggregateevents(data, numstates, toltime=1e-8):
    transcount = scipy.sparse.lil_matrix((numstates, numstates), dtype=int)
    statetime = np.zeros(numstates, dtype=float)

    for exid, example in enumerate(data):
        states = example[0]
        times = example[1]

        if len(np.unique(states)) < 2:
            warnings.warn(
                ("The example id={:d} has only 1 or no distinct "
                 "state and will be ignored. Please remove incomplete "
                 "examples from the dataset").format(exid))
        else:
            for i, s in enumerate(states):
                if times[i] < toltime:
                    warnings.warn(
                        ("The example id={:d} has a state that "
                         "have not been active for longer than "
                         "toltime.").format(exid))
                else:
                    statetime[s] += times[i]
                    if i:
                        if states[i - 1] == s:
                            warnings.warn(
                                ("The example id={:d} contains two entries "
                                 "for the same state in a row. Please  "
                                 "aggregate these obs.").format(exid))
                        else:
                            transcount[states[i - 1], s] += 1

    return transcount.toarray(), statetime
