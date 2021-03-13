import ftx 
import sys 
apikey = ''
apisecret = ''
limitPrice = 
size =      
client = ftx.FtxClient(api_key = apikey, api_secret = apisecret)
sys.tracebacklimit = 0
while 1 :
    try:
        client.place_order('OXY/USD', 'buy', 0.5, 100)
    except Exception:
        pass
    