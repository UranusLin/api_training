from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class PredictService:
    @staticmethod
    def validate_input(cust_no: str, date_str: str):
        if len(cust_no) != 24:
            raise ValueError("cust_no should be 24 characters long")

        try:
            datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("Invalid date format")

    @staticmethod
    def process_prediction(cust_no: str, date_str: str):
        # Mock processing (replace with actual logic)
        active_prod_cnt = 5
        avg_num_3m = 817678.667

        if active_prod_cnt < 0 or avg_num_3m < 0:
            raise ValueError("active_prod_cnt and avg_num_3m must be non-negative")

        return {
            "status_code": "0000",
            "status_msg": "API success",
            "cust_no": cust_no,
            "date": date_str,
            "active_prod_cnt": active_prod_cnt,
            "avg_num_3m": avg_num_3m
        }
