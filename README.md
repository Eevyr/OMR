# Final Report of group 21
##### BON Chloe, LEE Yi-Hsuan

Our goal in this project is to be able to play a pictured music sheet through a computer and turn it into MIDI file which allows user to edit after.


## MIDI File Generator



## Monophonic Music Player and translator
### Semantic Recognition

1. Download monophonic code:
  * you can download everything from [this folder](https://www.dropbox.com/sh/smd8r66pxcegvt3/AAB3vFl77J3Scu791mZsAMuIa?dl=0)
  * or you can also clone the `monophonic` repo, and add the [Semantic-Model](https://www.dropbox.com/sh/senkb6uoogx46fu/AABIT3ZVaxw-5EzpE3_-XPUTa?dl=0) folder in 

, and go to the project folder under a command line window. Make sure your path is like this:

```
monophonic % 
```
2. Type this command

```bash
python3 ctc_predict.py -model Semantic-Model/semantic_model.meta -vocabulary Data/vocabulary_semantic.txt -image Data/example/deck_full.png
```

3. Enjoy your Christmas song
4. You can go to `output/` to find out `output.mid` which is the file you just played
5. Import `output.mid` into your favorite software and add more features


## Polyphonic Music Player 


## Citation
This repository was used for the experiments reported in the paper:

[End-to-End Neural Optical Music Recognition of Monophonic Scores](http://www.mdpi.com/2076-3417/8/4/606)
[An empirical evaluation of end-to-end polyphonic optical music recognition](https://archives.ismir.net/ismir2021/paper/000020.pdf)

## Corpora
This repository is intended for the Printed Images of Music Staves (PrIMuS) dataset.

PrIMuS can be donwloaded from https://grfia.dlsi.ua.es/primus/
