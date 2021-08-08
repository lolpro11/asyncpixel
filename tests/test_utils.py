"""Test bazaar."""
import datetime

from asyncpixel import utils


def test_calc_player_level() -> None:
    """Calc player level."""
    assert utils.calc_player_level(0) == 1.0

def test_get_rank() -> None:
    """Check api error."""
    assert utils.get_rank(prefix_raw="[VIP]") == "VIP"
    assert utils.get_rank(rank="VIP") == "VIP"
    assert utils.get_rank(rank="NORMAL") == None
    assert utils.get_rank(package_rank="VIP") == "VIP"
    assert utils.get_rank(new_package_rank="VIP") == "VIP"
    assert utils.get_rank(monthly_package_rank="VIP") == "VIP"
