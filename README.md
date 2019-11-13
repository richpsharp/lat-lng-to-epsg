# lat-lng-to-epsg
Get EPSG code given a set of lat/lng coordinates. License is 3-Clause BSD and
free to use for all purposes including commercial.

Usage:

```
import lat_lng_to_epsg

>>> lat_lng_to_epsg.lat_lng_to_epsg(-70, 40)
32737
>>> lat_lng_to_epsg.lat_lng_to_epsg(40, 179)
32660
>>> lat_lng_to_epsg.lat_lng_to_epsg(40, 180)
32601
>>> lat_lng_to_epsg.lat_lng_to_epsg(40, -180)
32601
```
