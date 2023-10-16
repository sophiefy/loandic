# LoanDic

LoanDic is a Japanese loanword dictionary. Its entries are mainly from: 

- [UniDic](https://clrd.ninjal.ac.jp/unidic/)
- [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic)
- [naist-jdic](http://naist-jdic.osdn.jp/)

We have also manually checked and added some entires.


## Demo

```bash
% mecab -d . -r ./dicrc -Ochamame
```

```bash
hello and welcome to my channel!   
B       hello   ハロー                  名詞-普通名詞-一般
        and     アンド                  名詞-普通名詞-一般
        welcome ウェルカム                      名詞-普通名詞-一般
        to      ツー                    名詞-普通名詞-一般
        my      マイ                    名詞-普通名詞-一般
        channel チャンネル                      名詞-普通名詞-一般
        !                       ！      補助記号-句点
```

```bash
tiktokはbytedanceが運営する動画に特化したsocial networking serviceです。
B       tiktok  ティックトック                  名詞-普通名詞-一般
        は      ワ      ハ      は      助詞-係助詞                             ワ
        byte    バイト                  名詞-普通名詞-一般
        dance   ダンス                  名詞-普通名詞-一般
        が      ガ      ガ      が      助詞-格助詞                             ガ
        運営    ウンエー        ウンエイ        運営    名詞-普通名詞-サ変可能                          ウンエー
        する    スル    スル    為る    動詞-非自立可能 サ行変格        連体形-一般             スル
        動画    ドーガ  ドウガ  動画    名詞-普通名詞-一般                              ドーガ
        に      ニ      ニ      に      助詞-格助詞                             ニ
        特化    トッカ  トッカ  特化    名詞-普通名詞-サ変可能                          トッカ
        し      シ      スル    為る    動詞-非自立可能 サ行変格        連用形-一般             スル
        た      タ      タ      た      助動詞  助動詞-タ       連体形-一般             タ
        social networking       ソーシャルネットワーキング                      名詞-普通名詞-一般
        service サービス                        名詞-普通名詞-一般
        です    デス    デス    です    助動詞  助動詞-デス     終止形-一般             デス
        。                      。      補助記号-句点
```

