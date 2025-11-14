# -*- coding: utf-8 -*-
import os
import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import GroupMessage
from plugins import dice_sum, spell_search, states

test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()


class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")


    #判断是否正确加载低阶法表
    spell_search.initcheck()
    states.initcheck()
    #法表功能测试
    #spell_search.SearchSpellList('羽落术')

    async def on_group_at_message_create(self, message: GroupMessage):
        msg = message.content.strip()
        member_openid = message.author.member_openid
        print("[Info] bot 收到消息：" + message.content)
        if msg == f"你好":
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=f"你好，给你两刀")
        elif msg == f"李苗正青":
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=f"你好，我喜欢你，哇奥！！！！")
        elif msg == f"检定":
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=f"最终检定值 = D20 + 对应调整值 + 熟练加值（若有对应熟练项）")
        elif msg.startswith("/d"):
            msgs = msg.split()
            print(msgs)
            if len(msgs) > 2:
                resultmsg = "格式有错误哦，尝试例如“/d4 2”这样的形式"
            elif len(msgs) == 1:
                resultmsg = dice_sum.DiceSum(msgs[0], "1")
            else:
                resultmsg = dice_sum.DiceSum(msgs[0], msgs[1])
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=resultmsg)
        elif msg.startswith("/spell"):
            msgs = msg.split()
            resultmsg = spell_search.SearchSpellList(msgs[1])
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=resultmsg)
        elif msg.startswith("/state"):
            msgs = msg.split()
            resultmsg = states.SearchStateList(msgs[1])
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=resultmsg)
        else:
            print("Normal")
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=f"丢骰子要点进头像里扔哦")

        _log.info(messageResult)


if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_messages=True)
    client = MyClient(intents=intents, is_sandbox=True)
    client.run(appid=test_config["appid"], secret=test_config["secret"])