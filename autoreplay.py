#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2017/10/23'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

# # 自动回复
# # 封装好的装饰器，当接收到的消息是Text，即文字消息
# @itchat.msg_register(['Text','Picture','Card','Sharing','Map'],isFriendChat=True,isGroupChat=True,isMpChat=True)
# #这个装饰器还有一个参数 就是text_replay 的函数名，   msg_register函数 是一个闭包函数，里面还有一个_msg_register()函数
# def text_reply(msg):
#     # 当消息不是由自己发出的时候
#     print msg
#     '''
#     msg  text消息类型 格式： 王侨  发送给梅梅的
#     {   u'AppInfo': {u'Type': 0, u'AppID': u''}, u'ImgWidth': 0,
#         u'FromUserName': u'@83669c0e3a6e16de5daa1a999ddbaff6789e16604eee31a0dcaa4d6780b2f2b1', 王侨的微信名
#         u'PlayLength': 0, u'OriContent': u'', u'ImgStatus': 1,
# 发送方信息 u'RecommendInfo': {u'UserName': u'', u'Province': u'', u'City': u'', u'Scene': 0,
#         u'QQNum': 0, u'Content': u'', u'Alias': u'', u'OpCode': 0, u'Signature': u'', u'Ticket': u'',
#         u'Sex': 0, u'NickName': u'', u'AttrStatus': 0, u'VerifyFlag': 0
#     },
#     u'Content': u'\u53d1\u6d88\u606f\u7ed9\u6211\u3002\u5b9d\u5b9d',传输的文本
#     u'MsgType'消息类型: 1, u'StatusNotifyUserName': u'', u'ImgHeight': 0,
#     u'StatusNotifyCode': 0, 'Type': 'Text', u'NewMsgId': 8813300164929485037L,
#     u'Status': 3, u'VoiceLength': 0, u'MediaId': u'', u'MsgId': u'8813300164929485037',
#     u'ToUserName': u'@f4869f0cb31ebeea576b0120d703fc89358bc739629c53bba08a22fb05428404',接收方  梅梅的微信号
#     u'ForwardFlag': 0, u'FileName'文件名  发送文件时用: u'', u'Url': u'', u'HasProductId': 0,
#
#     'User': 接收方信息  梅梅的信息
#     <   User:
#     {   u'UserName': u'@f4869f0cb31ebeea576b0120d703fc89358bc739629c53bba08a22fb05428404', 微信号
#         u'City': u'\u8d35\u9633'城市, u'DisplayName': u'', u'UniFriend': 0,
#         'MemberList': <ContactList: []>, u'PYQuanPin': u'meimei',微信昵称的拼音
#         u'RemarkPYInitial': u'BBDD'备注拼音的缩写 宝宝大大, u'Uin': 0, u'AppAccountFlag': 0,
#         u'VerifyFlag': 0, u'Province': u'\u8d35\u5dde'省份 贵州, u'KeyWord': u'',
#         u'RemarkName': u'\u5b9d\u5b9d\u5927\u5927'备注 宝宝大大, u'PYInitial': u'MM',昵称的拼音的首字母
#         u'ChatRoomId': 0, u'IsOwner': 0, u'HideInputBarFlag': 0,
#         u'EncryChatRoomId': u'', u'AttrStatus': 135269, u'SnsFlag': 17,
#         u'MemberCount': 0, u'OwnerUin': 0, u'Alias': u'',
#         u'Signature': u'\u4eba\u95f4\u56db\u6708\u5929'个性签名 人间四月天, u'ContactFlag': 2049,
#         u'NickName': u'\u6885\u6885'昵称 梅梅, u'RemarkPYQuanPin': u'baobaodada',备注的拼音
# 头像地址 u'HeadImgUrl': u'/cgi-bin/mmwebwx-bin/webwxgeticon?seq=637775806&username=@f4869f0cb31ebeea576b0120d703fc89358bc739629c53bba08a22fb05428404&skey=@crypt_14e41f7c_2a13332732b9f0b98508e8a087b1a9bf',
#         u'Sex': 2, u'StarFriend': 0, u'Statues': 0
#     }
#     >,
#     u'AppMsgType': 0, 'Text': u'\u53d1\u6d88\u606f\u7ed9\u6211\u3002\u5b9d\u5b9d'传输的文本,
#     u'Ticket': u'', u'FileSize': u'', u'CreateTime': 1508853455消息发送的时间, u'SubMsgType': 0
#
#     }
#
#
#     '''
#     if  not msg['FromUserName'] == myUserName:
#         # 发送一条提示给文件助手
#         if msg['Text']:
#             itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
#                             (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
#                              msg['User']['NickName'],
#                              msg['Text']), 'filehelper')
#             # 回复给好友
#             #return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])
#         if msg['Picture']:
#             itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
#                             (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
#                              msg['User']['NickName'],
#                              msg['Picture']), 'filehelper')
#             # 回复给好友
#             #return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Picture'])
#         if msg['Card']:
#             itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
#                             (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
#                              msg['User']['NickName'],
#                              msg['Card']), 'filehelper')
#             # 回复给好友
#             #return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Card'])
#         if msg['Sharing']:
#             itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
#                             (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
#                              msg['User']['NickName'],
#                              msg['Sharing']), 'filehelper')
#             # 回复给好友
#             #return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Sharing'])
#         if msg['Map']:
#             itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
#                             (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
#                              msg['User']['NickName'],
#                              msg['Map']), 'filehelper')
#             # 回复给好友
#             #return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Map'])


