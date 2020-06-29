#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re
import random
import string
import json
from lxml import html
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

def wechat(message):#给微信发消息
        print(message)
        server = "https://sc.ftqq.com/SCU62807Td3777eaaf7aadda269b881670e4732275d8e8cfacbb04.send?text="+message
        requests.post(server)


# In[ ]:


headers={'User-Agent': 'api-client/1 com.douban.frodo/6.22.0(166) Android/28 product/HMA-L09 vendor/HUAWEI model/HMA-L09  rom/android  network/4G  platform/mobile',
         'Authorization': 'Bearer b81f4fc1614470df285def4423cd529d'}

groupurl='https://api.douban.com/v2/group/670255/topics'

key=['0df993c66c0c636e29ecbb5344252a4a','0b2bdeda43b5688921839c8ecb20399b']
apikey = '0b2bdeda43b5688921839c8ecb20399b'

words=[]#词库初始化

#日常
wordsdaily = ['[流泪][流泪][拥抱][拥抱]','🤗🤗','已阅，不错','嗨呀？','我在！','[大笑][大笑]','已阅，是假的','让我康康','我来康康',
         '吴语','我来啦！','前排吃🍉','保持善意，祝您平安','？？','哈哈哈哈哈哈','到此一氵放','你手短短','nsdd',
         '给你dd','哇哦！！！！','我觉得不行','xswl','你在逗我','万碎爷驾到！咣当','美美美（超大声','惊惹','宁可信其有，不可信其吴',
         '[鼓掌][鼓掌]','华华世界，吴奇不有','我可以我可以','赵小果追着猪路过（猪跑了( ๑ˊ•̥▵•)੭₎₎','……','你糊了','看戏😬🤔',
         '我气得全身发抖,大热天手脚冰凉','我不要你觉得，我要我觉得。','啧啧啧啧啧（超大声','哎哟喂！（超大声',
         '我来啦','已阅，给你踩踩','我对此毫不知情','我也不知道','简直胡扯瞎闹！','差不多得了还没完没了了，键盘侠就说的是你这种人吧',
         '是我不懂 打扰了','给你锅盖','我不信我不信','嘤嘤嘤','我又来啦','赵小果背着猪路过','已阅，让人迷惑','真是美妙至极！',
         '太🉑️了','不错dd','看得我心里咯噔一下','很不错','[大笑][大笑]','已阅','已阅，晚安','已阅。','朕已阅',
         '我吴fk说','不错 和我的料对上了','(๑•̀ㅂ•́)و✧','棒！','你太糊了','打起来','D区','🤗~~',
         '嗨呀！','你不错','[大笑][大笑][大笑][大笑]','是真的','大家康康呢？','让大家康康呢！','我吴语凝噎','嘻嘻嘻',
         '吃🍉','歇一会儿吧','？？？？','哈哈哈哈','谢邀','rwkk','dd','哇哦！','ヽ(=▽=)و','不要骗我',
         '我有个朋友也想康康','已阅，毫不知情，深表震惊！','好了好了我知道了','天呐怎么会有这种事',
         '我来抢沙发了，我会是最赞吗？','好贴给你dd','是嘛？','dd楼主','[欢呼][欢呼]','你没有心','………',
         '我竟吴言以对','前排看戏😬🤔','爱你~','踩踩','先不说了我妈来了','吴鸡鲅鱼','噗','是嘛？','我是个没有感情的顶帖机器',
         '我是个没有感情的打卡机器','啊泥哈谁哟','怎么了呢','很吴语也很吴奈','哇特大喜讯！','哟喂，夺新鲜呐',
         '这是你的问题，你自己解决！','硕咚！','赵小果追着猪路过','🆙🆙','🐮🍺','太丑了！','迷幻行为','人设立住了',
         '🉑️','不错，建议加精','看得我心里咯噔一下','[思考][思考]','来呀，快活呀，反正有大把时光♪','打起来打起来！',
         '他大姨妈~(这是日语不是脏话！没文化！','有趣！','我只想给你给你宠爱♪','不用说了,听我的！','big胆！',
         '纳尼？','(ÒωÓױ)！','有点意思','意思不多，但还有点','放学别走！','惊了！','吐了','摸摸你！','害 我懒得给你评论了',
         '我眼泪PradaPrada的Dior','此刻又何以为歌♪','不愧是你','是你不懂 吴语','不愧是我！',
         '不要吵了，现在这局面都是被我们真正的对家挑起来的！','嘴下留德哈','可以，人设不倒','+1','dbq','🈚','我不知道',
         '我没有❤','💔💔💔💔','围观','莫名其妙','哈？','咦？','有、意思','豆列警告','条形码警告','哇塞',
         '💚 小可爱到此一氵放💚 小可爱到此一氵放💚💚 小可爱到此一氵放💚 小可爱到此一氵放💚 💚 小可爱到此一氵放💚',
         '👌','赵小果追着猪路过（猪跑了( ๑ˊ•̥▵•)੭₎₎','我是个没有感情的顶帖机器','嘿！','大家等一下我来处理！','可以，碰个大的',
         '已阅。完全捏造，已交律师处理','律师函警告！','一直很尊重吴老师，没交往，没视频，没故事','停！','我们都是有血有肉的人',
         '不错，入手了','他……真的是个好人','你介意有嫂子吗','👂🏿👂🏿👂🏿👂🏿👂','厉害👍🏿👍🏿','有、灵性','求私！','踢一脚',
         '楼主康康我喜欢的糊逼吧','emmmmmm','小碎哪去了？！','小碎都不来！','蹲','哭死我了哭死我了','脱粉了']

