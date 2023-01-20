# DYDX Protocol Service

A simple python API that allows XTF to interact with DYDX Protocol


### Setup

The code is written using Python3

#### Local

Install the dependencies
```
pip3 install Flask
pip3 install dydx-v3-python
pip3 install -U flask-cors
```

Start the app:
```
python3 python.py
```

Note: Currently the app is configured to run on local port 8001

### API Specs

<details>
    <summary>GET All Markets</summary>

Request Type: GET

Request Endpoint: /api/markets

Request Headers: None

Request Body: NA

Response Headers: None

Response Body:
```
[
    {
        "assetResolution": "100000000",
        "baseAsset": "AAVE",
        "baselinePositionSize": "7000",
        "incrementalInitialMarginFraction": "0.02",
        "incrementalPositionSize": "1400",
        "indexPrice": "86.7038",
        "initialMarginFraction": "0.1",
        "maintenanceMarginFraction": "0.05",
        "market": "AAVE-USD",
        "maxPositionSize": "70000",
        "minOrderSize": "0.1",
        "nextFundingAt": "2023-01-17T17:00:00.000Z",
        "nextFundingRate": "-0.0000152058",
        "openInterest": "21708.62",
        "oraclePrice": "86.8400",
        "priceChange24H": "7.073792",
        "quoteAsset": "USD",
        "status": "ONLINE",
        "stepSize": "0.1",
        "syntheticAssetId": "0x414156452d38000000000000000000",
        "tickSize": "0.01",
        "trades24H": "1097",
        "transferMarginFraction": "0.032499",
        "type": "PERPETUAL",
        "volume24H": "14869218.762000"
    }
]
```
</details>

### 👩‍💻 Resources

- [About-Us](https://dydx.exchange/about)