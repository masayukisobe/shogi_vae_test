## ベータ分布を用いたVAEによる将棋の形勢判断の試み

### 概要
人間による将棋の形勢判断は勝率%ではなく「先手が安全勝ち」「どちらかが倒れている」「静かな互角」「形勢不明」のように表現されることが多い。これをAIでやるにはベータ分布が適していると思われる。

探索ベースの将棋AIの評価関数は勝率%(内部的には大抵int16_t)を用いる必要があるが、この試みでは探索を用いるAIではなく局面のみに対してVAE(変分オートエンコーダ)を適用してベータ分布を出力するモデルを作成する。

### 方針
 - VAEを用いてベータ分布のパラメータを教師なし学習
   - VAEは通常正規分布が用いられるが、再パラメータ化トリックでベータ分布を用いる
 - 得られたエンコーダを、局面の勝ち負けを教師信号とする教師あり学習でファインチューニング
 - エンコーダの構造は、低層に既存のhalf kp NNUEの評価パラメータの特徴量抽出パラメータを流用し上層のみ学習
 - デコーダ側はシンプルな密結合NN
 - 損失関数はTBD
 - 学習データ上の原局面を用いる場合とそこから静止探索を行った局面を用いる場合の２つを試す

### プログラム類

 - 学習と評価（作成中）
 - ツール類
   - show_nn_bin.py .. NNUE評価関数ファイル(nn.bin)のビューア
   - show_psv.py .. PSVファイル(学習データセット)のビューア
