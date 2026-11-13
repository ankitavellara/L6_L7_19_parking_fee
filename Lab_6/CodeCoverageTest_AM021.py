
import pytest
from parking_fee import parking_fee, find_slot, monthly_pass


# ==========================================
# PARKING FEE TEST CASES
# ==========================================

def test_free_short_stay():
    assert parking_fee("car", 20, False, False) == 0


def test_unknown_vehicle():
    with pytest.raises(ValueError):
        parking_fee("bus", 60, False, False)


def test_negative_duration():
    with pytest.raises(ValueError):
        parking_fee("car", -10, False, False)


def test_paid_parking_exact_hour():
    assert parking_fee("car", 60, False, False) == 30


def test_paid_parking_partial_hour():
    assert parking_fee("car", 61, False, False) == 60


def test_ev_discount():
    assert parking_fee("car", 120, True, False) == 30


def test_truck_ev_no_discount():
    assert parking_fee("truck", 60, True, False) == 60


def test_lost_ticket_surcharge():
    assert parking_fee("bike", 60, False, True) == 210


# ==========================================
# PARKING SLOT TEST CASES
# ==========================================

def test_parking_lot_full():
    assert find_slot("car", 0, False) == "full"


def test_disabled_parking():
    assert find_slot("car", 5, True) == "ground floor"


def test_truck_parking():
    assert find_slot("truck", 5, False) == "basement"


def test_any_floor():
    assert find_slot("car", 5, False) == "any floor"


# ==========================================
# MONTHLY PASS TEST CASES
# ==========================================

def test_bike_monthly_pass():
    assert monthly_pass("bike", False) == 500


def test_car_monthly_pass():
    assert monthly_pass("car", False) == 1500


def test_resident_bike_discount():
    assert monthly_pass("bike", True) == 400


def test_resident_car_discount():
    assert monthly_pass("car", True) == 1200


def test_truck_monthly_pass_invalid():
    with pytest.raises(ValueError):
        monthly_pass("truck", False)
