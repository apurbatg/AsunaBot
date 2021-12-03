from TGNRobot.mongo import db
from typing import Dict, List, Union


coupledb = db.couple
nsfwdb = db.nsfw


# Couple Chooser

async def _get_lovers(chat_id: int):
    lovers = coupledb.find_one({"chat_id": chat_id})
    if lovers:
        lovers = lovers["couple"]
    else:
        lovers = {}
    return lovers


async def get_couple(chat_id: int, date: str):
    lovers = await _get_lovers(chat_id)
    if date in lovers:
        return lovers[date]
    else:
        return False


async def save_couple(chat_id: int, date: str, couple: dict):
    lovers = await _get_lovers(chat_id)
    lovers[date] = couple
    await coupledb.update_one(
        {"chat_id": chat_id},
        {
            "$set": {
                "couple": lovers
            }
        },
        upsert=True
    

    

async def is_nsfw_on(chat_id: int) -> bool:
    chat = nsfwdb.find_one({"chat_id": chat_id})
    if not chat:
        return True
    return False

async def nsfw_on(chat_id: int):
    is_nsfw = is_nsfw_on(chat_id)
    if is_nsfw:
        return
    return nsfwdb.delete_one({"chat_id": chat_id})


async def nsfw_off(chat_id: int):
    is_nsfw = is_nsfw_on(chat_id)
    if not is_nsfw:
        return
    return nsfwdb.insert_one({"chat_id": chat_id})


async def is_served_chat(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True
 )
        )
