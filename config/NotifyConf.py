# -*- coding: utf-8 -*-


import TickerConfig
from work_wechat import WorkWeChat, MsgType, TextCard


def sendNotify(msg):
    """
    pushBear微信通知
    :param str: 通知内容 content
    :return:
    """
    if (
        TickerConfig.NOTIFY_CONF["is_enable"]
    ):
        try:
            wechat = WorkWeChat(
                corpid=TickerConfig.NOTIFY_CONF["CORP_ID"],
                corpsecret=TickerConfig.NOTIFY_CONF["CORP_SECRET"],
            )

            wechat.message_send(
                agentid=TickerConfig.NOTIFY_CONF["AGENT_ID"],
                msgtype=MsgType.TEXTCARD,
                touser=('@all',),
                textcard=TextCard(
                    title='购票成功',
                    description=(
                        f'<div class="highlight">{msg}</div>'
                    ),
                )
            )
            print(u"已下发 企业微信 应用通知, 请查收")
        except Exception as e:
            print(u"企业微信 配置有误 {}".format(e))


if __name__ == "__main__":
    sendNotify(1)
