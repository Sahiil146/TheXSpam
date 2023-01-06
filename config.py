import logging
import aiohttp
import os
from TheXSpam import OWNERS
from TheXSpam import *
from os import getenv
from pyrogram import Client
from pyrogram.types import *


logging.basicConfig(level=logging.WARNING)


#----------------------------------- REQUIRED CODES --------------------------------------#


API_ID = int(getenv("API_ID", "22939641"))

API_HASH = getenv("API_HASH", "8854a48ffd429bd794e070a4d1c12be7")

SESSION = getenv("SESSION", "AQAvFDt0AvXf63cbfn_3O8j2Nsc7bE_x54ZDvPKLdO5_Qid1H41dU0ZxJU_98tW3ssjkXZo1PZ3GgmB0Y69wHHvcYgS0SJNHDngzWp7-60pjWxOzJTmmXDfPHPPnaeeBxoTupB3ZbeGWJNFl7T62Drv4sfR16PAzi4bLtOywUmr2GrQHOr6iHDfFFYmTZ6i9nbF7jVK4FdyPrNc0YP7RKgy4s-qKFgeN7YGY_CV9yBPbaYXmdOLrDs0C4yCBqRW2ptVF2en3wsxaP85rP4-ExsGx61QAF2twT0ZeVl79CbIDTVHoEgdoKIPngPGlpffRm_tnin4O39y2RDc6EeVF8IJcAAAAAUe6UtIA")

ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/9c2825a87007d1bee6647.jpg")

OWNER_ID = int(os.environ.get("OWNER_ID", "5659722901"))


#-------------------------------- OPTIONAL -------------------------------------#


