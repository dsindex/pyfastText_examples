# pyfastText

- description
  - test code for [fastText.py(python wrapper of fastText)](https://github.com/salestock/fastText.py)
  - installation
  ```shell
  pip install fasttext
  ```

- word vector
  - train
  ```shell
  python train_wordvec.py --train data.txt --model model --type=skipgram

  # you can adjust hyper-parameters by editing train_wordvec.py
  # for example,
  #   dim=100, epoch=5, ... 
  # data.txt is just a big text file like 'text9'
  ```
  - lookup
  ```shell
  python lookup_wordvec.py --model=model.bin
  facebook
  [-0.21015416085720062, 0.3572459816932678, ..., 0.40391290187835693, 0.2624731957912445]
  ```

- classification


