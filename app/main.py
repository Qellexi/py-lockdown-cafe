from __future__ import annotations
from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(self, friends: list[dict], cafe: Cafe) -> None:
    masks_to_buy = 0
    for visitor in friends:
        try:
            self.visit_cafe(visitor)
        except VaccineError:
            print("All friends should be vaccinated")
        except NotWearingMaskError:
            masks_to_buy += 1
            if masks_to_buy > 0:
                f"Friends should buy {masks_to_buy} masks"
        else:
            return f"Friends can go to {cafe.name}"
