import requests
import json
import numpy as np
from datetime import datetime


def find(arr, T):
    i = 0
    while i < len(T):
        if T[i][0] == arr:
            return (T[i][1][1:-1])
        else:
            i = i + 1


def avions():
    cle = 'TO FILL IN'
    code = 'LFPG'
    link = 'https://airlabs.co/api/v9/schedules?dep_icao=' + code + '&api_key=' + cle
    tab = np.loadtxt('airports_codes.txt',
                     skiprows=1,
                     dtype=str,
                     usecols=(0, 1),
                     delimiter='	')
    vf = []
    r = requests.get(link)
    re = r.json()
    rep = re['response']
    for j in range(len(rep)):
        nb = rep[j]['flight_iata']
        gt = rep[j]['dep_gate']
        pt = rep[j]['aircraft_icao']
        arr = rep[j]['arr_iata']
        retard = rep[j]['delayed']
        dttime = rep[j]['dep_time']
        if pt != None and gt != None:
            vf.append([arr, nb, dttime[11:].replace(':','&'), retard, gt, pt])
        else:
            pass
    vf = vf[0:10]
    normaliser(vf)
    for i in range(len(vf)):
        vf[i].insert(2,find(vf[i][0],tab).strip())
        vf[i].pop(0)
    return vf


def normaliser(c):
    for j in range(len(c)):
        if c[j][3] == None: c[j][3] = 'OT' """on time"""
        else: c[j][3] = str(c[j][3])