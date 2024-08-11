# LISM_NHI
 HI column density estimator for stars inside 100 pc

```
from astropy.coordinates import SkyCoord
import astropy.units as u
coord = SkyCoord(217.4289421*u.deg,-62.67949*u.deg,frame='icrs') # Proxima Centauri coordinates
dist = 1.3 # pc - distance to Proxima Centauri

from LISM_NHI import LISM_NHI
log10_NHI = LISM_NHI.main(coord, dist)
```
