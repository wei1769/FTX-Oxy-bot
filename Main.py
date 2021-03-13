#run 'pip3 install ftx' first 
import ftx 
import sys 
apikey = ''  #api key
apisecret = ''  #api secret
limitPrice = #Price to bid
size =      #Size to bid 
client = ftx.FtxClient(api_key = apikey, api_secret = apisecret)
sys.tracebacklimit = 0
while 1 :
    try:
        client.place_order('OXY/USD', 'buy', limitPrice,size )
    except Exception:
        pass
    