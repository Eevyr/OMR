# Final Report of group 21
##### BON Chloe, LEE Yi-Hsuan

Our goal in this project is to be able to play a pictured music sheet through a computer and turn it into MIDI file which allows user to edit after.


## MIDI File Generator

1. once the repository cloned, compile midiconstructor.c and run a.out :
```bash
gcc midiconstructor.c
./a.out 
```
2. the corresponding midi file of your code has been created under the name of output.mid
3. If you want to change some of the content : you can modify the ecrire_piste2 function in midiconstructor.c.

To modify the instrument that will be played :
you have to play with the number in the argument of the function MIDI_Program_Change(fichier, 0, NUMBER_FOR_INSTRUMENT).
Here are some example of instruments : 0 to 7 represents pianos, 40 to 47 represents strings, and 80 to 103 synthesizers.

To modify the notes :
It is the inout of Note_unique_avec_duree(fichier, CHANNEL, MIDI_NOTE, VELOCITY, DURATION) that you need to modify.
The midi note can take values from 0 to 127 (Do2 to Sol8), and you can find on wikipedia conversion for notes to numbers for midi file.

You can add other loops are free notes in sequence inside this function ecrire_piste2 or you can also add another track (which would be called ecrire_piste3 to be played in parallel (create a polyphonic music !)).

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

3. Enjoy your Christmas song. Or, change the parameter of image path:
```bash
python3 ctc_predict.py -model Semantic-Model/semantic_model.meta -vocabulary Data/vocabulary_semantic.txt -image [image_path]
```
4. You can go to `output/` to find out `output.mid` which is the file you just played
5. Import `output.mid` into your favorite software and add more features


## Polyphonic Music Player 

Using pretrained models :

1. Use the colab notebook to output your xml file.

Trying to retrain from scratch (warning : doesn't work completely):

1. Clone the polyphonic repo;
2. Dataset of png files and their corresponding labels in an organized folder can be download at [this adress](https://www.dropbox.com/s/sh26wabvcsaf4zn/Dataset.zip?dl=0).
Unzip it and put it in the polyphonic repository.
3. Once in the experiment_code folder, for the baseline decoder, run the command :
```bash
python train.py -voc_p vocab/baseline_pitch.txt -voc_r vocab/baseline_rythm.txt -corpus ../Dataset
```
For the FlagDecoder : 
```bash
python train_flag_accidental.py -voc_s <path to symbol vocabulary> -voc_d <path to duration vocabulary> -voc_a <path to alter vocabulary> -corpus <path to corpus>
```
And for the RNNDecoder :
```
python train_multi.py -voc_p <path to pitch vocabulary> -voc_r <path to rhythm vocabulary> -corpus <path to corpus>
```

Once the models trained, you can test them with the same command lines as in the colab notebook but the models/baseline.pt etc... (pre-trained models), has to be replaced by the path to the new generated model.

## Citation
This repository was used for the experiments reported in the paper:

[End-to-End Neural Optical Music Recognition of Monophonic Scores](http://www.mdpi.com/2076-3417/8/4/606)

[An empirical evaluation of end-to-end polyphonic optical music recognition](https://archives.ismir.net/ismir2021/paper/000020.pdf)

## Corpora
This repository (monophonic part) is intended for the Printed Images of Music Staves (PrIMuS) dataset.

PrIMuS can be donwloaded from https://grfia.dlsi.ua.es/primus/
