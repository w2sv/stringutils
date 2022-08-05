import pytest

from stringutils import unique_hash


@pytest.mark.parametrize('input_string, expected', [
    ('aaaaaaaiaiaiaiai', 2730210105715975),
    ('uiuiiui', 5229154224271890),
    ('ÜiÜiÜiÜi', 5571490624003287)
])
def test_unique_hash(input_string, expected):
    assert unique_hash(input_string) == expected