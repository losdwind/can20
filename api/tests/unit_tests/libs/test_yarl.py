import pytest
from yarl import URL


def test_yarl_urls():
    expected_1 = "https://can20.ai/api"
    assert str(URL("https://can20.ai") / "api") == expected_1
    assert str(URL("https://can20.ai/") / "api") == expected_1

    expected_2 = "http://can20.ai:12345/api"
    assert str(URL("http://can20.ai:12345") / "api") == expected_2
    assert str(URL("http://can20.ai:12345/") / "api") == expected_2

    expected_3 = "https://can20.ai/api/v1"
    assert str(URL("https://can20.ai") / "api" / "v1") == expected_3
    assert str(URL("https://can20.ai") / "api/v1") == expected_3
    assert str(URL("https://can20.ai/") / "api/v1") == expected_3
    assert str(URL("https://can20.ai/api") / "v1") == expected_3
    assert str(URL("https://can20.ai/api/") / "v1") == expected_3

    with pytest.raises(ValueError) as e1:
        str(URL("https://can20.ai") / "/api")
    assert str(e1.value) == "Appending path '/api' starting from slash is forbidden"
