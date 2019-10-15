import os
import argparse
from linebot import LineBotApi
from linebot.models import TextSendMessage

def parse_args():
    token = os.getenv("LINE_TOKEN")
    uid = os.getenv("LINE_UID")

    parser = argparse.ArgumentParser(description="LINE Pusher")
    parser.add_argument('msg', help="message to push")
    if not token:
        parser.add_argument('token', help="line channel access token")
    else:
        parser.add_argument('--token', default=token, help="line channel access token")
    if not uid:
        parser.add_argument('user_id', help="line user id")
    else:
        parser.add_argument('--user_id', default=uid, help="line user id")

    args = parser.parse_args()
    return args

args = parse_args()

line_bot_api = LineBotApi(args.token)
line_bot_api.push_message(args.user_id, TextSendMessage(text=args.msg))
