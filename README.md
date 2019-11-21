# RTL-SDRを用いたRF信号波形のキャプチャ
Pythonで実装した，RTL-SDRを用いてRF信号波形をキャプチャするための方法の説明．
## RTL-SDRのセットアップ（Windows）
### 必要なドライバのインストール
* USBドングルを初めてPCに接続すると，自動的にワンセグチューナーのドライバがインストールされる．
* しかし，ターミナルやスクリプトから操作するためには，USBドングルをRTL-SDRとして認識するドライバを適用する必要がある．
* まずはインターネットで「Zadig」というソフトウェアをダウンロードする．（URL: https://zadig.akeo.ie ）
* Zadigを管理者権限で実行する．
* Optionタブから，List All Devicesをクリックする．
* USBデバイス名がリストアップされるので，Bulk-In,Interface(Interface 0)または，RTL2832Uを選択する．
* Install Driverをクリックする．
* これで，USBドングルがRTL-SDRとして認識されるようになる．

### 操作ソフトのダウンロード及び設定
* インターネットでRTL-SDRを操作するためのモジュールをダウンロードする．（URL: http://sdr.osmocom.org/trac/attachment/wiki/rtl-sdr/RelWithDebInfo.zip ）
* Zipファイルを解凍し，中に入っている「rtl-sdr-release」フォルダをCドライブ直下などにコピーする．
* 32及び64ビットオペレーションの実行ファイルが用意されているため，利用しているPCに応じてどちらかを選択し，パスを通す．
* 通すパスは「rtl-sdr-release」フォルダ内の，「x32」フォルダまたは，「x64」フォルダである．
* 「x32」フォルダ内には32ビット用，「x64」フォルダ内には64ビット用の実行ファイルが格納されている．

### ターミナルによる操作
* ここまでのセッティングを終えると，コマンドプロンプトなどからRTL-SDRを操作することができるようになる．
* コマンド類はインターネットで調べてほしい．（URL: https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr ）

### Pythonで操作するための設定
* ターミナルによる操作は非常に使い勝手が悪い．
* PythonにはRTL-SDRが操作できるようになるライブラリがあるので，そのセットアップをする．
* pipコマンドなどで，「pyrtlsdr」というライブラリをインストールする．
```
> py -m pip install pyrtlsdr
```
* このリポジトリでは，RF信号をキャプチャするためのチュートリアル的なサンプルコードを公開しているが，細かな使い方はドキュメンテーションを参照してほしい．

## pyrtlsdrライブラリを利用したRF信号のキャプチャ
### ライブラリのインポート
```python
  import numpy as np
  import rtlsdr
```
* rtlsdr: RTL-SDRを扱えるようにするライブラリ
* numpy: あると便利

### インスタンス化
rtlsdr.RtlSdrクラスをインスタンス化
```python
  sdr = rtlsdr.RtlSdr(device_index=0)
```
* device_index: PCがUSBドングルに割り当てた番号（だいたい0か1）

### インスタンス変数の設定
```python
  sdr.sampling_rate = 20.48*10**6
  sdr.center_freq = 400*10**6
  sdr.set_agc_mode(True)
  sdr.gain = 50
```
* sampling_rate: サンプリングレート
* center_freq: 中心周波数
* set_agc_mode(): AGCモード（ブール値）
* gain: ゲイン

### 信号波形のキャプチャ
```python
  observationTime = 10**(-3)
  nSamples = observationTime*sdr.sampling_rate
  signalWave = sdr.read_samples(nSamples)
```
* observationTime: 観測時間
* nSamples: キャプチャするサンプル数
* read_samples(): 信号をキャプチャするメソッド

ここまでで，変数signalWaveにnSamplesで定義されたサンプル数の信号波形が格納される．
