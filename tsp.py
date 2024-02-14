# Die Aufgabe besteht darin, eine Reihenfolge für den Besuch 
# mehrerer Orte so zu wählen, dass keine Station außer der ersten mehr
# als einmal besucht wird, die gesamte Reisestrecke des
# Handlungsreisenden möglichst kurz und die erste Station
# gleich der letzten Station ist.
#
# https://de.wikipedia.org/wiki/Problem_des_Handlungsreisenden

from itertools import permutations
import math

def berechne_kuerzeste_route(punkte):
    kuerzeste_route = None
    kuerzeste_entfernung = float('inf')

    for route in permutations(punkte):
        entfernung = 0
        for i in range(len(route)):
            if i == len(route)-1:
                entfernung += berechne_entfernung(route[i], route[0])
            else:
                entfernung += berechne_entfernung(route[i], route[i + 1])

        if entfernung < kuerzeste_entfernung:
            kuerzeste_entfernung = entfernung
            kuerzeste_route = route

    return kuerzeste_route

def berechne_entfernung(punkt1, punkt2):
    p1x = punkt1[0]
    p1y = punkt1[1]
    p2x = punkt2[0]
    p2y = punkt2[1]

    xEntf = p1x - p2x
    yEntf = p1y - p2y

    return math.sqrt(xEntf**2 + yEntf**2)
