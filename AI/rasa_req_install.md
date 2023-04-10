python3.7.7

pip 23.0.1

---

mecab-ko 설치

```
wget https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
```

```
tar xvfz mecab-0.996-ko-0.9.2.tar.gz
```

```
cd mecab-0.996-ko-0.9.2
```

```
./configure
```

```
make
```

```
make check
```

```
sudo make install
```



mecab-ko-dic 설치

```
wget https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
```

```
tar xvfz mecab-ko-dic-2.1.1-20180720.tar.gz
```

```
cd mecab-ko-dic-2.1.1-20180720
```

```
./configure
```

```
make
```

```
sudo make install
```



mecab-ko-dic 에러 발생 시

```
ls /usr/local/lib/libmecab.so.2
```

```
sudo nano /etc/ld.so.conf
```

```bash
# 아래와 같이 수정
include ld.so.conf.d/*.conf
/usr/local/lib
```



다시 mecab-ko-dic 설치

```
cd .. 
rm -r mecab-ko-dic-2.1.1-20180720

tar xvfz mecab-ko-dic-2.1.1-20180720.tar.gz
cd mecab-ko-dic-2.1.1-20180720
sudo apt install autoconf
sudo apt install libtool
autoreconf
./configure
make
sudo make install
```







---



(on ubuntu, pip install mecab_python)

pip install natto-py

pip install spacy

mkdir tmp

python -m spacy init vectors ko ko.vec.gz ./tmp/ko_vec_model

python -m spacy package ./tmp/ko_vec_model ./

cd ko_pipeline-0.0.0

python setup.py sdist

cd dist

pip install ko_pipeline-0.0.0.tar.gz

pip install rasa



rasa train

rasa shell