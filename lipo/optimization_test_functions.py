#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: David J. Elkind
# Creation date: 2018-02-17 (year-month-day)

"""
"""

from __future__ import division

import numpy as np


def gramacy_lee_2012(x):
  """
  A standard 1-dimensional global optimization test function with many local minima.
  f(x) = sin(10 pi x) / (2 x) + (x - 1) ^ 4

  There is a global minimum at

  :param x: a float in [0.5, 2.5]
  :return: f(x)
  """
  if not (0.5 < x < 2.5):
    raise ValueError("Provided values of x not in bounds for this objective function. See documentation.")
  y = np.sin(10.0 * np.pi * x)
  y /= 2 * x
  y += np.power(x - 1.0, 4.0)
  return y


def branin(x):
  """
  A standard 2-dimensional global optimization test function with a long, shallow valley.
  f(x) = (x2 - 4 * 5.1 (x1 / pi)^2 + 5 x1 / pi - 6)^2 + 10 (1 - (8 pi)^-1 ) cos (x1) + 10
  (The general form doesn't specify coefficients.)

  There is a global minimum at

  :param x: tuple such that
    x[0] in [-5, 10]
    x[1] in [0, 15]
  :return: f(x)
  """
  x1 = x[0]
  x2 = x[1]
  if not (-5.0 < x1 < 10.0) or not (0.0 < x2 < 15.0):
    raise ValueError("Provided values of x not in bounds for this objective function. See documentation.")
  fx = 10
  fx += np.power(x2 - 5.1 / 4 * np.power(x1 / np.pi, 2.0) + 5 / np.pi * x1 - 6, 2.0)
  fx += 10 * (1 - np.reciprocal(8 * np.pi)) * np.cos(x1)
  return fx


def goldstein_price(x):
  """
  A standard 2-dimensional global optimization test function with a large, nearly-flat region.

  There is a global minimum at (0, -1).
  :param x:
  :return:
  """
  if not all([(-2 < x[i] < 2) for i in [0, 1]]):
    raise ValueError("Provided value of x not in bounds for this objective function. See documentation.")
  x1 = x[0]
  x2 = x[1]
  factor1 = np.power(x1 + x2 + 1, 2.0)
  factor1 *= 19 - 14 * x1 + 3 * x1 * x1 - 14 * x2 + 6 * x1 * x2 + 3 * x2 * x2
  factor1 += 1
  factor2 = np.power(2 * x1 - 3 * x2, 2.0)
  factor2 *= 18 - 32 * x1 + 12 * x1 * x1 + 48 * x2 - 36 * x1 * x2 + 27 * x2 * x2
  factor2 += 30
  return factor1 * factor1
