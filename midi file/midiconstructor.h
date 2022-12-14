//
//  midiconstructor.h
//  
//
//  Created by Chloé Bon on 19/11/2022.
//

#ifndef midiconstructor_h
#define midiconstructor_h

#include <stdio.h>

#endif /* midiconstructor_h */

void MIDI_ecrire_en_tete(FILE *fichier, unsigned char SMF, unsigned short pistes, unsigned short nbdiv);

unsigned long MIDI_ecrire_en_tete_piste(FILE *fichier);

void MIDI_fin_de_la_piste(FILE *fichier);

void ecrire_taille_finale_piste(FILE *fichier, unsigned long marque);

void ecrire_piste1(FILE *fichier);

void MIDI_delta_time(FILE *fichier, unsigned long duree);

void ecrire_variable_length_quantity(FILE *fichier, unsigned long i);

void MIDI_Program_Change(FILE *fichier, unsigned char canal, unsigned char instrument);

void MIDI_Note(unsigned char etat, FILE *fichier, unsigned char canal, unsigned char Note_MIDI, unsigned char velocite);

void Note_unique_avec_duree(FILE *fichier, unsigned char canal, unsigned char Note_MIDI, unsigned char velocite, unsigned long duree);

void MIDI_Control_Change(FILE *fichier, unsigned char canal, unsigned char type, unsigned char valeur);

void ecrire_piste2(FILE *fichier);

void MIDI_tempo(FILE *fichier, unsigned long duree);
