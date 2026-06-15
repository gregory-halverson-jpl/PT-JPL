from typing import Union
import numpy as np
import rasters as rt
from rasters import Raster

BARREN_GREEN_CANOPY_VALUE = np.nan
# BARREN_GREEN_CANOPY_VALUE = 0

CLIP_FAPAR = False
CLIP_FIPAR = False

def calculate_green_canopy_fraction(
        fAPAR: Union[Raster, np.ndarray], 
        fIPAR: Union[Raster, np.ndarray],
        barren_green_canopy_value: float = BARREN_GREEN_CANOPY_VALUE,
        clip_fAPAR: bool = CLIP_FAPAR,
        clip_fIPAR: bool = CLIP_FIPAR) -> Union[Raster, np.ndarray]:
    """
    This function calculates the green-canopy fraction (fg) from the given fAPAR and fIPAR values.
    
    The green-canopy fraction is calculated as the ratio of the fraction of absorbed photosynthetically 
    active radiation (fAPAR) to the fraction of intercepted photosynthetically active radiation (fIPAR). 
    The result is clipped to the range [0, 1]. If fIPAR is zero, the result is set to NaN.

    Args:
        fAPAR (Union[Raster, np.ndarray]): The fraction of absorbed photosynthetically active radiation. 
            It can be a Raster object or a numpy ndarray.

        fIPAR (Union[Raster, np.ndarray]): The fraction of intercepted photosynthetically active radiation. 
            It can be a Raster object or a numpy ndarray.

    Returns:
        Union[Raster, np.ndarray]: The calculated green-canopy fraction. The return type matches the input type.
    """
    if clip_fAPAR:
        fAPAR = rt.clip(fAPAR, 0.0, 1.0)
    
    if clip_fIPAR:
        fIPAR = rt.clip(fIPAR, 0.0, 1.0)
    
    fg = rt.where(fIPAR > 0, np.clip(fAPAR / fIPAR, 0.0, 1.0), barren_green_canopy_value)
    
    return fg
