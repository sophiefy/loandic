# LoanDic

LoanDic is a Japanese loanword dictionary. Its entries are mainly from: 

- [UniDic](https://clrd.ninjal.ac.jp/unidic/)
- [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic)
- [naist-jdic](http://naist-jdic.osdn.jp/)

We have also manually checked and added some entires.


## Demo

```bash
% mecab -d . -r ./dicrc -Osimple
```

```bash
hello and welcome to youtube my channel!  
hello   ハロー  名詞-普通名詞-一般
and     アンド  名詞-普通名詞-一般
welcome ウェルカム      名詞-普通名詞-一般
to      ツー    名詞-普通名詞-一般
youtube ユーチューブ    名詞-普通名詞-一般
my      マイ    名詞-普通名詞-一般
channel チャンネル      名詞-普通名詞-一般
!               補助記号-句点
```

```bash
tiktokはbytedanceが運営する動画に特化したsocial networking serviceです。
tiktok  ティックトック  名詞-普通名詞-一般
は      ワ      助詞-係助詞
byte    バイト  名詞-普通名詞-一般
dance   ダンス  名詞-普通名詞-一般
が      ガ      助詞-格助詞
運営    ウンエー        名詞-普通名詞-サ変可能
する    スル    動詞-非自立可能
動画    ドーガ  名詞-普通名詞-一般
に      ニ      助詞-格助詞
特化    トッカ  名詞-普通名詞-サ変可能
し      シ      動詞-非自立可能
た      タ      助動詞
social networking       ソーシャルネットワーキング      名詞-普通名詞-一般
service サービス        名詞-普通名詞-一般
です    デス    助動詞
。              補助記号-句点
```

