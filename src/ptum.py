from __future__ import annotations
import numpy as np


class LatLon:
    def __init__(self, lat: float, lon: float) -> None:
        """_summary_

        Args:
            lat (float): _description_
            lon (float): _description_
        """
        self.r_earth: float = 6378.0  # in km
        self.lat = lat
        self.lon = lon

    def add_distance(self, delta_lat: float, delta_lon: float, unit="km") -> LatLon:
        """_summary_

        Args:
            delta_lat (float): _description_
            delta_lon (float): _description_
            unit (str, optional): _description_. Defaults to "km".

        Returns:
            LatLon: _description_
        """
        new_lat = self.lat + (
            delta_lat * self.convert_distance_units(unit) / self.r_earth
        ) * (180.0 / np.pi)
        new_lon = self.lon + (
            delta_lon * self.convert_distance_units(unit) / self.r_earth
        ) * (180.0 / np.pi) / np.cos(self.lat * np.pi / 180.0)
        return LatLon(new_lat, new_lon)

    @staticmethod
    def convert_distance_units(unit: str) -> float:
        """_summary_

        Args:
            unit (str): _description_

        Raises:
            ValueError: _description_

        Returns:
            float: _description_
        """
        match unit:
            case "m":
                return 1 / 1000.0
            case "km":
                return 1.0
            case "mi":
                return 1.60934
            case _:
                raise ValueError(
                    "We only used 'm' (meter), 'km' (kilometer) or 'mi' (miles), you"
                    f" gave the unit {unit}."
                )

    def to_tuple(self):
        return (self.lat, self.lon)

    def __str__(self):
        return f"Lat: {str(self.lat)}, Lon: {str(self.lon)}"

    def __repr__(self):
        return f"Lat: {str(self.lat)}, Lon: {str(self.lon)}"


class Ptum:
    """PTUM Class"""

    def __init__(self, origin: LatLon, radius: float) -> None:
        pass
