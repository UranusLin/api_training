from fastapi import HTTPException
from .models import InputData, OutputData
from .service import PredictService
import time
import logging

logger = logging.getLogger(__name__)


class PredictController:
    @staticmethod
    async def predict(data: InputData) -> OutputData:
        try:
            start_time = time.time()

            cust_no = data.inputs["cust_no"]
            date_str = data.inputs["date"]

            PredictService.validate_input(cust_no, date_str)
            outputs = PredictService.process_prediction(cust_no, date_str)

            end_time = time.time()

            return OutputData(
                business_unit=data.business_unit,
                request_id=data.request_id,
                trace_id="mock_trace_id",
                request_time=start_time,
                response_time=end_time,
                outputs=outputs
            )

        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            raise HTTPException(status_code=400, detail=str(e))
