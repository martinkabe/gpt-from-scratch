# gpt-from-scratch

## Youtube

https://www.youtube.com/watch?v=kCc8FmEb1nY

### Other good yt videos about transformers

https://www.youtube.com/watch?v=SZorAJ4I-sA

https://www.youtube.com/watch?v=4Bdc55j80l8

https://www.youtube.com/watch?v=ZXiruGOCn9s

## Google Colab

https://colab.research.google.com/drive/1JMLa53HDuA-i7ZBmqV7ZnA3c_fvtXnx-?usp=sharing

## Create Conda virtual environment

conda create -n cvenv python=3.10 anaconda

## Switch to virtual environment (using conda)

conda activate cvenv

## Deactivate virtual environment

conda deactivate

## Delete a no longer needed virtual environment

conda remove -n cvenv --all

## Install packages

conda install -n cvenv pandas gensim nltk

<!-- for transformers pipeline - this requires older version of numpy -->

<!-- conda remove -n cvenv numpy -->

conda install -n cvenv numpy==1.19.5

conda install -n cvenv -c huggingface transformers
