
"""OpenVRD - Stormwater hydrology tools."""

import math


def rational_method(area_m2, coefficient, rainfall_mm_h):
    """Calculate peak stormwater discharge in L/s."""

    if not all(math.isfinite(v) for v in
               (area_m2, coefficient, rainfall_mm_h)):
        raise ValueError("Inputs must be finite.")

    if area_m2 <= 0:
        raise ValueError("Area must be positive.")

    if not 0 <= coefficient <= 1:
        raise ValueError("Invalid runoff coefficient.")

    if rainfall_mm_h < 0:
        raise ValueError("Invalid rainfall intensity.")

    return area_m2 * coefficient * rainfall_mm_h / 3600
