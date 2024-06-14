# Fileforge Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

The Fileforge Python Library provides convenient access to the Fileforge API from applications written in Python. 

The library includes type definitions for all request and response fields, and offers both synchronous and asynchronous clients powered by httpx.

## Installation

Add this dependency to your project's build file:

```bash
pip install fileforge
# or
poetry add fileforge
```

## Usage
Simply import `Fileforge` and start making calls to our API. 

```python
from fileforge import GenerateRequestOptions
from fileforge.client import Fileforge

client = Fileforge(
    api_key="YOUR_API_KEY" # Defaults to FILEFORGE_API_KEY
)
client.generate(
    options=GenerateRequestOptions(),
    files=["path/to/file1", "path/to/file2"]
)
```

## Async Client
The SDK also exports an async client so that you can make non-blocking
calls to our API. 

```python
from fileforge import GenerateRequestOptions
from fileforge.client import AsyncFileforge

client = AsyncFileforge(
    api_key="YOUR_API_KEY"  # Defaults to FILEFORGE_API_KEY
)

async def main() -> None:
    client.generate(
        options=GenerateRequestOptions(),
        files=["path/to/file1", "path/to/file2"]
    )
asyncio.run(main())
```

## Exception Handling
All errors thrown by the SDK will be subclasses of [`ApiError`](./src/schematic/core/api_error.py).

```python
import fileforge

try:
    client.generate(...)
except fileforge.core.ApiError as e: # Handle all errors
  print(e.status_code)
  print(e.body)
```

## Advanced

### Timeouts
By default, requests time out after 60 seconds. You can configure this with a 
timeout option at the client or request level.

```python
from fileforge.client import Fileforge

client = Fileforge(
    # All timeouts are 20 seconds
    timeout=20.0,
)

# Override timeout for a specific method
fileforge.generate(..., {
    timeout_in_seconds=20.0
})
```

### Retries
The SDK is instrumented with automatic retries with exponential backoff. A request will be
retried as long as the request is deemed retriable and the number of retry attempts has not grown larger
than the configured retry limit (default: 2).

A request is deemed retriable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)
  
Use the `max_retries` request option to configure this behavior. 

```python
client.generate(..., {
     max_retries=1
})
```

### Custom HTTP client
You can override the httpx client to customize it for your use-case. Some common use-cases 
include support for proxies and transports.

```python
import httpx

from fileforge.client import Fileforge

client = Fileforge(
    http_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Beta Status

This SDK is in **Preview**, and there may be breaking changes between versions without a major 
version update. 

To ensure a reproducible environment (and minimize risk of breaking changes), we recommend pinning a specific package version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. 
Additions made directly to this library would have to be moved over to our generation code, 
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
 a proof of concept, but know that we will not be able to merge it as-is. We suggest opening 
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
