# DayBetter Services Python Client

[![PyPI](https://img.shields.io/pypi/v/daybetter-services-python.svg)](https://pypi.org/project/daybetter-services-python/)
[![Python Versions](https://img.shields.io/pypi/pyversions/daybetter-services-python.svg)](https://pypi.org/project/daybetter-services-python/)
[![License](https://img.shields.io/pypi/l/daybetter-services-python.svg)](LICENSE)

Asynchronous client library used by the [Home Assistant DayBetter Services integration](https://github.com/home-assistant/core/pull/154677).  
It handles authentication, device discovery, status polling, PID metadata and device control against the DayBetter cloud API.

## Features

- Fully async `DayBetterClient` with context-manager support
- Automatic environment selection (test/prod) based on `hass_code`
- Convenience helpers for common API endpoints (devices, statuses, MQTT config)
- Sensor-focused workflow `fetch_sensor_data()` that merges devices, statuses and PID filters
- Type hints + `py.typed` for first-class editor / mypy support
- Published on PyPI for Home Assistant and other integrations

## Installation

```bash
pip install daybetter-services-python
```

## Quick Start

```python
import asyncio
from daybetter_python import DayBetterClient

async def main() -> None:
    async with DayBetterClient(token="YOUR_TOKEN", hass_code="db-xxxx") as client:
        # Fetch merged sensor payloads (used by Home Assistant)
        sensors = await client.fetch_sensor_data()
        for item in sensors:
            print(item["deviceName"], item.get("temp"), item.get("humi"))

        # Control a device (brightness example)
        await client.control_device(
            device_name="device_001",
            action=True,
            brightness=180,
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Home Assistant Integration

The official integration PR can be followed here: [home-assistant/core#154677](https://github.com/home-assistant/core/pull/154677).  
The integration imports this library and simply calls `client.fetch_sensor_data()` inside a data coordinator, so all business logic lives in this package.

See `docs/homeassistant.md` for:
- Installation instructions (pip, custom component)
- How to obtain the DayBetter token and `hass_code`
- Sample `configuration.yaml` snippets
- Known limitations and future roadmap

## Development

```bash
git clone https://github.com/THDayBetter/daybetter-services-python.git
cd daybetter-services-python
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# Quality checks
flake8 daybetter_python
mypy daybetter_python
pytest
```

Pull requests are welcome! Please open an issue if you encounter problems with the DayBetter cloud API.

## Release Process

1. Update `pyproject.toml`, `setup.py`, and `daybetter_python/__init__.py` with the new version.
2. Document changes in `CHANGELOG.md`.
3. Build and upload:
   ```bash
   rm -rf dist build *.egg-info
   python -m build
   twine check dist/*
   twine upload dist/*
   ```
4. Create a Git tag (e.g., `git tag v1.0.7 && git push origin v1.0.7`).

## License

This project is licensed under the [MIT License](LICENSE).
