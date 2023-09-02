import asyncio

from API import *
from sessions import *
import websockets
import json

# TODO: Explore websockets for streaming data.

import os

from dotenv import load_dotenv

load_dotenv()


with TastyworksSession(os.environ.get("TT_USERNAME"), os.environ.get("TT_PASSWORD")) as session:
    print(get_net_liquidating_value_history(session["session-token"], "5WW13756"))
    print(get_volatility_data(session["session-token"], ["AAPL", "TSLA"]))
    print(get_dividend_history(session["session-token"], "AAPL"))


























