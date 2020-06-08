import requests
import time
import json
import pandas as pd
import numpy as np
from pandas import DataFrame

id_dict = {"12484":"HEX","12710":"Forsage-Smartway","12947":"EASY-CLUB","11762":"Bitrearer","12936":"EcoSmartECS","12055":"MillionMoney","12587":"DoubleWay","11352":"Bank-of-TRON-BTT","13079":"EtherStake-Business","13141":"GIDAAI","12072":"CryptoFriends","12922":"Ethrun","12965":"Billion-Money","12694":"Fomo5k","13143":"BinaryTop","11552":"CryptoHands","11553":"Onigiri-Bank","12991":"ETHBULL","12682":"BeeHive-Fast","12816":"BULLRUN-30","12895":"Crypto-Life","13063":"ETHERKING","12900":"Ethernity-Money","13160":"NEXUS","13087":"AdsEarnETH","13089":"Bullrun4","13090":"Bullrun-v4","13088":"ETH50K","13133":"Zozo","12143":"Smartex","13138":"Coloron2","13075":"SaleChain","13164":"Speed-Bull-2","12673":"Absolutus","12855":"SETH%E8%B6%85%E7%BA%A7%E4%BB%A5%E5%A4%AA%E5%9D%8A","12056":"ShuffleMonster-V3","12581":"JUSTGAME","13163":"p2p","13149":"PartyCoin","13009":"Unixo","12733":"NGUYENPHUNHO","10402":"Gandhiji","12212":"PyraBank","12360":"CatPromotion","11622":"Topuppins","12741":"ETHERALIVE","13147":"Neuromancer-Network","12751":"ETHEREUMS%E2%80%A2CASH","12943":"EasyPool","12844":"MILLIONAIRE-VINE","13094":"Bullrun5","13140":"xoxov3","13036":"skyether","13142":"SpaceBullPro","12886":"etherpool","12995":"UltraSpace-Pool","12183":"Blue-Chip-Fund","12875":"poolvine","12969":"tigersline","12869":"Tiger-Cash","13165":"Fennix-Smart-Contract","13131":"Bullrun-Network","13095":"BullRun-V8-Gold","12542":"Etherlly","12384":"Diamond-Dividends","12675":"Etrix","13070":"TTMINE","12778":"ETHERA%E2%80%A2UK","12167":"%E5%A4%A7%E5%AF%8C%E7%BF%81","12944":"elephantluckcash","11672":"Space-Miners","1246":"CryptoHoma","171":"PoWH-3D","11217":"Xdapp-EOS","12806":"LamboFunds","12568":"TronDash-TRX-Bank","12523":"Dapp-Investor","830":"Fomo3D","12188":"King-Token-KGT","11472":"Gako-Binary-Option","12414":"EtherHives","12829":"DeFiGroupch-TRON","11904":"Lucky-Network","11386":"TronFund","10367":"P3TNETWORKclosed","11277":"TCH5","12670":"Ovirus","12351":"TronLoot","11266":"Tron-Double-Doo","11257":"Tronopoly","11027":"Tron-Double","12424":"8therBank","1381":"333-EOS","11108":"TronWorlds","11275":"TronDeposit-TD3D-NEW","12803":"Sports-AI","11108":"TronWorlds","12220":"DeFi-20","11974":"Libra-TRON","10170":"Mizhen-Game","12803":"Sports-AI","1250":"EthProfitio","12440":"Hyip-Dapp-Pool","11006":"[TRON]invest","11073":"Tron777","11595":"EOS100ROI","10362":"Bribery","13050":"STONK-SIMULATOR","10041":"TotalMoney","12566":"HolidayGiftBox","12763":"NTS-Crypto-Deposit","10343":"ETHedge","1238":"Nasdaq","12990":"Ether-Magic","1293":"Dponzi","11585":"TronPond","11164":"TronHeist","11095":"%E5%8C%BA%E5%9D%97%E4%BF%A1%E4%BB%B0%E5%9B%BE","13157":"H3X","11916":"TRON-VENDING","10649":"FirstWinner","11063":"Slugroad","10625":"Crypto-Skyscraper","12545":"CryptoTomatoes","1280":"MagicX","10896":"ETHUP","11691":"Morrex","10054":"Efirica","11325":"0xowns-art","11468":"Tron666","12554":"Send-Me-Tron","11481":"Blockvest","12547":"RED-BOX-DAPP","11179":"77Tronnetwork","10813":"Mega-Blockchain-FOMO-Tron","11690":"BTT-BitTorrent-P3B-Exchange","12664":"Drones","12724":"TRXLAND%C2%A9-2020","12201":"Ships","1338":"Smart-Pyramid","1275":"apexONE","12669":"Moriarty","13068":"TronCats","10638":"Thetronnutclub","11122":"MegaTron","10370":"Temple-Of-Tron","12970":"DeckPot","12225":"TronFomo","12054":"ZOO","1162":"Lucky7","13081":"Arcadium-D1VS","10152":"Invither","10398":"Tron-Trump-Wall","11280":"Tronix","11002":"Smart-Investments","1374":"Miner-Token-Online","12172":"EosFairWin","12065":"tronsnap","12628":"TronBot","12447":"IOSTPassive","11404":"SafeMath","1136":"Ether-Game","10053":"EasyLevel","12461":"Fish-n'-Chips","12149":"FairWin","12198":"RED-CHIP-FUND","10346":"mlmeth","1458":"5inv","12630":"BBC-TOKEN","10014":"Stock-Exchange","10164":"Ternary","10363":"Tron-Garden","11318":"TronInvest","11432":"SnailTroi","10631":"Tron-Village","12552":"SafeFund","12389":"EthHashing","11902":"BOXME","1377":"Riveth","1382":"MyDice","12001":"P3B-Shrimp-Farmverified","10812":"NTA3D","1315":"Ethernity5","1205":"LootEther","10280":"5ETH","1311":"Green-Ethereus","12764":"Perodium-Dividends","10409":"Farm-Farm","11652":"UniTron","11203":"Tron-Double-BTT","1215":"Leprechaun","11274":"TRXFLY","10280":"5ETH","12764":"Perodium-Dividends","11652":"UniTron","1278":"255ETH-Club","13161":"PyraBank-Hex2T","11250":"Tron4You","1215":"Leprechaun","11274":"TRXFLY","1456":"WCG","11358":"Tomo3D","12141":"Spacecans","1268":"EthLong","13129":"HEXRun-Multiply-your-HEX","1240":"Easy-Invest-6","11187":"P1G","11315":"IOSTROI","10121":"EasyOption","10543":"FreeEThereum","1153":"Easy-Invest","11907":"P3B-Exchange-BTT","1129":"3DayProfits","1462":"Fast10ETH","10262":"EOSTime","1200":"We-Cooperate-Growth","10537":"Tronkarp-Farm","12709":"oFund","1204":"Grandiose","1407":"Freera","12422":"DappKing","12580":"ADDI-TRON","10081":"Richer3D","11514":"TURBOETH","11562":"Uroborus","12619":"TronOilStation","10178":"Xworld","10297":"TRON-Shrimp-Farm","11243":"1H","12782":"STARTRON","11391":"TronRich-Banking-Lotto-Dice","10293":"Universal-Crypto-Token","1298":"RecordBreaker","12088":"RedLine","11245":"333ROI","1402":"iGuess-@-DappPub","10055":"The-HODL-Community","10596":"ETH-FORTNITE","11186":"Stockpile","10568":"TRON-SHRIMP-3D"}
dict_len = len(id_dict)
null = ""
false = False

