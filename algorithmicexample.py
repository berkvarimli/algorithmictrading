####################################################################################################################
####################################################################################################################
####################################################################################################################
########################### ALGORITHMIC TRADE WITH PYTHON - SCANNING BINANCE PAIRS #################################
########################## IT IS NOT INVESTMENT ADVISE. For Educational Purposes ONLY ##############################
####################################################################################################################
####################################################################################################################
################################### SAIT BERK VARIMLI - ELECTRONIC ENGINEER ########################################
########################################## berkvarimli@gmail.com ###################################################
####################################################################################################################



from binance.client import Client
import configparser
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ta
from ta import add_all_ta_features
from ta.utils import dropna
import time
import requests
from datetime import date
import emoji
import csv


# Loading keys from config file
test_api_key = '' ## YOUR BINANCE API KEY
test_secret_key = '' ## YOUR BINANCE SECRET KEY

client = Client(test_api_key, test_secret_key)
## YOU CAN ADD PAIR FROM BINANCE WHICH YOU WANT TO PROCESS
allsymbols = ["BTCUSDT","ETHUSDT","XRPUSDT","BNBUSDT","WINUSDT","TRXUSDT","LTCUSDT","FILUSDT","BTTUSDT","EOSUSDT","DOTUSDT","ENJUSDT","CHZUSDT","LINKUSDT","HOTUSDT","ETCUSDT","THETAUSDT","1INCHUSDT","BCHUSDT","QTUMUSDT","WRXUSDT","SOLUSDT","SXPUSDT","ADAUSDT","NKNUSDT","XLMUSDT","OMGUSDT","ONEUSDT","DENTUSDT","VETUSDT","OGNUSDT","CAKEUSDT","KSMUSDT","AVAXUSDT","SUSHIUSDT","ONTUSDT","DOGEUSDT","XTZUSDT","AKROUSDT","STORJUSDT","YFIUSDT","BZRXUSDT","NEOUSDT","BLZUSDT","XEMUSDT","CRVUSDT","KAVAUSDT","ANKRUSDT","AAVEUSDT","USDTTRY","FTMUSDT","GRTUSDT","LUNAUSDT","MITHUSDT","VITEUSDT","PSGUSDT","MATICUSDT","KMDUSDT","BELUSDT","EGLDUSDT","BANDUSDT","STMXUSDT","ZECUSDT","ATOMUSDT","DASHUSDT","ALGOUSDT","IOSTUSDT","BTSUSDT","SANDUSDT","ZILUSDT","HNTUSDT","BATUSDT","GBPUSDT","ALPHAUSDT","RENUSDT","FLMUSDT","SRMUSDT","COMPUSDT","RUNEUSDT","ZENUSDT","NEARUSDT","YFIIUSDT","REEFUSDT","UNFIUSDT","UNIUSDT","IOTAUSDT","RSRUSDT","TRBUSDT","ICXUSDT","XMRUSDT","LINAUSDT","CTKUSDT","OCEANUSDT","TFUELUSDT","ZRXUSDT","COTIUSDT","KNCUSDT","CHRUSDT","SKLUSDT","SCUSDT","AUDIOUSDT","GTOUSDT","WAVESUSDT","MTLUSDT","HBARUSDT","DODOUSDT","SNXUSDT","BALUSDT","FTTUSDT","CVCUSDT","MBLUSDT","MANAUSDT","CELRUSDT","RLCUSDT","LITUSDT","CTSIUSDT","JUVUSDT","ALICEUSDT","SFPUSDT","DATAUSDT","XVSUSDT","TOMOUSDT","RVNUSDT","AXSUSDT","STXUSDT","ARPAUSDT","PONDUSDT","FETUSDT","JSTUSDT","SUNUSDT","VTHOUSDT","BTCSTUSDT","TUSDUSDT","ACMUSDT","ROSEUSDT","KEYUSDT","SUPERUSDT","FUNUSDT","PERLUSDT","TCTUSDT","ETHUPUSDT","CKBUSDT","OGUSDT","DIAUSDT","USDTDAI","WTCUSDT","PNTUSDT","MFTUSDT","HARDUSDT","ANTUSDT","OXTUSDT","DREPUSDT","LRCUSDT","FIOUSDT","AIONUSDT","DEGOUSDT","IOTXUSDT","ONGUSDT","REPUSDT","PAXUSDT","TWTUSDT","LSKUSDT","ASRUSDT","DOCKUSDT","HIVEUSDT","LTOUSDT","DGBUSDT","USDTBIDR","COSUSDT","ATMUSDT","RAMPUSDT","STPTUSDT","TROYUSDT","ORNUSDT","NANOUSDT","WANUSDT","STRAXUSDT","NULSUSDT","INJUSDT","MDTUSDT","WINGUSDT","BEAMUSDT","ARDRUSDT","FIROUSDT","PERPUSDT","UMAUSDT","AVAUSDT","OMUSDT","UTKUSDT","BNTUSDT","COCOSUSDT","USDTRUB","NBSUSDT","PAXGUSDT","NMRUSDT","DUSKUSDT","RIFUSDT","WNXMUSDT","IRISUSDT","BADGERUSDT","CELOUSDT","DNTUSDT","AUTOUSDT","TRUUSDT","DCRUSDT","SUSDUSDT","CTXCUSDT","FISUSDT","USDTBVND"]
##allsymbolsbtc = ["BTCUSDT","XRPBTC","BTCBUSD","BNBBTC","ETHBTC","BTCEUR","VETBTC","LTCBTC","XLMBTC","TRXBTC","ARDRBTC","ADABTC","NKNBTC","BTCUSDC","ENJBTC","CAKEBTC","FILBTC","SXPBTC","BTCGBP","DOGEBTC","XTZBTC","BCHBTC","LINKBTC","DOTBTC","XMRBTC","BATBTC","KNCBTC","CTXCBTC","WAVESBTC","WRXBTC","ELFBTC","OMGBTC","EOSBTC","THETABTC","MDTBTC","GRSBTC","BTGBTC","1INCHBTC","RUNEBTC","WBTCBTC","EGLDBTC","QTUMBTC","CHZBTC","SOLBTC","FTTBTC","IOTABTC","ZECBTC","ATOMBTC","ZRXBTC","OGNBTC","VITEBTC","XEMBTC","AVAXBTC","BEAMBTC","BTCTRY","VIABTC","ALGOBTC","UNIBTC","RAMPBTC","LINABTC","LUNABTC","XVGBTC","MITHBTC","SCBTC","ETCBTC","ZILBTC","AIONBTC","GRTBTC","SRMBTC","BTCAUD","YFIBTC","ONEBTC","FORBTC","DASHBTC","TOMOBTC","ONTBTC","REEFBTC","BTCBRL","RVNBTC","AAVEBTC","AERGOBTC","IOSTBTC","TKOBTC","BCDBTC","KMDBTC","NEOBTC","RSRBTC","HBARBTC","RENBTC","CTSIBTC","POWRBTC","TFUELBTC","MATICBTC","REPBTC","IDEXBTC","FETBTC","BANDBTC","PIVXBTC","LSKBTC","ALPHABTC","OCEANBTC","ARKBTC","BTCPAX","COTIBTC","STMXBTC","LOOMBTC","RDNBTC","ICXBTC","BTCSTBTC","STXBTC","ADXBTC","KAVABTC","HNTBTC","MANABTC","TCTBTC","WANBTC","BTCTUSD","CRVBTC","GLMBTC","SUPERBTC","ANKRBTC","ONGBTC","FTMBTC","FUNBTC","SANDBTC","DEGOBTC","KSMBTC","SNTBTC","EPSBTC","CELRBTC","HIVEBTC","NANOBTC","SUSHIBTC","PERLBTC","ARPABTC","FIOBTC","BNTBTC","PONDBTC","BQXBTC","DREPBTC","SNXBTC","AUDIOBTC","COMPBTC","GASBTC","ASTBTC","TRBBTC","ORNBTC","STORJBTC","DGBBTC","NULSBTC","DIABTC","TROYBTC","LITBTC","UTKBTC","SUNBTC","SFPBTC","OMBTC","CHRBTC","AKROBTC","AMBBTC","UMABTC","TVKBTC","BTCDAI","GTOBTC","XVSBTC","DATABTC","POLYBTC","AGIBTC","NEBLBTC","DUSKBTC","PHBBTC","WTCBTC","AXSBTC","SCRTBTC","DOCKBTC","BELBTC","EVXBTC","NEARBTC","INJBTC","MTLBTC","QKCBTC","BTSBTC","ALICEBTC","CKBBTC","SKYBTC","CVCBTC","GVTBTC","BTCBIDR","EASYBTC","DODOBTC","OGBTC","BZRXBTC","ANTBTC","LRCBTC","ZENBTC","FLMBTC","ROSEBTC","JSTBTC","SKLBTC","UNFIBTC","FRONTBTC","WINGBTC","PNTBTC","IOTXBTC","OXTBTC","STPTBTC","MKRBTC","BLZBTC","LTOBTC","STRAXBTC","NAVBTC","WABIBTC","RCNBTC","AUCTIONBTC","PPTBTC","COSBTC","RIFBTC","DCRBTC","SNGLSBTC","HARDBTC","VIDTBTC","OSTBTC","BTCNGN","VIBBTC","SYSBTC","RLCBTC","TWTBTC","PERPBTC","MDABTC","PSGBTC","GOBTC","DLTBTC","BALBTC","APPCBTC","AVABTC","WPRBTC","FXSBTC","NBSBTC","PHABTC","YFIIBTC","DNTBTC","BTCRUB","GXSBTC","AUTOBTC","NMRBTC","YOYOBTC","BADGERBTC","SNMBTC","CTKBTC","NASBTC","IRISBTC","TRUBTC","QSPBTC","PAXGBTC","OAXBTC","REQBTC","FIROBTC","BRDBTC","POABTC","CNDBTC","JUVBTC","QLCBTC","CELOBTC","MTHBTC","NXSBTC","WNXMBTC","CDTBTC","FISBTC","ASRBTC","CFXBTC","ATMBTC","ACMBTC","SUSDBTC","BTCUAH","BTCIDRT","RENBTCBTC","BTCZAR","BTCVAI"]
testsym = ["BTCUSDT","ETHUSDT","XRPUSDT","LINKUSDT","LTCUSDT","BCHUSDT","EOSUSDT","TRXUSDT","ADAUSDT","XTZUSDT","DOTUSDT","UNIUSDT","FILUSDT","ENJUSDT","MANAUSDT","SANDUSDT","CHZUSDT","KSMUSDT","AKROUSDT","VETUSDT","SUSHIUSDT","SOLUSDT","NEARUSDT","ATOMUSDT"]
wallet=[[]]

