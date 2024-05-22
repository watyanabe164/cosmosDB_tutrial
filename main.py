"""利用token数と利用料金を集計する"""

import sys
from datetime import datetime, timedelta
from correct_token_usage import TotalingTokenUsage, ClientsInfo

from logger import logger

try:
    ### メイン処理 ###
    fetch_size = 100

    usage_client = TotalingTokenUsage(cosmos_url, cosmos_key, "mediator", "chat_history")
    usage_results = usage_client.get_token_usages_group_by_appid(fetch_size)
    print(list(usage_results))

    clients_info = ClientsInfo(cosmos_url, cosmos_key, "mediator", "chat_history")
    clients_results = clients_info.get_clients_info(fetch_size)
    print(list(clients_results))
except Exception as e:
    logger.exception("token集計中にエラーが発生しました")
    raise RuntimeError from e