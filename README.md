## creprox :ninja:
REST-ly perform an HTTP GET request with rotating user agents.

```http
GET https://creprox.vercel.app/httpbin.org/get
```

> [!WARNING]
> Due to the continuous gateway errors, rotating proxy has been removed.

### Usage

Place the URL without the protocols after the `creprox.vercel.app`. For example:

```http
GET https://creprox.vercel.app/example.com
```

Which will be transformed into a new URL with `https` protocol.