## ORDERS SAVE TO .CSV FILE
with open('wallet.csv', newline='') as f:
    reader = csv.reader(f)
    wallet = list(reader)
print(wallet)
reader = csv.DictReader(open("wallet.csv"))
file = open('wallet.csv', 'w+', newline ='')

## ORDERS SEND TO TELEGRAM
def telegram_bot_sendtext(bot_message):
    
    bot_token = '1600349290:' ## YOUR BOT TOKEN
    bot_chatID = '-1001431859947' ## YOUR TELEGRAM CHAT ID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

## EXAMPLE FUNCTION FOR INDICATOR TENKANSEN FROM ICHIMOKU CLOUDS
def tenkansen(high,low,i):
    calc_tenkan = (high[(1+i):(21+i)].max() + low[(1+i):(21+i)].min()) / 2
    return calc_tenkan

## TELEGRAM MESSAGES TEMPLATE
my_message = "LONG Signals Tarih: {} ".format(date.today()) + "\n" + emoji.emojize(':rocket:')+emoji.emojize(':rocket:')+emoji.emojize(':rocket:')
my_message2 = "SHORT Signals Tarih: {} ".format(date.today()) + "\n" +emoji.emojize(':bear:')+emoji.emojize(':bear:')+emoji.emojize(':bear:')

