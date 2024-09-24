from fastapi import APIRouter
from .models import InputData, OutputData
from .controller import PredictController

router = APIRouter()

@router.post("/predict/v1", response_model=OutputData)
async def predict(data: InputData):
    return await PredictController.predict(data)