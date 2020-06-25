#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# Models used for ADC and SD analysis
class ModelBrownian:
    """Model for free, unrestricted diffusion.
    
    Parameters
    ----------
    R: float
        Point scanning across the field of view.
    dt: float
        Uniform time step size.
    """
    lower = [0.0, 0.0]
    upper = np.inf
    initial = [0.5e-12, 2.0e-9]
    def __init__(self):
        self.R = 0.0
        self.dt = 0.0

    def __call__(self, t, D, delta):
        return D + delta**2 / (2*t*(1-2*self.R*self.dt/t))

class ModelConfined:
    """Model for confined diffusion.
    
    Parameters
    ----------
    R: float
        Point scanning across the field of view.
    dt: float
        Uniform time step size.
    """
    lower = [0.0, 0.0, 0.0]
    upper = np.inf
    initial = [0.5e-12, 2.0e-9, 1.0e-3]
    def __init__(self):
        self.R = 0.0
        self.dt = 0.0

    def __call__(self, t, D_micro, delta, tau):
        return D_micro * (tau/t) * (1 - np.exp(-t / tau)) + \
            delta ** 2 / (2 * t * (1 - 2 * self.R * self.dt / t))

class ModelHop:
    """Model for hop diffusion.
    
    Parameters
    ----------
    R: float
        Point scanning across the field of view.
    dt: float
        Uniform time step size.
    """
    lower = [0.0, 0.0, 0.0, 0.0]
    upper = np.inf
    initial = [0.5e-12, 0.5e-12, 2.0e-9, 1.0e-3]
    def __init__(self):
        self.R = 0.0
        self.dt = 0.0

    def __call__(self, t, D_macro, D_micro, delta, tau):
        return D_macro + \
            D_micro * (tau/t) * (1 - np.exp(-t / tau)) + \
            delta ** 2 / (2 * t * (1 - 2 * self.R * self.dt / t))

class ModelImmobile:
    """Model for immobile diffusion.

    Parameters
    ----------
    R: float
        Point scanning across the field of view.
    dt: float
        Uniform time step size.
    """
    upper = [np.inf]
    lower = [0.0]
    initial = [0.5e-12]
    def __init__(self):
        self.R = 0.0
        self.dt = 0.0

    def __call__(self, t, delta):
        return delta**2 / (2*t*(1-2*self.R*self.dt/t))

class ModelHopModified:
    """Model for hop diffusion.
    
    Parameters
    ----------
    R: float
        Point scanning across the field of view.
    dt: float
        Uniform time step size.
    """
    lower = [0.0, 0.0, 0.0, 0.0]
    upper = np.inf
    initial = [0.5e-12, 0.5e-12, 0.0, 1.0e-3]
    def __init__(self):
        self.R = 0.0
        self.dt = 0.0

    def __call__(self, t, D_macro, D_micro, alpha, tau):
        return alpha * D_macro + \
            (1.0 - alpha) * D_micro * (1 - np.exp(-t/tau))


# Models used for MSD analysis
class ModelLinear:
    """Linear model for MSD analysis."""
    def __call__(self, t, D, delta2):
        return 4 * D * t + 2 * delta2

class ModelPower:
    """Generic power law model for MSD analysis."""
    def __call__(self, t, D, delta2, alpha):
        return 4 * D * t**alpha + 2 * delta2