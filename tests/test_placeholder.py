from daybetter_python import DayBetterClient


def test_client_attributes() -> None:
    client = DayBetterClient(token="abc123")
    assert client.token == "abc123"

