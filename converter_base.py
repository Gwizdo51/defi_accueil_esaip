# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:24:08 2023

@author: ndeye
"""

import math
from measurement.measures import Speed, Distance, Weight
from typing import Optional


class Currency:

    def __init__(
        self,
        eur: Optional[float] = None,
        fr: Optional[float] = None,
        usd: Optional[float] = None,
        gbp: Optional[float] = None,
        mxn: Optional[float] = None,
        jpy: Optional[float] = None
    ):

        self.dict_units = {
            "eur": eur,
            "fr": fr,
            "usd": usd,
            "gbp": gbp,
            "mxn": mxn,
            "jpy": jpy
        }

        for unit in self.dict_units.keys():
            if self.dict_units[unit] is not None:
                self.init_val = self.dict_units[unit]
                self.init_unit = unit

 
    @property
    def eur(self):

        match self.init_unit:
            case "eur":
                return self.init_val
            case "fr":
                return self.init_val * 6.55957
            case "usd":
                return self.init_val * 0.93084
            case "gbp":
                return self.init_val * 1.1697
            case "mxn":
                return self.init_val / 18.84976302
            case "jpy":
                return self.init_val * 0.006325293888


    @property
    def fr(self):

         match self.init_unit:
            case "eur":
                return self.init_val  / 6.55957
            case "fr":
                return self.init.val
            case "usd":
                return self.init_val * 6.1059379
            case "gbp":
                return self.init_val * 7.66549
            case "mxn":
                return self.init_val / 2.8382056613560
            case "jpy":
                return self.init_val * 0.041421886840

    @property
    def usd(self):

         match self.init_unit:
            case "eur":
                return self.init_val / 0.93084
            case "fr":
                return self.init_val / 6.1059379
            case "usd":
                return self.init_val * 0.93084
            case "gbp":
                return self.init_val * 1.25539
            case "mxn":
                return self.init_val / 17.5479
            case "jpy":
                return self.init_val * 0.006778788

    @property
    def gbp(self):

         match self.init_unit:
            case "eur":
                return self.init_val / 1.1697
            case "fr":
                return self.init_val / 7.66549
            case "usd":
                return self.init_val / 1.25539
            case "gbp":
                return self.init_val
            case "mxn":
                return self.init_val / 21.99486
            case "jpy":
                return self.init_val * 0.005423217426

    @property
    def mxn(self):

         match self.init_unit:
            case "eur":
                return self.init_val * 18.84976302
            case "fr":
                return self.init_val * 2.8382056613560
            case "usd":
                return self.init_val * 17.5479
            case "gbp":
                return self.init_val * 21.99486
            case "mxn":
                return self.init_val
            case "jpy":
                return self.init_val * 0.1195615647

    @property
    def jpy(self):

         match self.init_unit:
            case "eur":
                return self.init_val / 0.006325293888
            case "fr":
                return self.init_val / 0.041421886840
            case "usd":
                return self.init_val / 0.006778788
            case "gbp":
                return self.init_val / 0.005423217426
            case "mxn":
                return self.init_val / 0.1195615647
            case "jpy":
                return self.init_val
            

class Slope:

    def __init__(self, rate: Optional[float] = None, angle: Optional[float] = None):

        self.dict_units = {
            "rate": rate,
            "angle": angle
        }

        for unit in self.dict_units.keys():
            if self.dict_units[unit] is not None:
                self.init_val = self.dict_units[unit]
                self.init_unit = unit

    @property
    def rate(self):
        if self.init_unit == "rate":
            return self.init_val
        elif self.init_unit == "angle":
            return 100 * math.tan(math.pi * self.init_val / 180)

    @property
    def angle(self):
        if self.init_unit == "rate":
            return (180 / math.pi) * math.atan(self.init_val / 100)
        elif self.init_unit == "angle":
            return self.init_val


def convert(value: float, unit_start: str, unit_end: str) -> float:

    dict_unit = {
        "km": Distance(km=value),
        "m": Distance(m=value),
        "mi": Distance(mi=value),
        "ft": Distance(ft=value),
        "inch": Distance(inch=value),
        "yd": Distance(yd=value),
        "kg": Weight(kg=value),
        "lb": Weight(lb=value),
        "km__hr": Speed(km__hr=value),
        "m__sec": Speed(m__sec=value),
        "eur": Currency(eur=value),
        "fr": Currency(fr=value),
        "usd": Currency(usd=value),
        "gbp": Currency(gbp=value),
        "mxn": Currency(mxn=value),
        "rate": Slope(rate=value),
        "angle": Slope(angle=value)
    }

    measure_obj = dict_unit[unit_start]
    return measure_obj.__getattribute__(unit_end)