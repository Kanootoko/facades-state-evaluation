"""
Exceptions connected with buildings.
"""

from fastapi import status
from facades_api.utils import FacadesApiError


class TooManyBuildingsError(FacadesApiError):
    """
    Exception of too big number of buildings returned after user request.
    """
    def __init__(self, buildings: int, maximum_buildings: int):
        self.buildings = buildings
        self.maximum_buildings = maximum_buildings
        super().__init__()

    def status_code(self) -> int:
        return status.HTTP_400_BAD_REQUEST

    def __str__(self) -> str:
        return f"Too many buildings requested: {self.buildings} with a maximum of {self.maximum_buildings}"
