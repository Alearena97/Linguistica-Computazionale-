# _*_ coding: utf-8 _*_
import sys
import codecs
import nltk

def main(testo1,testo2):
    confronta(testo1,testo2)

def confronta(doc1,doc2):
    print "\nConfronto di",doc1,"e ",doc2
    #inizializzo le variabili che usero' durante il programma 
    def dividifrasiEparole(testo):
        tokenTot = []
        numero = 1
        tokensPosTot = []
    #definisco la funzione per calcolare la densita' lessicale
	def densitalessicale(catGram,avv,tokens):
            punteggiatura = 0
    #creo un for con una condizione per eliminare la punteggiatura
            for token in tokens:                                   
                if token[1] == "." or token[1] == ",":
                    punteggiatura = punteggiatura+1
    #stampo il calcolo della densita' lessicale 
            print "La densita' lessicale e'",(catGram[0]+catGram[1]+catGram[2]+float(avv))/(len(tokens)-punteggiatura)
        print "\nDivisione in frasi e parole",testo
    #apro il file, ne leggo il contenuto, lo divido in frasi
        apri = codecs.open(testo,"r","utf-8") 
        raw = apri.read() 
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        testofrasi = tokenizer.tokenize(raw)  #divide in frasi il file
    #creo un for per tokenizzare il testo ed eseguire il postagging
        for frase in testofrasi:
            testoparole = nltk.word_tokenize(frase)
            tokenTot = tokenTot+testoparole 
            tokensPosTot = nltk.pos_tag(tokenTot) 
    #creo un for per eliminare la punteggiatura dal corpus e mantenere solo le parole
        rawsoloparole = []
        for parola in raw:
            if parola not in [".",",",":",";","!","?","(",")","'"]:
                rawsoloparole.append(parola)
    #eseguo le operazioni richieste e le stampo 
        print "\nIl numero totale di token e'", len(tokenTot)
        print "\nIl numero totale di frasi e'", len(testofrasi)
        print "\nLa lunghezza media delle frasi e'",(len(tokenTot)/len(testofrasi))
    #utilizzo l'array creato prima con le sole parole del testo per trovare la media di caratteri
        print "\nLa lunghezza media delle parole e'",(float(len(rawsoloparole))/len(tokenTot)),"\n"
    #creo un dizionario ordinato basantomi sui token totali 
        dizionario = nltk.FreqDist(tokenTot)
        dizionarioOrdinato = dizionario.most_common()
    #creo un for per calcolare la type token ratio per porzioni incrementali di 1000 token. Inizializzo un array nel quale inseriro' i risultati 
        ttr = []
        i = 1
        for token in tokenTot:
            if token not in ttr:
                ttr.append(token)
            if  i%1000 == 0:     #se divisibile per 1000 effettua le operazioni anche per 2000,3000,4000,5000
    #utilizzo i risultati inseriti nell'array per eseguire le operazioni e stampare la grandezza del vocabolario e la ttr per porzioni incrementali di 1000 token
                print "la grandezza del vocabolario per",i," token e'",len(ttr)
                print "la type token ratio dei primi",i," token e'",float(len(ttr))/i
            i = i+1
    #inizializzo un array nel quale inserire i risultati delle classi di frequenza 3, 6 e 9
        i = 0
        classiFreq = [0,0,0]
    #creo un for che scorre il dizionario ordinato e aggiungo le condizioni per avere i primi 5000 token
        for voce in dizionarioOrdinato:
            if i == 5000:
                return    #quando i arriva a 5000token dara' i risultati delle classi di frequenza
            if voce[1] == 3:
                classiFreq[0] = classiFreq[0]+1
            if voce[1] == 6:
                classiFreq[1] = classiFreq[1]+1
            if voce[1] == 9:
                classiFreq[2] = classiFreq[2]+1
            i = i+1
    #stampo la grandezza delle classi di frequenza grazie all'array precedentemente creato
        print "\nLa grandezza della classe di frequenza 3 sui primi 5000 token e'",classiFreq[0]
        print "\nLa grandezza della classe di frequenza 6 sui primi 5000 token e'",classiFreq[1]
        print "\nLa grandezza della classe di frequenza 9 sui primi 5000 token e'",classiFreq[2],"\n"
    #creo un array nel quale inserire i sostantivi, gli aggettivi e i verbi che trovo nel testo postaggato
    #creo anche una variabile per contare gli avverbi che utilizzo per calcolare la densita' lessicale
        sos_agg_vrb = [0,0,0]
        avverbi = 0
    #creo un for che scorre il testo postaggato e aggiunge all'array precedentemente creato e alla variabile avverbi gli elementi richiesti
        for token in tokensPosTot:
    #inserisco delle condizioni nelle quali elenco i POS da utilizzare per trovare gli elementi richiesti e inserirli nell'array e nella variabile
            if token[1]  == "NN" or token[1] == "NNP" or token[1] == "NNS" or token[1] == "NNPS":
                sos_agg_vrb[0] = sos_agg_vrb[0]+1
            if token[1] == "JJ" or token[1] == "JJR" or token[1]  == "JJS":
                sos_agg_vrb[1] = sos_agg_vrb[1]+1
            if token[1]  == "VB" or token[1] == "VBD" or token[1] == "VBG" or token[1] == "VBN" or token[1]  == "VBP" or token[1] == "VBZ":
                sos_agg_vrb[2] = sos_agg_vrb[2]+1
            if token[1] == "RB" or token[1] == "RBR" or token[1] == "RBS":
                avverbi = avverbi+1
    #creo un array speculare a sos_agg_vrb che contenga i nomi delle categorie memorizzate in quest'ultimo, 
    #all'indice 0 di sos_agg_vrb trovo i sostantivi, all'indice 0 di categorie la stringa sostantivi
        categorie = ["sostantivi","aggettivi","verbi"]
        i = 0
    #stampo i risultati
        for categoria in sos_agg_vrb:
            print "Il numero medio di",categorie[i],"per frase e'", float(categoria)/len(testofrasi)
            i = i +1
        densitalessicale(sos_agg_vrb,avverbi,tokensPosTot)
    dividifrasiEparole(doc1)
    dividifrasiEparole(doc2)
main(sys.argv[1],sys.argv[2])
 