def save2df(r, row_list):
    r_dict = eval(r)
    contract_list = []
    for contract in r_dict["contracts"]:
        contract_list.append(contract["address"])

    temp_list = [r_dict["id"], r_dict["title"], r_dict["platform"], r_dict["category"], r_dict["publish_date"], contract_list]
    row_list.append(temp_list)
    return

def ScrapeData(dict, save_path):
        i = 1
        e = 0
        row_list = []
        
        for key in dict:
                randsleep = np.random.randint(low = 1, high = 3, size = 1)
                time.sleep(randsleep)

                headers = {
                    "Accept": "application/json, text/plain, */*",
                    "Referer": "https://dapp.review/dapp/614/Mega-Crypto-Polis-ETH",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
                }
                try:
                        r = requests.get('https://dapp.review/api/dapp/' + key, headers = headers).text
                except:
                        print("connection error")
                        e += 1
                        continue

                try:
                        save2df(r, row_list)
                        print(f"{i}/{dict_len} DApp collected: {dict[key]}")
                        i = i + 1
                except:
                        print("error occurred.")
                        e = e + 1

        row_nparray = np.array(row_list)
        columns = ["id", "name", "platform", "cate", "publish_date", "contract"]
        df = pd.DataFrame(data = row_nparray, index = None, columns= columns)
        df.to_csv(save_path)
        print(f"{i} files scrapped, {e} failed.")

if __name__ == '__main__':
        ScrapeData(id_dict, './eth_highrisk.csv')

