
from .aggregateevents import aggregateevents
from .generatormatrix import generatormatrix
import scipy.linalg


def ctmc(data, numstates, transintv=1.0, toltime=1e-8):
    """ Continous Time Markov Chain (with automatic error correction)"""
    transcount, statetime = aggregateevents(data, numstates, toltime)
    genmat = generatormatrix(transcount, statetime, toltime)
    transmat = scipy.linalg.expm(genmat * transintv)
    return transmat, genmat, transcount, statetime
