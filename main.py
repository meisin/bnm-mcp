from mcp.server.fastmcp import FastMCP
from typing import Any
import httpx
import json
import os

from pydantic import BaseModel
from typing import Literal

class BNM_input(BaseModel):
    type: Literal["commercial", "islamic", "investment", "total"]

class Forex_input(BaseModel):
    session: Literal["0900", "1130", "1200", "1700"]
    quote: Literal["rm", "fx"]

mcp = FastMCP(
    name="bnm-mcp",
    description="A MCP for connecting Bank Negara Malaysia (BNM) API.",
    version="0.1.0",
    author="bnm",
    author_url=""
    )

USER_AGENT = "bnm-app/1.0"
BNM_API_BASE = "https://api.bnm.gov.my/public"

async def make_bnm_request(url: str) -> dict[str, Any] | None:
    """Make a request to BNM API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.BNM.API.v1+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
        
@mcp.tool()
async def get_exchange_rate(session: Forex_input | None, quote: Forex_input | None):
    """Get currency exchange rates from the Interbank Foreign Exchange Market in Kuala Lumpur. 
       The price of selected countries currency are quoted in relation to Ringgit.
    Args:
        session (optional): the session on which the rate is taken from. 
                            The allowed values are defined in EX_session. 
        quote (optional): the Base Currency (Ringgit Or Foreign Currency) As The Denominator For The Exchange Rate. 
                          The allowed values are defined in Base_currency.
    Returns:
        Exchange rate data or error message.
    """
    if session is None and quote is None:
        url = f"{BNM_API_BASE}/exchange-rate"
    else:
        temp_url = f"{BNM_API_BASE}/exchange-rate?session={session.session}&quote={quote.quote}"
        url = temp_url.replace("'", "")

    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch exchange rate from Bank Negara."

    return data['data']

@mcp.tool()
async def get_base_rate():
    """
    Get current Base Rates or Base Lending Rates for retail loans or financing facilities and 
    Indicative Effective Lending Rates for a standard housing loan/home financing offered by 
    financial institutions in Malaysia.
    
    Returns:
        Latest base rate information or error message.
    """
    url = f"{BNM_API_BASE}/base-rate"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch base rate from Bank Negara."
    #rate = [format_alert(feature) for feature in data["features"]]
    return data['data']

@mcp.tool()
async def get_daily_FX_turnover():
    """
    Get Daily foreign exchange turnover for all currencies including interbank and customer deals.
    
    Returns:
        Latest base rate information or error message.
    """
    url = f"{BNM_API_BASE}/fx-turn-over"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch base rate from Bank Negara."
    return f"""
        Total turn over: {data['data']}"""


@mcp.tool()
async def get_financial_consumer_alert():
    """
    Get list of is companies and websites which are  neither authorised nor approved under the relevant laws and regulations administered by BNM.
    Returns:
        Latest Financial Consumer Alert list or error message.
    """
    url = f"{BNM_API_BASE}/consumer-alert"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch Financial Consumer Alert from Bank Negara."
    return data['data']


@mcp.tool()
async def get_interbank_swap():
    """
    Get Daily interbank swap volume by tenure.

    Returns:
        Latest Daily Interbank Swap Volume by tenure or error message.
    """
    url = f"{BNM_API_BASE}/interbank-swap"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch Financial Consumer Alert from Bank Negara."
    
    return data['data']

@mcp.tool()
async def get_islamic_interbank_rate():
    """
    Get Daily weighted average of Islamic interbank deposit rates for various tenures.

    Returns:
        Latest Islamic Interbank Rate or error message.
    """
    url = f"{BNM_API_BASE}/islamic-interbank-rate"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch Islamic Interbank Rate from Bank Negara."
    
    return data['data']

@mcp.tool()
async def get_kijang_emas():
    """
    Get Daily trading prices of Malaysia gold bullion coin.

    Returns:
        Latest gold trading prices or error message.
    """
    url = f"{BNM_API_BASE}/kijang-emas"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch daily Gold trading prices from Bank Negara."
    
    return data['data']

@mcp.tool()
async def get_overnight_policy_rate():
    """
    Get Overnight Policy Rate (OPR) decided by the Monetary Policy Committee.

    Returns:
        Latest OPR or error message.
    """
    url = f"{BNM_API_BASE}/opr"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch Overnight Policy Rate (OPR)."
    
    return data['data']

@mcp.tool()
async def get_usd_myr_intraday_rate():
    """
    Get latest USD/MYR (US Dollar - Malaysian Ringgit) interbank intraday highest and lowest exchange rate. 
    Rates are obtained from the best U.S. dollar against Malaysian ringgit interbank highest and 
    lowest dealt rates by commercial banks.

    Returns:
        Latest USD/MYR intraday highest and lowest exchange rate or error message.
    """
    url = f"{BNM_API_BASE}/usd-interbank-intraday-rate"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch US Dollar- Malaysian Ringgit intraday rate."
    
    return data['data']

@mcp.tool()
async def get_usd_myr_reference_rate():
    """
    Get latest reference rate that is computed based on weighted average volume of the 
    interbank USD/MYR FX spot rate transacted by the domestic financial institutions and 
    published daily at 3:30 p.m.

    Returns:
        Latest USD/MYR reference rate that is computed based on weighted average volume or error message.
    """
    url = f"{BNM_API_BASE}/kl-usd-reference-rate"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch US Dollar- Malaysian Ringgit reference rate."
    
    return data['data']

@mcp.tool()
async def get_malaysia_overnight_rate_i():
    """
    Get Malaysia overnight rate from Bank Negara Malaysia.

    Returns:
        Latest Malaysia overnight rate or error message.
    """
    url = f"{BNM_API_BASE}/my-overnight-rate-i"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch Malaysia overnight rate."
    
    return data['data']

"""
===================
Montary and Banking 
===================
"""

@mcp.tool()
async def get_reserve_money():
    """
    Get latest reserve money data by Bank Negara Malaysia.

    Returns:
        Latest data on BNM's Money Reserve or error message.
    """
    url = f"{BNM_API_BASE}/msb/1.1"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch latest Money Reserve data."

    return data['data']

@mcp.tool()
async def get_currency_circulation_by_denomination():
    """
    Get Currency in Circulation by Denomination of coins: one cent, five cent, ten cent, twenty cent, fifty cent, one ringgit.
    Notes: one ringgit, five ringgit, ten ringgit, twenty ringgit, fifty ringgit, one hundred ringgit.

    Returns:
        Latest currency in circulation by denomination or error message.
    """
    url = f"{BNM_API_BASE}/msb/1.2"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch currency in circulation."
    
    return data['data']

@mcp.tool()
async def get_monetary_aggregates_M1_M2_M3():
    """
    Get monetary aggregates M1, M2, and M3 data by Bank Negara Malaysia.

    Returns:
        Latest monetary aggregates M1, M2 and M3 or error message.
    """
    url = f"{BNM_API_BASE}/msb/1.3"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch monetary aggregates M1, M2 and M3."
    

    return data['data']

@mcp.tool()
async def get_broad_money_M3():
    """
    Get Broad Money M3 data by Bank Negara Malaysia.

    Returns:
        Latest Broad Money M3 or error message.
    """
    url = f"{BNM_API_BASE}/msb/1.3.1"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch Broad Money M3 from Bank Negara."
    
    return data['data']

@mcp.tool()
async def get_bnm_statement_assets():
    """
    Get statement of assets of Bank Negara Malaysia.

    Returns:
        Latest statement of assets of Bank Negara Malaysia or error message.
    """
    url = f"{BNM_API_BASE}/msb/1.4"
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch statement of assets."
    
    schema = {
    "bil_dis": "Bills Discounted",
    "def_exp": "Deferred Expenditure",
    "dep_wit_fin_ins": "Deposits with Financial Institutions",
    "gol_for_exc": "Gold and Foreign Exchange",
    "hol_of_spe_dra_rig": "Holdings of Special Drawing Rights",
    "imf_res_tra_pos": "IMF Reserve Tranche Position",
    "loa_and_adv": "Loans and Advances",
    "mal_gov_pap": "Malaysian Government Papers",
    "month_dt": "End of Period (Month)",
    "oth_ass": "Other Assets",
    "pro_lan_and_bui": "Properties - Land and Buildings",
    "tot_ass": "Total Assets",
    "year_dt": "End of Period (Year)",
    "year_month": "End of Period"
    }

    combined = {k: (data['data'][k], schema[k]) for k in data['data']}
    return combined
    #return data['data']

@mcp.tool()
async def get_banking_system_statement_assets(type: BNM_input | None):
    """
    Get Statement of assets for banking systems. The available banking institution types are defined in Banking_institution_type.

    Returns:
        Latest statement of assets based on the type of banking institution or error message.
    """
    if type is None:
        return f"Please specify one of the following banking institution types: {Banking_institution_type}"
    else:
        temp_url = f"{BNM_API_BASE}/msb/1.7?type={type.type}"
        url = temp_url.replace("'", "")
    
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch banking system statement of assets."
    
    return data['data']


"""
=============================
Financial and Capital Markets 
=============================
"""
@mcp.tool()
async def get_interest_rates_banking_institution():
    """
    Get Interest Rates by banking institution.
    
    Returns:
        Latest statement of assets based on the type of banking institution or error message.
    """
    url = f"{BNM_API_BASE}/msb/2.1"
    
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch Interest Rate By Banking Institution."
    
    return data['data']

@mcp.tool()
async def get_malaysian_government_securities_market_indicative_yield():
    """
    Get Malaysian Government securities Market Indicative Yield from Bank Negara Malaysia.
    
    Returns:
        Latest government securities market indicative yield or error message.
    """
    url = f"{BNM_API_BASE}/msb/2.5"
    
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch government securities market indicative yield."
    
    return data['data']

@mcp.tool()
async def get_volume_transaction_interbank_money_market():
    """
    Get Volume of Transaction in Interbank Money Market from Bank Negara Malaysia.
    
    Returns:
        Latest Volume of Transaction in Interbank Money Market or error message.
    """
    url = f"{BNM_API_BASE}/msb/2.7"
    
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch Volume of Transaction in Interbank Money Market."
    
    return data['data']

@mcp.tool()
async def get_volume_transaction_kl_foreign_exchange_market():
    """
    Get Volume of Interbank Transactions in the Kuala Lumpur Foreign Exchange Market from Bank Negara Malaysia.
    
    Returns:
        Latest Volume of Interbank Transactions in the Kuala Lumpur Foreign Exchange Market or error message.
    """
    url = f"{BNM_API_BASE}/msb/2.8"
    
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch Volume of Interbank Transactions in the Kuala Lumpur Foreign Exchange Market."
    
    return data['data']

"""
============================================
External Sector and Macroeconomic Indicators 
============================================
"""
@mcp.tool()
async def get_federal_government_finance():
    """
    Get Federal Government Finance.
    
    Returns:
        Latest federal government finance or error message.
    """
    url = f"{BNM_API_BASE}/msb/3.1"
    
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch Federal Government Finance."
    
    return data['data']

@mcp.tool()
async def get_labour_market_indicators_financial_services_sector():
    """
    Get Labour Market Indicators for the Financial Services Sector from Bank Negara Malaysia.
    
    Returns:
        Latest Labour Market Indicators for the Financial Services Sector or error message.
    """
    url = f"{BNM_API_BASE}/msb/3.5.12a"
    
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch Labour Market Indicators for the Financial Services Sector."
    
    return data['data']

@mcp.tool()
async def get_external_reserves():
    """
    Get information of External Reserves from Bank Negara Malaysia.
    
    Returns:
        Latest informtaion on External Reserves or error message.
    """
    url = f"{BNM_API_BASE}/msb/3.8"
    
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch information on External Reserves."
    
    return data['data']


"""
=============================
Insurance and Takaful
=============================
"""
@mcp.tool()
async def get_takaful_key_indicators():
    """
    Get Takaful Key Indicators from Bank Negara Malaysia.
    
    Returns:
        Latest takaful key indicators or error message.
    """
    url = f"{BNM_API_BASE}/msb/4.11"
    
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch Takaful Key Indicators."
    
    return data['data']

"""
===================
Bond Info Hub (HIB)
===================
"""
@mcp.tool()
async def get_bond_market_highlights():
    """
    Get Market Highlights for the bond market.
    
    Returns:
        Latest market highlights for the bond market or error message.
    """
    url = f"{BNM_API_BASE}/msb/bih/market-highlights"
    
    data = await make_bnm_request(url)

    if not data:
        return "Unable to fetch market highlights for the Bond Market."
    
    return data['data']



if __name__ == "__main__":
    mcp.run(transport="stdio")


## Not used:
## Islamic Interbank Money Market (IIMM)
