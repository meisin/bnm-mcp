# BNM-MCP

A Model Context Protocol (MCP) Server for connecting to the Bank Negara Malaysia (BNM) [Open API](https://apikijangportal.bnm.gov.my/openapi).
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

- Python >=3.11
- MCP SDK 1.2.0 or higher
- `uv` package manager

### Install uv Package Manager
Method 1: Using pip (Recommended for most users)
```sh
pip install uv
```
Method 2: For Unix systems (Linux, macOS):
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Usage

1. Clone this repository.
```sh
git clone https://github.com/meisin/bnm-mcp.git
```

2. Install dependencies.
```sh
uv sync
```

5. Run the MCP server:

```sh
uv run main.py
```

The server will start and expose the tools via the MCP interface.

## Connecting to Claude Desktop
1. Install Claude Desktop from the official website
2. Configure Claude Desktop to use your MCP server:
```sh
{
    "mcpServers": {
        "mcp-server": {
            "command": "uv",  # It's better to use the absolute path to the uv command
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/YOUR/bnm-mcp",
                "run",
                "main.py"
            ]
        }
    }
}
```

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

## License

This project is for research and educational purposes. Please refer to Bank Negara Malaysia's API terms of use for data usage policies.
