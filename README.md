# NLP-analyzer

> Morphological analyzer demo

## Description
Morphological analyzer reads input words from stdin.
Uses dictionary stored in pytrie structure marisa-trie.
Output is in format "word:lemma:tag:pattern".

* For more information about tags see [tags.pdf](https://github.com/AndrejKlocok/NLP-analyzer/blob/master/tags.pdf)

## Dependencies
[Pytries](https://github.com/pytries/marisa-trie)

``` bash
# install pytrie marisa
pip install marisa-trie

```
## Usage
``` bash
# example
echo naše červené kladivá | python3 marisa.py corpora.marisa
```