## CODE MAIN SECTION, SEARCH ALL PAIRS AND CHECK WITH INDICATORS
## I EMBEDDED SOME INDICATORS BELOW WITHOUT FUNCTION FOR EXAMPLE; SPANB FROM ICHIMOKU, WMA, MA
for sym in allsymbols:
   # print("Start analyzing " + sym)
    klines = client.get_historical_klines(sym, Client.KLINE_INTERVAL_4HOUR, "15 day ago UTC")
    klines.reverse()
    ohlcv = pd.DataFrame(klines)
    ohlcv.columns = ['open_time',
              'o', 'h', 'l', 'c', 'v',
              'close_time', 'qav', 'num_trades',
              'taker_base_vol', 'taker_quote_vol', 'ignore']
    coinprice_high = ohlcv["h"].astype(np.float)
    coinprice_low = ohlcv["l"].astype(np.float)
    coinprice_close = ohlcv["c"].astype(np.float)
    tenkansen_0 = tenkansen(coinprice_high,coinprice_low,0)
    tenkansen_1 = tenkansen(coinprice_high,coinprice_low,1)
    ##SPANB MATH. CALCULATIONS
    spanb_price = (float(ohlcv["h"][60:180].max()) + float(ohlcv["l"][60:180].min())) /2
    spanb_price_min1 = (float(ohlcv["h"][61:181].max()) + float(ohlcv["l"][61:181].min())) /2
    spanb_price_min2 = (float(ohlcv["h"][62:182].max()) + float(ohlcv["l"][62:182].min())) /2
    spanb_price_min3 = (float(ohlcv["h"][63:183].max()) + float(ohlcv["l"][63:183].min())) /2
    spanb_price_min4 = (float(ohlcv["h"][64:184].max()) + float(ohlcv["l"][64:184].min())) /2
    spanb_price_min5 = (float(ohlcv["h"][65:185].max()) + float(ohlcv["l"][65:185].min())) /2
    spanb_price_fut1 = (float(ohlcv["h"][59:179].max()) + float(ohlcv["l"][59:179].min())) /2
    spanb_price_fut2 = (float(ohlcv["h"][58:178].max()) + float(ohlcv["l"][58:178].min())) /2
    spanb_price_fut3 = (float(ohlcv["h"][57:177].max()) + float(ohlcv["l"][57:177].min())) /2
    spanb_price_fut4 = (float(ohlcv["h"][56:176].max()) + float(ohlcv["l"][56:176].min())) /2
    ##
    
    ## WMA MATH CALCULATIONS
    wmapri = ohlcv["c"].astype(np.float)
    wmapa = pd.Series(wmapri)
    d = []
    e = []
    f = []
    g = []
    h = []
    j = []
    for i in range(len(wmapri)):
        c = wmapri[(i):(i+3)]
        if(len(c)==3):
            a = (np.average(c, weights=[3, 2, 1]))
            d.append(a)
    
    for i in range(len(d)):
        c2 = d[(i):(i+5)]
        if(len(c2)==5):
            a2 = (np.average(c2, weights=[5,4,3, 2, 1]))
            e.append(a2)
    
    for i in range(len(e)):
        c3 = e[(i):(i+8)]
        if(len(c3)==8):
            a3 = (np.average(c3, weights=[8,7,6,5,4,3, 2, 1]))
            f.append(a3)
        
    for i in range(len(f)):
        c4 = f[(i):(i+13)]
        if(len(c4)==13):
            a4 = (np.average(c4, weights=[13,12,11,10,9,8,7,6,5,4,3, 2, 1]))
            g.append(a4)
            
    for i in range(len(g)):
        c5 = g[(i):(i+21)]
        if(len(c5)==21):
            a5 = (np.average(c5, weights=[21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3, 2, 1]))
            h.append(a5) 
            
    for i in range(len(h)):
        c6 = h[(i):(i+34)]
        if(len(c6)==34):
            a6 = (np.average(c6, weights=[34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3, 2, 1]))
            j.append(a6)
    ###
    ###wma 21-42-84
    ma1 = []
    ma2 = []
    ma3 = []
    for i in range(len(wmapri)):
        c = wmapri[(i):(i+21)]
        if(len(c)==21):
            helper1 = (np.average(c, weights=[21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3, 2, 1]))
            ma1.append(helper1)
    
    for i in range(len(wmapri)):
        c = wmapri[(i):(i+42)]
        if(len(c)==42):
            helper2 = (np.average(c, weights=[42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]))
            ma2.append(helper2)
    
    for i in range(len(wmapri)):
        c = wmapri[(i):(i+84)]
        if(len(c)==84):
            helper3 = (np.average(c, weights=[84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]))
            ma3.append(helper3)
    

   # print(wmapri[0])
    print(sym)
    ##CONDITIONS
    if(spanb_price == spanb_price_min1 and spanb_price_min2 == spanb_price_min3 and spanb_price == spanb_price_fut1 and spanb_price_fut1 == spanb_price_fut2 ):
        if((float(ohlcv["c"][0]) > spanb_price and float(ohlcv["c"][1]) < spanb_price) and (wmapri[0]>j[1]) ):
            print("kademe1")
            wallet.append([sym+","+ohlcv["c"][0]+",Kademe1"])
            print(sym + ohlcv["c"][0])
            my_message = my_message + "\nSpanB  + WMA Level 1: {} ".format(ohlcv["c"][0]) + sym + " BUY"
       #elif((float(ohlcv["c"][0]) > spanb_price and float(ohlcv["c"][2]) < spanb_price) and (wmapri[0]>j[1]) ):
       #    print("kademe2")
       #    wallet.append([sym+","+ohlcv["c"][0]+",Level2"])
       #    print(sym + ohlcv["c"][0])
       #    my_message = my_message + "\nSpanB  + WMA Level 2: {} ".format(ohlcv["c"][0]) + sym + " BUY"
       #elif((float(ohlcv["c"][0]) > spanb_price and float(ohlcv["c"][3]) < spanb_price) and (wmapri[0]>j[1]) ):
       #    print("kademe3")
       #    wallet.append([sym+","+ohlcv["c"][0]+",Level3"])
       #    print(sym + ohlcv["c"][0])
       #    my_message = my_message + "\nSpanB  + WMA Level 3: {} ".format(ohlcv["c"][0]) + sym + " BUY"
       #elif((float(ohlcv["c"][0]) > spanb_price and float(ohlcv["c"][4]) < spanb_price) and (wmapri[0]>j[1]) ):
       #    print("kademe4")
       #    wallet.append([sym+","+ohlcv["c"][0]+",Level4"])
       #    print(sym + ohlcv["c"][0])
       #    my_message = my_message + "\nSpanB  + WMA Level 4: {} ".format(ohlcv["c"][0]) + sym + " BUY"
    if((wmapri[1]>j[2]) and (wmapri[2]<j[3]) and (wmapri[0]>j[1]) and (float(ohlcv["o"][0]) < float(ohlcv["c"][0]))):
        print("kademe5")
        wallet.append([sym+","+ohlcv["c"][0]+",Level5"])
        print(sym + ohlcv["c"][0])
        my_message = my_message + "\nWMA Kademe 5: {} ".format(ohlcv["c"][0]) + sym + " BUY " + emoji.emojize(':thumbs_up:')
        print(j[1])
    if(wmapri[0]<j[1] and wmapri[1]>j[2]):
        wallet.append([sym+","+ohlcv["c"][0]+",Level6"])
        my_message2 = my_message2 + "\nWMA Level 6: {} ".format(ohlcv["c"][0]) + sym + " SELL " + emoji.emojize(':thumbs_down:')
    if(wmapri[0]<j[0] and wmapri[0]<j[1] and wmapri[1]>j[2] ):
        my_message2 = my_message2 + "\nWMA Level 7: {} ".format(ohlcv["c"][0]) + sym + " SELL " + emoji.emojize(':thumbs_down:')
        
    if(tenkansen_0<wmapri[0] and tenkansen_1>wmapri[1] and wmapri[0]>j[0]):
        my_message = my_message + "\nTenkansen Possible BUY: {} ".format(ohlcv["c"][0]) + sym + " BUY " + emoji.emojize(':thumbs_up:')
        print("tenkansen")
        print(sym)
        
    if(ma2[2]<ma3[2] and ma2[1]>ma3[1]):
        my_message = my_message + "\nMA Possible BUY : {} ".format(ohlcv["c"][0]) + sym + " BUY " + emoji.emojize(':thumbs_up:')
print(wallet)
with file:    
    write = csv.writer(file)
    write.writerows(wallet)  
    
telegram_bot_sendtext(my_message)
telegram_bot_sendtext(my_message2)
    
