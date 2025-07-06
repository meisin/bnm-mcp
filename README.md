# BNM-MCP

A Modular Command Platform (MCP) for connecting to the Bank Negara Malaysia (BNM) public API.  
This project provides tools to fetch various financial data from BNM, such as exchange rates, base rates, gold prices, and more.

## Features

- Get currency exchange rates from the Interbank Foreign Exchange Market in Kuala Lumpur
- Retrieve current Base Rates and Lending Rates
- Fetch daily foreign exchange turnover
- Access Financial Consumer Alert lists
- Obtain daily interbank swap volumes
- Get Islamic interbank deposit rates
- Retrieve daily gold bullion coin prices (Kijang Emas)
- Get Overnight Policy Rate (OPR)
- Fetch USD/MYR intraday and reference rates

## Requirements

- Python 3.9+
- [httpx](https://www.python-httpx.org/)
- [pydantic](https://docs.pydantic.dev/)
- MCP framework (assumed to be provided by `mcp.server.fastmcp`)

Install dependencies with:

```sh
pip install httpx pydantic
```

## Usage

1. Clone this repository.
2. Ensure all dependencies are installed.
3. Run the MCP server:

```sh
python main.py
```

The server will start and expose the tools via the MCP interface.

## Tools Overview

Each tool is an async function decorated with `@mcp.tool()` and can be called to fetch specific data:

- `get_exchange_rate(session, quote)`
- `get_base_rate()`
- `get_daily_FX_turnover()`
- `get_financial_consumer_alert()`
- `get_interbank_swap()`
- `get_islamic_interbank_rate()`
- `get_kijang_emas()`
- `get_overnight_policy_rate()`
- `get_usd_myr_intraday_rate()`
- `get_usd_myr_reference_rate()`

### Example Tool Call

```python
result = await get_exchange_rate(session=EX_session(session="0900"), quote=Base_currency(quote="fx"))
print(result)
```

## Configuration

- The API base URL is set to `https://api.bnm.gov.my/public`
- User-Agent is set to `bnm-app/1.0`

## License

This project is for research and educational purposes. Please refer to Bank Negara Malaysia's API terms of use for data usage policies.