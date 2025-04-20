from __future__ import annotations

from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
from datetime import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name


    def visit_cafe(self, visitor: dict):
        if not "vaccine" in visitor.keys():
            raise NotVaccinatedError()
        elif visitor.get("vaccine").get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError()
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError()
        else:
            return f"Welcome to {self.name}"
