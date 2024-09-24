import pytest
from api.service import PredictService


def test_validate_input():
    # Valid input
    PredictService.validate_input("176ZpUZczEtk29&9+w1Fgw==", "2022-01-07 09:40:50")

    # Invalid cust_no
    with pytest.raises(ValueError, match="cust_no should be 24 characters long"):
        PredictService.validate_input("short", "2022-01-07 09:40:50")

    # Invalid date
    with pytest.raises(ValueError, match="Invalid date format"):
        PredictService.validate_input("176ZpUZczEtk29&9+w1Fgw==", "invalid-date")


def test_process_prediction():
    result = PredictService.process_prediction("176ZpUZczEtk29&9+w1Fgw==", "2022-01-07 09:40:50")
    assert result["status_code"] == "0000"
    assert result["status_msg"] == "API success"
    assert result["active_prod_cnt"] >= 0
    assert result["avg_num_3m"] >= 0
