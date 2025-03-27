from delta_rest_client import DeltaRestClient
delta_client = DeltaRestClient(
  base_url='https://cdn-ind.testnet.deltaex.org',
  api_key='3e9PJ3Q0XxirZaeXe9QkdsSUKPzZ5y',
  api_secret='tu3mmqonRq18P0YxIyM4sDsEiQdUFIELZUqtygho19tox6gWzlcB1VECejca'
)
delta_client
orders = delta_client.get_live_orders()