#国庆到7号
wordsguoqing =['我和我的祖国♪ 一刻也不能分割♪','我歌唱每一座高山♪ 我歌唱每一条河♪','🆙(啊~国庆快乐','国庆节快乐！'
               '不论我走到哪里♪ 都流出一首赞歌♪','我的祖国和我♪ 像海和浪花一朵♪','放假啦！','祝祖国70周年快乐！']

wordswu=['前排拉踩小吴','复建+10','小吴腿短短','ibjy没有x','舔狗埃博拉','华：这就安排','520亲儿子王一博','yb次方kswlkswl',
         '啵姐年轻貌美，生图能打，是娱乐圈都知道的，虽然脑子不好使，如果她真的长得不好看，那华姐爱她这么多年，只能说华姐瞎',
         '🌾您以后喊他的时候请称为💚农民博博💚好吗？','dd粉丝好可爱的！这肯定是pph！','pph你也信？哼！',
         '我就是瞎了！我就是喜欢他没素质！边谈恋爱边麦麸！整天买热搜虚假宣传！爱他丑而不自知!','农民綦一szd', 
         '💚不因吹逼走来💚不因吃藕离开💚始于欺骗陷于装逼💚钟于麦麸爱你吸血💚超级酷给绝世文盲💚赖日疯长💚 你是人间地狱💚',
         'I‘m coming！Really like my new house，My favorite color is Green🔫💚，I‘m all for peace & love^_^ Please don’t cut ibo’，it is a form of violece…don‘t do that！！！ I hope to be friends with your gays[嘻嘻] And I want to end my self-introduction by a poem：到此一氵放！',
         '奶啵被黑了八天八夜的时候，我跟我朋友打电话，她哭了，我也哭了。怎么会有这么丧心病狂的黑子！非要逼他退出娱乐圈才肯罢手吗？我气得浑身发抖，泪流不停。但怎么办呢？就算天空是黑的，也要摸黑生存，总要有人发出光啊！我气得花了650买了一个豆瓣号，做了个机器人，搜集了所有的锤，想到找出漏洞挨个反驳，誓还奶啵一个公道。搜集完了所有的锤后，我发现，这些锤，竟然都是真的！妈的吴博我恨你！你没有💚',
         '毕竟营销傻子多','勿cut cool gay','cool gay 到此一氵放','华早点倒闭','真是吴处不在','bjyx是假的','吴皇登基',
         '吴博博','宁可信綦有，不可信其吴','众所周知，碎组吴假料','博华一笑szd！','无花果kswlkswl','哥哥到底挡了谁的路？要这么搞他？',
         '看得我心理吴博一下','复建-10','太丑了！','迷幻行为','人设立住了','不要吵了，现在这局面都是被我们真正的对家挑起来的！',
         '我竟吴言以对','前排看戏😬🤔','华华世界，吴奇不有','打起来','D区','我气得全身发抖,大热天手脚冰凉',
         '吴鸡鲅鱼','嘴下留德哈','可以，人设不倒','是我不懂 打扰了','[流泪][流泪][拥抱][拥抱]','👂🏿👂🏿👂🏿👂🏿👂','[大笑][大笑][大笑][大笑]',
         '歇一会儿吧','完全捏造，已交律师处理','差不多得了还没完没了了，键盘侠就说的是你这种人吧','宁可信其有，不可信其吴',
         '华华世界，吴奇不有','吴语','保持善意，祝您平安','天呐怎么会有这种事','已阅。完全捏造，已交律师处理','已阅，洗洗睡吧']

