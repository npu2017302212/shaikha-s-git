import codecs
import jieba.posseg as pseg
import jieba

jieba.load_userdict("人物名称.txt")
names = {}
relationships = {}
linenames = []
replace_words={'师母':'吴慧芬','陈老':'陈岩石','老赵':'赵德汉','达康':'李达康','高总':'高小琴',
              '猴子':'侯亮平','老郑':'郑西坡','小艾':'钟小艾','老师':'高育良','同伟':'祁同伟',
              '赵公子':'赵瑞龙','郑乾':'郑胜利','孙书记':'孙连城','赵总':'赵瑞龙','昌明':'季昌明',
               '沙书记':'沙瑞金','郑董':'郑胜利','宝宝':'张宝宝','小高':'高小凤','老高':'高育良',
               '伯仲':'杜伯仲','老杜':'杜伯仲','老肖':'肖钢玉','刘总':'刘新建',"美女老总":"高小琴"}

with codecs.open("剧情梗概.txt", 'r', 'utf8') as f:
    for line in f.readlines():
        text = pseg.cut(line)
        linenames.append([])
        for w in text:
            if w.flag != 'nr' or len(w.word) < 2:
                if w.word not in replace_words:
                    continue
            if w.word in replace_words:
                w.word = replace_words[w.word]
            linenames[-1].append(w.word)
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1

for line in linenames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] += 1

with codecs.open("结点.txt", "w", "utf8") as f:
    for name, times in names.items():
        if times > 10:
            f.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("关系.txt", "w", "utf8") as f:
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 10:
                f.write(name + " " + v + " " + str(w) + "\r\n")

