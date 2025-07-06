# 💹💹 BNM-MCP 📊📊

A Model Context Protocol (MCP) Server for connecting to the Bank Negara Malaysia (BNM) [Open API](https://apikijangportal.bnm.gov.my/openapi).
This project provides tools to fetch various financial data from BNM, such as exchange rates, base rates, gold prices, and more.

## Disclaimer
This MCP server is neither affiliated with BNM nor endorsed by BNM; the server leverages on BNM's OpenAPI endpoints and contains just a subset of BNM's API. 

## Available Tools 📊💰🏦💹

### Exchange Rates & Currency

`get_exchange_rate` - Get currency exchange rates from the Interbank Foreign Exchange Market in Kuala Lumpur. Prices of selected countries' currencies are quoted in relation to Ringgit.

`get_usd_myr_intraday_rate` - Get latest USD/MYR (US Dollar - Malaysian Ringgit) interbank intraday highest and lowest exchange rate. Rates are obtained from the best U.S. dollar against Malaysian ringgit interbank highest and lowest dealt rates by commercial banks.

`get_usd_myr_reference_rate` - Get latest reference rate that is computed based on weighted average volume of the interbank USD/MYR FX spot rate transacted by the domestic financial institutions and published daily at 3:30 p.m.

`get_daily_FX_turnover` - Get daily foreign exchange turnover for all currencies including interbank and customer deals.

### Interest Rates

`get_base_rate` - Get current Base Rates or Base Lending Rates for retail loans or financing facilities and Indicative Effective Lending Rates for a standard housing loan/home financing offered by financial institutions in Malaysia.

`get_overnight_policy_rate` - Get Overnight Policy Rate (OPR) decided by the Monetary Policy Committee.

`get_malaysia_overnight_rate_i` - Get Malaysia overnight rate from Bank Negara Malaysia.

`get_islamic_interbank_rate` - Get daily weighted average of Islamic interbank deposit rates for various tenures.

`get_interest_rates_banking_institution` - Get interest rates by banking institution.

### Money & Banking

`get_reserve_money` - Get latest reserve money data by Bank Negara Malaysia.

`get_currency_circulation_by_denomination` - Get Currency in Circulation by Denomination of:
- **Coins:** one cent, five cent, ten cent, twenty cent, fifty cent, one ringgit
- **Notes:** one ringgit, five ringgit, ten ringgit, twenty ringgit, fifty ringgit, one hundred ringgit

`get_monetary_aggregates_M1_M2_M3` - Get monetary aggregates M1, M2, and M3 data by Bank Negara Malaysia.

`get_broad_money_M3` - Get Broad Money M3 data by Bank Negara Malaysia.

`get_bnm_statement_assets` - Get statement of assets of Bank Negara Malaysia.

`get_banking_system_statement_assets` - Get statement of assets for banking systems. Available banking institution types: commercial, islamic, investment, total.

### Market Data
`get_interbank_swap` - Get daily interbank swap volume by tenure.

`get_kijang_emas` - Get daily trading prices of Malaysia gold bullion coin.

`get_malaysian_government_securities_market_indicative_yield` - Get Malaysian Government securities Market Indicative Yield from Bank Negara Malaysia.

`get_volume_transaction_interbank_money_market` - Get Volume of Transaction in Interbank Money Market from Bank Negara Malaysia.

`get_volume_transaction_kl_foreign_exchange_market` - Get Volume of Interbank Transactions in the Kuala Lumpur Foreign Exchange Market from Bank Negara Malaysia.

`get_bond_market_highlights` - Get market highlights for the bond market.

### Government & Economy

`get_federal_government_finance` - Get Federal Government Finance data.

`get_external_reserves` - Get information of External Reserves from Bank Negara Malaysia.

`get_labour_market_indicators_financial_services_sector` - Get Labour Market Indicators for the Financial Services Sector from Bank Negara Malaysia.

### Consumer Protection

`get_financial_consumer_alert` - Get list of companies and websites which are neither authorised nor approved under the relevant laws and regulations administered by BNM.

### Islamic Finance
 `get_takaful_key_indicators` - Get Takaful Key Indicators from Bank Negara Malaysia.

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

## Getting Started 🛠️🛠️🛠️

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

## License

This project is for research and educational purposes. Please refer to Bank Negara Malaysia's API terms of use for data usage policies.