SESSION2 = getenv("SESSION2", "BQBiMZkAroWGivV3h6TzVydcHWoxBmXZR_HCf2btzI5E7F9aYe7BkIJAiI229gbrjgeeidtTZevDUgkS9dnrS3sEDxlKhG74JtR_tqP6sLf6Qzi2xN_nspLyKNm6CC0QneyzZQVP2W7ou0P2nfaQ3bJ_3B3ODKoc_1mNat4PRvKtkdvDGVllwXl7NDgPXk18YfRvqivbGY2RaEFumLdScOxxFDPPScNqVkhWbzl9g3jocQAB5HlSL72-pHSGQdOPUvtE5bJvWEjJQ52Bn92W2z_Fi_zpOW_mrRXM0WtHB2YdGbKqt9HPZv--DpJiT8n3FqmfwyMEl6TH0LBcFsu4SnbiS9CgYwAAAAFefBhBAQ")
SESSION3 = getenv("SESSION3", "BQBiMZkAXFjh1-EQEE9KF_sp37ucK1_P4jrlcsJihflilvGceTZfh_E_s1Lg9QXtEzps1hlsJWt8qd9Qzp4KAmvl89OASYEl6i-PChKE2K4t6_NuvSy5J-gWq_H4wwbxfruQLRNU-R6LI5lPBbr9EKhnGSf8sio2WscifIUxnDqLjf1mkWnP1b6czphIuIjMZlOP6ygMp7-Cvyp4dZ5OGfpIkg4FrjWYvvUfdor0BH11vww9skfy5H8eM86u2XIZ-i_ZkAqOLI5FtBqZubBNaRl26Sas1kgh--izsLRhmcJ6VVEEv6HjRUfHS3ND2g1aNcZFXI-nQyESDt0Bz2u7dgciBMdNZwAAAAFfurZEAQ")
SESSION4 = getenv("SESSION4", "BQBiMZkACAkXew112o9N5r4IZyXLgoW-fx7IouAO7IksNI3rsTaGQj8UF8HAW9fGbLFJStJOzuIBcF6WJxw1SkICkb15zsf7id_Dmv6aIfM40KqaGI64ObulAwRXwWG1t8W9S5XqPq14CaloMz7X8Yc9KGB-R7-7JRbDf1a5hh8_0kjL15oBRd_74uorAWAzBSxu2mJ-ZeJYHhyYc7wXhk2K2GiFy80LG9N8MqS9JhtVmrO5GSWZ5q4azFgdEdcLNv41V4lWOu_is4RfMyVsB8I1cLJLT2fDFB6ROKHyjj_aRT7AN0OQbFztErClBhtkussPTM4309hCCII6ymrt14AcYfIDFAAAAAFhumkFAQ")
SESSION5 = getenv("SESSION5", "BQBiMZkAZovjKS9TYwXhppW4A-3vTMwJ-bRECo30UYfde2LjwCf_1eAWShPEdu6qgtCaWeglUh4CArje4UN2qjWYdETRrDJKSbYvYEu0vWr5QADbHG-eeP04sGKRV7AoypCTNgHCibzL4sq0gUasNrMS25BX-SFfo8Fpr3zm3ieMc_XZdd4jwnSD5jK2QQjkmP2om3e-weA0GbCQw92pDc63N6Q3fOnLxE90a7l2j_1XEgn1dEhhi1KlUtKCUfhcwtz_ZVDsfMKq8TMDN-V4oPZZXykkCm16w-d1QWfDs66GJ8JgvWnWKxxup1mUjzEqySY8DR7QVUzU2BEsQW6FaOZyXaZESAAAAAFVZ8I8AQ")
SESSION6 = getenv("SESSION6", "BQBiMZkAqko1MgtudptKPo-NxtgBuhAxGPoJhSELKHyvML14rfDosSdZpSO9op-Hj-t8ewPt3rwPpzVUhQVAiftrKeGm_mjfYX7Tz-O2clC_7nbkgkekVRosDU0G2pPH8SKTSGQDjMCatUZgGOD24SDCIUmVmRgbpLV0ToGFc0t5erzktUBqQUNrXXj3a4Yzr3k-BIpkbLZ-ijmKcIya-2lvGJyzl5ggmoXRQmeHVFrAMeqYGppX5ZrETI4YiTCA8ad4IvKUCL2AKGfMLw3K6DLKPhXbCd0eJ4XqDdYkAcV8Pjij8Kl1Ql7b-PAH6jXwX8X2C7xksxp4RjBkb_vqaGFll0n4MQAAAAFfSbvJAQ")
SESSION7 = getenv("SESSION7", "BQBiMZkAFkPA96b6M89FXZP6emk2dN3E6Jpudnx1Jj6DAh8MaBNogt4py_vl_ghY4Nv-x38wCl6prYH-6bRZaIxj-gHAlt4cSvepmVmFTWLLPYTrkIRwuhadxemc7CXO3l9UBMA93PulF9IvXXI4Hd30xMbtxq4P-0PUvtArokIHgfuSYK0fQvSoVbczBOFB8v0b6ntEGJqThV1TIuvVUtH08a3XEZZUcTKle-sSBC9xtZ_E-psu193iNnJYoOLk1dJxMpd4ehwkzw9NaSVjJ8AjxPUnpqhW7yd5yeHez8PST7H1xzekLfJVPb-bgL492Ph4h_uMfnMhNR2NbhGxhgMpgqa-VwAAAAFkF6pyAQ")
SESSION8 = getenv("SESSION8", "BQBiMZkAhcvmklTJYltMdOUz8G_D8mCIBlXMAx6E8wMEqS4jIW5NYHjQ0ASl_1WGQHUCX_gCaHv5DVgHL6dlII-OCWODLhXyj4UH-GoB4XyGJcxAg6Vmt8TaWH7Yi2dDALDunMT-6navhR3rg7_LpV1iDYQJ1Shf_fv9lFw_OaX9N2YdDTgboF7JExK4IFs5v-iG9nL47tLZUimxogNogwK-2Ku5mJlJbUQI5OGIukmqlEc44pI6LQrT17Yq_nILhu8MPHOGrAHvahIGQUCTXnzlZaGbX-hy1dS0C5NSdtZ5JNnaFd8D6hizZ-x3f8LH-HsfUVwU92F2g9pj2NVhDHk524JEiAAAAAFQfhCkAQ")
SESSION9 = getenv("SESSION9", "BQBiMZkAXSixIo1h8VDpQVmcefkMOcYbOlu0JY-YftaxO-Non5m9Ydon0mwjoY8V8x2tnWD_tPA_77RQmH8C-3jC8S1qjyFBVn5fQKSHag0i_Df_fab5Wpkyhx0SiWD2iOWB3eBE_Grr8wgt3kD9AMbwPWNfAwnZksX2gVLa1Mq8QrxM1P4rV59o8rpfJdjwZEAXHYHYE_vYHCz34OxH--RSJvLBk6AoPalxsRTenXPKXLJCidYU7q3d-JIybkLef6lRzkJpENLPQaXcSrsOJalml0b_SixOxwHnOg5UMpd-AMXlHK22lBz4YLAu4CQ8iQvwWqCON9AyXJtAqBGYnqFJK9ynQAAAAAFHRsqmAQ")
SESSION10 = getenv("SESSION10", "BQBiMZkAJyx-i_XItUwqKKAcnnm5vcFsbwqtYs3W6KfJ83vzca0G7fKr0f5Qtz8d_6kTActjKgzagef4nzFdhsUoSX_OnZEHn-hDXFUl8uaGzcXxzGbEwT3jV2obfaqAzk9hrRNs1KYfuvaxc31Fh_hSvBipaA71T0CsU5PveOWbcuaIYm55ETNV2bN3lFSBXjrHX40pFZDYxWHh4iKf7VTIaW6arjO_i5PV8a5sKE8_28kZbdNIzrVguED0jaJY2_s6Wac163cfNGu6DcFUJ18NlxTKyo8bQgnFUBGAuSSX_-ITCwShlUC-2zdxthrQ-iGqNkvmCFu4MDb1A0chc9N-xy1n2QAAAAFjsfroAQ")


#------------------------- CLIENTS -----------------------------#


if SESSION:
    client = Client(SESSION, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client = None

if SESSION2:
    client2 = Client(SESSION2, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client2 = None

if SESSION3:
    client3 = Client(SESSION3, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client3 = None

if SESSION4:
    client4 = Client(SESSION4, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client4 = None

if SESSION5:
    client5 = Client(SESSION5, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client5 = None

if SESSION6:
    client6 = Client(SESSION6, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client6 = None
        
if SESSION7:
    client7 = Client(SESSION7, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client7 = None

if SESSION8:
    client8 = Client(SESSION8, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client8 = None

if SESSION9:
    client9 = Client(SESSION9, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client9 = None

if SESSION10:
    client10 = Client(SESSION10, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client10 = None


#----------------------------- DON'T MESS ------------------------------#


aiohttpsession = aiohttp.ClientSession()

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

sudo = os.getenv("SUDO_USERS")
SUDO_USERS = []

if sudo:
    SUDO_USERS = make_int(sudo)

for x in OWNERS:
    SUDO_USERS.append(x)
    SUDO_USERS.append(OWNER_ID)
