from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class InputData(BaseModel):
    business_unit: str = Field(..., example="C170")
    request_id: str = Field(..., example="C170-20220107-094050-0001")
    inputs: dict = Field(..., example={
        "cust_no": "176ZpUZczEtk29&9+w1Fgw==",
        "date": "2022-01-07 09:40:50"
    })


class OutputData(BaseModel):
    business_unit: str
    request_id: str
    trace_id: str
    request_time: float
    response_time: float
    outputs: dict
