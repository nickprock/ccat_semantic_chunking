from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, Field
from typing import Dict, Literal


class MySettings(BaseModel):
    """
    breakpoint_threshold_type must be one between ["percentile", "standard_deviation", "interquartile"]
    breakpoint_threshold_amount:
    recommended values by langchain
        "percentile": 95,
        "standard_deviation": 3,
        "interquartile": 1.5,

    """
    breakpoint_threshold_type: str = "percentile"
    breakpoint_threshold_amount: float = 95


@plugin
def settings_model():
    return MySettings
