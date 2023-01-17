from flask import Flask
from dydx3 import Client
from web3 import Web3
from flask import jsonify


PORT = 8001

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
  return 'Hello %s!' % name

@app.route('/api/markets')
def get_markets():
  public_client = Client(
    host='https://api.stage.dydx.exchange',
  )
  markets = []
  for market in public_client.public.get_markets().data["markets"]:
    markets.append(public_client.public.get_markets().data["markets"][market])

  return markets


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=PORT)


