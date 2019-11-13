"""Simple calculation to find most UTM zones given (lat/lng) coordinate."""
import math


def lat_lng_to_epsg(lat_coord, lng_coord):
    """Calculate the EPSG code of the given WGS84 (lat/lng) coordinate.

    Parameters:
        lat_coord (float): number between -90 and 90 indicating latitute
            coordinate.
        lng_coord (float): number between -180 to 180 indicating longitude
            coordinate.

    Returns:
        EPSG code of the UTM zone that contains the given point.

    """
    utm_code = (math.floor((lng_coord + 180)/6) % 60) + 1
    lat_code = 6 if lat_coord > 0 else 7
    epsg_code = int('32%d%02d' % (lat_code, utm_code))
    return epsg_code