wordsnight =['早点休息吧！！！','晚安啦！','怎么还不睡','都几点了','康康几点了！头秃','你咋还不睡！','已阅，请休息吧',
             '已阅，晚安','已阅，晚安！','已阅，晚安啦！','怎么还不睡','都几点了还不睡？','康康几点了!','啊~~~我都困了你怎么没睡']

wordsmorning =['小鸟说早早早!♪','哦嗨以哟~','早上好！','早呀','早！！上！！好！！','早早早','今天也要上班啊','早啊~','大早上的干啥呢',
               '早上好啊','我来啦！']

wu=['博','小吴','ib']
morning=['早']
night=['晚安']

#words.extend(wordsmorning)
words.extend(wordsguoqing)
words.extend(wordsdaily)
#words.extend(wordswu)
#words.extend(wordsnight)
#words.extend(wordsoner)
print(len(words))


# In[ ]:


#main

count=1
countmax=300

#proxyget=requests.get("http://127.0.0.1:5010/get/").json()
#proxies = {"https": proxyget['proxy']}
# idoverlap=[]
idcheck=[]

print(datetime.now())

while True:
    try:
        id=[]
        content=requests.get(groupurl+'?apikey='+apikey).text#打开
        print(count)

        for i in json.loads(content)['topics']:
            if i['comments_count'] == 0:
                id=i['id']
                print(id)
                
                if id==idcheck:
                    wechat("回复失败，请检查")
                idcheck=id
                
                random_word = random.choice(words)
                if ("晚安" in i['title'])or ("晚安" in i['content']):
                    random_word = random.choice(wordsnight)
                elif ("早" in i['title']):
                    random_word = random.choice(wordsmorning)
                else:
                    for word in wu:
                        if (word in i['title'])or (word in i['content']):
                            random_word = '\n前排提醒嘲贴去专楼'+random.choice(wordswu)

                params={"udid":'ad6178cb34ac0e0c43adbe47dd22c76f26bd651a',
                        "apikey":'0dad551ec0f84ed02907ff5c42e8ec70',
                        "text":random_word,
                        "channel":'Douban',
                        "os_rom":'android'
                        }

                url_comment='https://frodo.douban.com/api/v2/group/topic/'+id+'/create_comment'

                send=requests.post(url_comment,headers=headers,data=params)
                print('reply'+id)
                random_sleep = random.randint(3,5)#发帖后
                time.sleep(random_sleep)  

                if send.status_code != 200:#发送失败
                    print(send.status_code)
                    wechat("回复失败，请检查") 
                    errorcount=errorcount+1
        
        
        count=count+1
        
        if count>countmax:
                count =1
                apikey = random.choice(key)#换一下apikey
                
    except Exception as error:
        print(error)


# In[ ]:





# In[ ]:




