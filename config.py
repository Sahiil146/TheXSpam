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


SESSION2 = getenv("SESSION2", "AQCsWG47GS9MRFcHHElt4vgcVt3ljeTAikcVdyTPfiUMXVX_kYXIZj8IxVeRXWnnGqOdg0O6mGQOVr3nGpyPiavLy58I_7mNz-nlPLASVeIsKefPEt2y5GQaRzO0CIQpiS688AtB3m54a8iu9wcgMlgk_LJ3lBVKQJ4xFbwK9BSLgsV_XmnQY7orL1QmS65nqgpstlfkheslojzoNufGq3YfiRhsVo9iexrFlWModEckJq-NjVs_wDexwHfIhktQN6KXByJQnd72CKxi3PtlZ_3KNcdkl2jAfwxNAo7Ht3MHL4BbtGETzOvLvicoxAbe9mfWvLMpXaK-toCwzB1ebp0CAAAAAUnxbIMA")
SESSION3 = getenv("SESSION3", "AQCRlzePrq7KdlWp8ne0y4ZWZy9ruTUvZXiHkdPrD2ydZwscIqowJzkukc85WMnHDgPvxd4b0XPnhONvMmg7iCAvKt7HHGmmwlJTDL51Z-BpgOc60kJHy-vklMza2Flexc28_6G0GvlaCdRvxVvg9hp_-Q2g9Igetzu0Gx1ekxfNEY4nhgUdvBhK82KLDVC5srewBa8TdSoWQ9huRQzyf97MptxRVuPRqvdcmb3rh15u19-t3uV50YGVx_ZUt8cfcSibGA1otdaWb_LvjmgHulwxvbV6uqd-4rWsxK8ww0SZLtXVQHHrQlEU-QuPkRIKq3SjZtOHUp7OElhdciL1Upr4AAAAAVAvfSkA")
SESSION4 = getenv("SESSION4", "AQAmOsAFaoii6PmSgbYoUMbacvbi3bYhCroTD5enbFHo7IuN6pdEGodrlxhozNLR7LTAHJcmEpeg-Y7HnWeLxdt5wpfHB3a731DpBwI7CjSaWQTwiD7B5nQZuIuPi-WLyRQlx8n7l2NBIvr-MV0benUvyHzEBwYNGpOnnMYPfYizkMSX7vrvGPphZ9dM81qRwD2s6eMo9P1HKVUv7Z-vnzoxBKj1WYfAdz8uWPBuGBmsxUhBuBza-c-85gD8nKwDzgV3GCraNYfH1JnlvQjX2O1Kc92MJVTv_WGKLScajf00eABFBpHX6TMKHng_f_8HLOTesgZ72tmfn2uP5QsPpyppAAAAAVc2yooA")
SESSION5 = getenv("SESSION5", "AQBG5KV6_tqFBftuAfUKHp2Oq5D8FfjiLpUnZTacr1qbikxxt9LoP8DniK891ENgzh9i7zEYQVUJMLBNmHkNuaZ1XI81ocwkrK4NEObecYTu2CXZFV_Z7xyEsj6aPflFStWNUF1Ldom-ZnYii7DEQ9VwYnhfcqHUQgH5QOHDE2nYG6GvTMvSALTf2llxcK9URP4Ow9fxqRIVX4SNWtIzer4Ehtn-eFoTsoDq7Wu1vH7nfK5342eOavQmJknH3DJYTwpwZwpsCTCXcT6FD_uX9xWbNnXNkaFs0B1pKOikzLrZGSqAD7Y8epqhaO8ibZEeBTFOxxWCaZUe72Abby543pCcAAAAAWC6jRQA")
SESSION6 = getenv("SESSION6", "AQBumo4iGpNL2vBoifD6dyClGHcrYXwarJU3S9eOO3hGxS4hYm4tbYwGwgo1pnN-gcQBtHE_GXyh3TAjxq5oXDsjDBARTeyJTNxkcMC3JXIGHRFVk690HWxGDvowlMXt57uYJxclPyfUeiOXfZzIlJGzQu_gsvttg3Jhu_UTpSITQNG4v3um5-Sg65urnr982MjfU0WwptL7S0QHqrW3llF_Nq4BbA6UGwjVgR0dZa5fHKEhj7JkboWKYa2lRxiqk-iKTJ3VhiIoL2a0FYe8d7E0ilJu08UWWfR_cPOe3wFKiYfK1WSC05D3nKd8PnlTyTatY9757hgwBYab3YDkprL3AAAAAVwSvy0A")
SESSION7 = getenv("SESSION7", "AQCDIrL99w8nSedpOO-uAnNuI_tuSlclysDH1Fem5hIbbDKsLcGCo8WZMPXxPOs2m3IsspI0--S0lGJORYEND0bPbSIhFKHxpswBh8H6qcFl1mnyVuMgy3WT8M6S-io_UFqL12liIxTqDWUUmppbuhRd6gMLS1TWrhpU_MfPkAzJ-JR4OieOT3hokLxtYBFuCyYWC5xcBWipMZPVVZzJ2g2U9kzdV3mezsF3JUHFa7OwwiS2UhFjipnUlypYs9eJm9k6jPxUXTE_5Ey9yH7RAcWng8alJC9d48cPNITayHJhamqE-Vz-vv2zEwtnDfvB4SZONHZKSUNmG-17aFLqn3n1AAAAAS63msEA")
SESSION8 = getenv("SESSION8", "AQBb30yEjwDbsDkibwv27YMK0XL_hPI82fSl6z5w7pdWhtr2uUTtQueKSpeWG5pTk4V2pCS7ROeYf52JmozRDS5Sercy0Yrcf_VmxO73jKTLayoAnOVy7GxQ5yMjxDmMM451UeqwxgAmcYD6Bmiq2gQGDVURAOmK51_BV6shb_jCifn2GbuyyvsEqLgB_NNEBgovwzOc7151w0vvfyJfrpp-IQ0m5QydMEpHlcL6Ib31HVS6b2JoZChh5GbshD4LuhWuV1CScsDb6M8XlxWkcy7IXBGlGoYAPeLIb7Y5hMwhXE5GZgKt11Laz96K6_fByxeC3hZE-rAYZZuSEt2c5N0MAAAAAVw4fX8A")
SESSION9 = getenv("SESSION9", "AQCDOkcMLqTFfqEnING70EqUHYxRabY6d_1Oqu_P-vlNDdlyV6QRSuyHHp5n5H39uiErWjbrkahYhXaWWcDMi5EWHzv70lq5-K_GgeLLJxXtGzBhBlgJ75GhI4CmPjLQTgyjN1DdEYtiEW-bc1qTWponLiA7BuAFUYoIYmN8BCyJzB9jQeb-QRFtEVJzBld93iIMR482DZ8OwpLwWFT8H6xCRqGlGkFrQr7HH9_SMpIZ39cC883mc8h2ra9V8cNglpHeeo9Caty4m6RnOmc-iV-Oyn1ziMte_Co6W0VS-SqEYTDydGtH6WvXb1Nrl-sBZznkdkQKgfN7rA_h3IS39XwvAAAAAUZpN4kA")
SESSION10 = getenv("SESSION10", "AQASnvLMr00gaVYji5n3ZSFy8L_NT5sSCJzjkc7twdsypHmwcjATmxSLvq31xR3S8NKC4vc01ExNQ7VwvizLOyfHOSoMtgutWKBuih0o3lLZwJRBOVEk4qaBLQJEBwgxKvM09pCuoWHj0xsCfpguW5QVJAC6PfhMbMvFZoOhMerg1cm34Ud7LQ7pdIeQjORwyN5a8lLa4TTxQFiJa1o969cb3N5Igx_GZNys3JJCwZm5-2wRf_BeLnajbcOu6eihj-a4DOTDr4vQi4UggMtSgf1A5cqWxmpTSbGYKMmwtkZadFoRAO5iKmd0pXIMNY30dedSu0tCYEtQPIfq2NgjvNgEeB8yOwA")


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