import itchat, time
from itchat.content import *

import threading

import itchat_getnews

function_stop_flag = False
auto_replay = False
def function_stop():

    #朋友私聊  文本消息  下载的文本信息
    @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
    def text_reply(msg):
        global auto_replay
        if not auto_replay:
            #print type(msg)

            if msg.FromUserName !=myUserName:
                if msg.text == u'关闭':
                    global function_stop_flag
                    function_stop_flag = True
                    print u'自动回复将关闭两分钟,你发送完消息，请您输入开启回复助手，我将不胜感激'
                    #return u'自动回复将关闭两分钟,你发送完消息，请您输入开启回复助手，我将不胜感激'
                    time.sleep(120)
                    itchat.send('%s: %s' % (msg.type, msg.text),toUserName = 'filehelper')
                elif msg.text == u'退出':
                    global done
                    done = False
                elif msg.text == u'机器人':
                    #global robot_replay
                    auto_replay = True

                else:
                    itchat.send('%s: %s' % (msg.type, msg.text),toUserName = 'filehelper')
                    print u'已收到你的消息，可以输入“关闭”关闭自动回复，输入“机器人”和图灵机器人聊天'
                    #return u'已收到你的消息，可以输入“关闭”关闭自动回复，输入“机器人”和图灵机器人聊天'
        else:
            if msg.text != u'滚蛋':

                r=itchat_getnews.tuling(msg.text)

                itchat.send('%s'%r,toUserName = 'filehelper')
                #print u'如果你不想看到我，可以输入“关闭”来关闭我两分钟，您发的消息我依然会发送给我的主人,消息为 %s' % (msg.text)
                defultreplay = u'我收到了你的消息'+msg['Text']+u'（出现我就说明机器人出现了一点问题，需要修复一下......）'
                return r or defultreplay
            else:
                #global robot
                auto_replay = False
                itchat.send(u'已经退出机器人聊天',toUserName = 'filehelper')

    @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
    def download_files(msg):
        if msg.FromUserName != myUserName:
            msg.download(msg.fileName)
            typeSymbol = {
                PICTURE: 'img',
                VIDEO: 'vid', }.get(msg.type, 'fil')
            itchat.send('@%s@%s' % (typeSymbol, msg.fileName),toUserName='filehelper')
            #return u'如果你不想看到我，可以输入“关闭”来关闭我两分钟，您发的消息我依然会发送给我的主人@%s@%s' % (typeSymbol, msg.fileName)


#群聊  文本消息  需要下载的文本消息
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=True)
def text_reply(msg):
    print msg
    # print msg.NickName
    print msg.actualNickName
    print msg.text
    if msg.isAt:
        itchat.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text),toUserName = 'filehelper')
        return u'我现在有事，已经收到你的消息： %s 待会回复你。' % msg.text

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def download_reply(msg):
    print msg.actualNickName
    print msg.text
    if msg.isAt:
        msg.download(msg.fileName)
        typeSymbol = {
            PICTURE: 'img',
            VIDEO: 'vid', }.get(msg.type, 'fil')
        itchat.send('@%s@%s' % (typeSymbol, msg.fileName),toUserName='filehelper')
        #return '@%s@%s' % (typeSymbol, msg.fileName)
#公众号 回复
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING],isMpChat = True)
def text_replay(msg):
    itchat.send('%s: %s' % (msg.type, msg.text),toUserName = 'filehelper')







#新的朋友自动添加
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    # username = itchat.get_friends(update= True)[0]
    # print username
    threading._start_new_thread(itchat.run,()) #生成一个线程，run函数一直运行，监测消息的输入，调用msg.register，
    done = True
    while done: #主进程
        if not function_stop_flag:
            function_stop()
            time.sleep(1)

        else:
            @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
            def text_reply(msg):
                if msg.text == u'开启':
                    global function_stop_flag
                    function_stop_flag = False
                    print u'自动回复已开启'

    '''
    {'UserName': u'@162c5d8f616948211725eb3a75c2cd67ff5ceed7b3a674946372b23bf8b9a544', 微信号
    'City': '', 'DisplayName': '', 'UniFriend': 0, 'OwnerUin': 0,
    'MemberList': <ContactList: []>, 'PYQuanPin': u'', 'RemarkPYInitial': u'',
    'Uin': 2019033710, 'AppAccountFlag': 0, 'VerifyFlag': 0, 'Province': '', 'KeyWord': '',
    'RemarkName': u'', 'PYInitial': u'', 'ChatRoomId': 0, 'HideInputBarFlag': 0, u'HeadImgFlag': 1,头像标志  为1表示有头像
    'EncryChatRoomId': '', 'AttrStatus': 0, 'SnsFlag': 17, 'MemberCount': 0, u'WebWxPluginSwitch': 0,
    'Alias': '', 'Signature': u'\u5f31\u6c34\u4e09\u5343\uff0c\u53ea\u53d6\u4e00\u74e2\u996e',个性签名
    'ContactFlag': 0, 'NickName': u'\u738b\u4fa8'昵称，           'RemarkPYQuanPin': u'',备注名称
    'HeadImgUrl'头像地址: u'/cgi-bin/mmwebwx-bin/webwxgeticon?seq=2116950377&username=@162c5d8f616948211725eb3a75c2cd67ff5ceed7b3a674946372b23bf8b9a544&skey=@crypt_14e41f7c_8c07b30f72c164d85d09664ab5104fc5',
    'Sex': 1,性别 1为男   2为女      'StarFriend  ': 0, 'Statues': 0}

    '''