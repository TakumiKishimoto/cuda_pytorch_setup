# PyTorch環境セットアップガイド

本ガイドでは、研究室のサーバー環境でPyTorchとCUDAを適切にセットアップする手順を説明します。

## 優先事項

1. **PyTorchとCUDAのバージョン整合性**
   - PyTorchとCUDAのバージョンを合わせることが重要です。

2. **利用可能なCUDAバージョン**
   - 研究室のサーバー環境で利用可能なCUDAバージョン（2024/06/27現在）:
     - CUDA 11.4
     - CUDA 11.7 (推奨)
     - CUDA 11.8
     - CUDA 12.4
   - 推奨: CUDA 11.7（ほぼ全ての環境で利用可能）

3. **CUDAパスの設定**
   - 選択したCUDAバージョンのパスを設定します。
   - `~/.bash_profile`に以下のリンクから適切なパス設定をコピーして追加してください：
     [CUDAパス設定](http://100.86.45.10/pukiwiki/?cuda#q=cuda)

      例 cuda 11.7 ver
      ```
      export CUDA_HOME="/usr/local/cuda-11.7"
      export PATH=$CUDA_HOME/bin:$PATH
      export LIBRARY_PATH=$CUDA_HOME/lib:$CUDA_HOME/lib64:$LIBRARY_PATH
      export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$CUDA_HOME/extras/CUPTI/lib64:$LD_LIBRARY_PATH
      # CUDNN
      export LIBRARY_PATH=/opt/home/cudnn/cudnn-linux-x86_64-8.8.1.3_cuda11-archive/lib:$LIBRARY_PATH
      export LD_LIBRARY_PATH=/opt/home/cudnn/cudnn-linux-x86_64-8.8.1.3_cuda11-archive/lib:$LD_LIBRARY_PATH
      export CPATH=/opt/home/cudnn/cudnn-linux-x86_64-8.8.1.3_cuda11-archive/include:$CPATH
      ```

4. **パスの読み込み**
   - サーバーにログイン後、以下のコマンドを実行してCUDAパスを読み込みます：
     ```
     source ~/.bash_profile
     ```
   - 確認のため、`~/.bash_profile`に以下のような行を追加することをお勧めします：
     ```
     echo 'CUDA 11.7 version loaded'
     ```

5. **PyTorchのインストール**
   - 選択したCUDAバージョンに対応するPyTorchをインストールします。
   - インストールコマンドは以下のリンクから確認できます：
     [PyTorch過去バージョン](https://pytorch.org/get-started/previous-versions/)

6. **CUDA利用可能性の確認**
   - `cuda_test.py`を実行して、現在のバージョンとCUDAの利用可能性を確認します。

以上の手順に従うことで、PyTorchとCUDAを適切にセットアップできます。