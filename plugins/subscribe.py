#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @VysakhTG

from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest
from info import ADMINS, AUTH_CHANNEL
from database.users_chats_db import db 


@Client.on_chat_join_request(filters.chat(AUTH_CHANNEL))
async def join_reqs(client, join_req: ChatJoinRequest):
    user_id = join_req.from_user.id
    first_name = join_req.from_user.first_name
    username = join_req.from_user.username
    date = join_req.date
    await db.add_req(
        user_id=user_id,
        first_name=first_name,
        username=username,
        date=date
        )
