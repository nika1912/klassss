"""Пакет geometry: плоские и пространственные фигуры."""
from geometry.flat import circle_area, triangle_area
from geometry.solid import sphere_volume, cube_volume

__all__ = ["circle_area", "triangle_area", "sphere_volume", "cube_volume"]
__version__ = "0.2.0"