"""
Helper functions for the seagen project.

Created by: Josh Borrow (joshua.borrow@durham.ac.uk)
"""

import numpy as np

from typing import Tuple


class InvalidCoordinate(Exception):
    pass


def check_valid_polar(r: np.ndarray, theta: np.ndarray, phi: np.ndarray) -> bool:
    """
    Check if these are valid polar co-ordinates; i.e.

        + r \in [0, inf)
        + theta \in [0, 2pi)
        + phi \in [0, pi]

    If not, it raises an InvalidCoordinate exception.
    """
    
    if not ((min(r) >= 0.) and (np.isfinite(r).all())):
        raise InvalidCoordinate(
            "Your r values are not bounded between 0 and infinity"
        )

    if not ((min(theta) >= 0.) and (max(theta) < 2 * np.pi)):
        raise InvalidCoordinate(
            "Your theta values are not bounded between 0 and 2 pi"
        )
    
    if not ((min(phi) >= 0.) and (max(phi) <= np.pi)):
        raise InvalidCoordinate(
            "Your phi values are not bounded between 0 and pi"
        )

    return True


def polar_to_cartesian(
        r: float,
        theta:float,
        phi: float
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Converts spherical polar to cartesian, and checks that they are valid
    using check_valid_polar.
    """

    if check_valid_polar(r, theta, phi):
        x = r * np.cos(theta) * np.sin(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(phi)

        return x, y, z
    
    else:
        return None, None, None

