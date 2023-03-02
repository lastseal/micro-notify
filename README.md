# Micro Notify
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Instalación

```bash
pip install git+https://github.com/lastseal/micro-notify
```

## Uso Básico

```python
from micro import notify

@notify.listen("event")
def main(channel, payload):
    print("Hello World")
```
