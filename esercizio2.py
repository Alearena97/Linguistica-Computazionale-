# _*_ coding: utf-8 _*_
import sys
import codecs
import nltk
import math
from nltk import bigrams
from nltk import trigrams

def main(testo1,testo2):
    def programma2(testo1):
    #apro il documento e divido il file in frasi 
        tokenTot = []
        apri = codecs.open(testo1,"r","utf-8") #apro il file
        raw = apri.read() #leggo il file appena aperto
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        testofrasi = tokenizer.tokenize(raw) #divido in frasi il file
    #eseguo la tokenizzazione e il postagging su tutti i token
        for frase in testofrasi:
            testoparole = nltk.word_tokenize(frase)
            tokenTot = tokenTot+testoparole 
            tokensPosTot = nltk.pos_tag(tokenTot) #eseguo il postagging su tutti i token
    #certo tra tutti i token i piu' frequenti ed escludo la punteggiatura 
        venticom = nltk.FreqDist(tokenTot)
        venticom = venticom.most_common()
        indice = 0
        print "I venti token piu' frequenti esclusa la punteggiatura sono\n"
        for token in venticom:
            if indice == 20:
                break
            if token[0] not in [".",",",":",";","!","?","(",")","'"]:
                print indice+1, token[0].encode("utf-8"), token[1]
                indice = indice + 1
    #creo un unico for e opero sui token postaggati e ordinati per frequenza. Aggiungo delle condizioni per trovare sostantivi, aggettivi e POS e successivamente stamparli, numerandoli.
        tokenPosTotfreq = nltk.FreqDist(tokensPosTot)
        tokenPosTotfreqCom = tokenPosTotfreq.most_common()
        sostantivi = []
        aggettivi = []
        i = 0
        toptenpos = []
        for token in tokenPosTotfreqCom:
            if (len(sostantivi) < 20) and (token[0][1]  == "NN" or token[0][1] == "NNP" or token[0][1] == "NNS" or token[0][1] == "NNPS"):
                sostantivi.append(token)
            if (len(aggettivi) < 20) and (token[0][1] == "JJ" or token[0][1] == "JJR" or token[0][1]  == "JJS"):
                aggettivi.append(token)
            if len(sostantivi) and len(aggettivi) == 20:
                break
            if (i < 10):
                if token[0][1] not in toptenpos:
                    toptenpos.append(token[0][1])
                    i = i + 1
    #stampo e numero sostantivi aggettivi e POS 
        print "\nI 20 sostantivi piu' frequenti sono\n"
        for indice,sostantivo in enumerate(sostantivi,1):
            print indice, sostantivo[0][0].encode("utf-8"), sostantivo[1]  
        print "\nI 20 aggettivi piu' frequenti sono\n"
        for indice,aggettivo in enumerate(aggettivi,1):
            print indice, aggettivo[0][0].encode("utf-8") , aggettivo[1] 
        print "\nI 10 POS piu' frequenti sono\n"
        for indice,pos in enumerate(toptenpos,1):
            print indice, pos.encode("utf-8")
    #Creo i bigrammi e i trigrammi e li ordino per frequenza
        bigrammi = bigrams(tokensPosTot)
        trigrammi = trigrams(tokensPosTot)
        bigrammifreq = nltk.FreqDist(bigrammi)  
        bigrammifreqOrdinati = bigrammifreq.most_common()
    #creo un for che scorre i bigrammi precedentemente ordinati 
        max = 1
        print "\nI venti bigrammi di token piu' frequenti, escluse le congiunzioni, gli articoli e la punteggiatura, sono:\n"
        for token in bigrammifreqOrdinati:
    #inserisco delle condizioni per numerare i bigrammi e fare in modo che ne il primo ne il secondo elemento della coppia siano congiunzioni articoli o punteggiatura
            if token[0][0][1] not in [".",",",":","(",")","IN","CC","DT"] and token[0][1][1] not in [".",",",":","(",")","IN","CC","DT"]:
                print max, token
                max = max + 1
            if max == 21:
                break
    #creo la lista di tutti i POS
        listadipos = []
        for token in tokensPosTot:  
            listadipos.append(token[1])
    #creo i bigrammi e i trigrammi dei POS e li ordino per frequenza 
        bigrammiPOS = list(bigrams(listadipos))
        trigrammiPOS = list(trigrams(listadipos))
        bigrammiPOSfreq = nltk.FreqDist(bigrammiPOS)
        trigrammiPOSfreq = nltk.FreqDist(trigrammiPOS)
    #creo un for per numerare e stampare i 10 bigrammi di POS piu' frequenti 
        print "\n I dieci bigrammi di POS piu' frequenti sono:\n"
        bigrammi10 = bigrammiPOSfreq.most_common(10)
        indice = 1
        for bigramma in bigrammi10:
            print indice,bigramma
            indice = indice +1
    #creo un for per numerare e stampare i 10 trigrammi di POS piu' frequenti
        print "\n I dieci trigrammi di POS piu' frequenti sono:\n"
        indice = 1
        trigrammi10 = trigrammiPOSfreq.most_common(10)
        for trigramma in trigrammi10:
            print indice,trigramma
            indice = indice +1
    #creo degli array in cui inserire i bigrammi aggettivo-sostantivo e le loro frequenze
        ventibigrammiAS = []
        coppieFreq = []
        for bigramma in bigrammifreqOrdinati:
    #inserisco delle condizioni per trovare i bigrammi aggettivo-sostantivo con frequenza maggiore di 2 e li inserisco negli array precedentemente creati, insieme alle loro frequenze 
            if bigramma[0][0][1] == "JJ" or bigramma[0][0][1] == "JJR" or bigramma[0][0][1] == "JJS" and tokenTot.count(bigramma[0][0][0]) > 2:
                if bigramma[0][1][1] == "NN" or bigramma[0][1][1] == "NNP" or bigramma[0][1][1] == "NNS" or bigramma[0][1][1] == "NNPS" and tokenTot.count(bigramma[0][1][0]) > 2:
                    ventibigrammiAS.append(bigramma)
                    frequenzeComponenti = tokenTot.count(bigramma[0][0][0]),tokenTot.count(bigramma[0][1][0])
                    coppieFreq.append(frequenzeComponenti)
    #stampo la lista numerata dei 20 bigrammi di token con le relative condizioni 
        print "\nI venti bigrammi composti da aggettivo-sostantivo con frequenza di token maggiore di 2 sono:\n"
        for indice,bigramma in enumerate(ventibigrammiAS,1):
            if indice == 21:
                break
            print indice,bigramma
            print "con frequenze di",bigramma[0][0][0].encode('utf-8'),coppieFreq[indice][0],"e",bigramma[0][1][0].encode('utf-8'),coppieFreq[indice][1]
    #calcolo la probabilita' di entrambi gli elementi dei bigrammi e la stampo 
            print "con probabilita di",bigramma[0][0][0].encode('utf-8'),float(coppieFreq[indice][0])/len(tokenTot)
            print "con probabilita di",bigramma[0][1][0].encode('utf-8'),float(coppieFreq[indice][1])/len(tokenTot)
    #calcolo la probabilita' congiunta dei bigrammi e la stampo 
            print "e probabilita congiunta di",float(bigramma[1])/float(len(tokenTot)),
    #creo una variabile che contiene la formula della LMI che utilizzero' durante il print 
            mi = (float(bigramma[1])/float(len(tokenTot))) / (float(coppieFreq[indice][0])/len(tokenTot) * float(coppieFreq[indice][1])/len(tokenTot))
            print "con Local Mutual Information di", math.log(mi,2),"\n"
    #inizializzo tre variabili che conterranno le frasi e le loro probabilita'
        frasiscelte = []
        frasiprobabilita0 = []
        frasiprobabilita1 = []
    #definisco una funzione per calcolare il modello di ordine 1 e eseguo il comando bigrams sulla frase su cui lavoro, chiamero' questa funzione in un ciclo for
        def markov1(frasetokenizzata):
            frasebigramma = list(bigrams(frasetokenizzata))
            for indice,bigramma in enumerate(frasebigramma,1):
    #calcolo la probabilita del primo elemento
                if indice == 1:
                    probabilita1 = (((tokenTot.count(bigramma[0])*1.0))/(len(tokenTot)*1.0))
    #calcolo la probabilita condizionata di tutti gli elementi seguenti
                if indice > 1:
                    frequenzabigramma = 0
    #controllo la frequenza di ogni elemento del bigramma
                    for coppia in bigrammifreq:
                        if coppia[0][0] == bigramma[0] and coppia[1][0] == bigramma[1]:
                            frequenzabigramma = frequenzabigramma + 1
    #aggiungo la probabilita condizionata alla catena markov 1 
                    probBig = (frequenzabigramma*1.0/len(tokenTot)*1.0)
                    probU = ((tokenTot.count(bigramma[1])*1.0)/len(tokenTot)*1.0)
                    probabilita1 = (probabilita1*1.0) * ((probBig / probU)*1.0)
    #salvo il risultato
                if indice == len(frasebigramma):
                    frasiprobabilita1.append(probabilita1)
    #creo un for che scorre le frasi con le relative condizioni richieste e se soddisfatte calcola il modello di markov 0
        for frase in testofrasi:
            tokenfrase = nltk.word_tokenize(frase)
            probabilita0 = 1
            if len(tokenfrase) >= 6 and len(tokenfrase) <= 8:
                for max,token in enumerate(tokenfrase,0):
                    if tokenTot.count(token) <= 2:
                        break
                    else: probabilita0 = probabilita0 * (tokenTot.count(token)*1.0/len(tokenTot)*1.0)
                    if max == len(tokenfrase)-1:
                        frasiscelte.append(frase)
                        frasiprobabilita0.append(probabilita0)
                        markov1(tokenfrase)
    #stampo la frase con probabilita maggiore calcolata con markov 0
        primaprob = frasiprobabilita0[0]
        primafrase = frasiscelte[0]
        for indice,frase in enumerate(frasiscelte,0):
            if frasiprobabilita0[indice] > primaprob:
                primaprob = frasiprobabilita0[indice]
                primafrase = frasiscelte[indice]
    #stampo la frase con probabilita maggiore calcolata con markov 1
        secondafrase = ""
        secondaprob = 0
        for indice, frase in enumerate(frasiscelte,0):
            if frasiprobabilita0[indice] > secondaprob and frasiprobabilita0[indice] is not primafrase:
                secondaprob = frasiprobabilita1[indice]
                secondafrase = frasiscelte[indice]
        print "\nla frase con probabilita' piu' alta lunga minimo 6 e massimo 8 token e nella quale ogni token ha frequenza maggiore di 2 e'\n",primafrase,"con probabilita' calcolata con modello di markov di ordine 0",primaprob
        print "\nla seconda frase con probabilita' piu' alta lunga minimo 6 e massimo 8 token e nella quale ogni token ha frequenza maggiore di 2 e'\n",secondafrase,"con probabilita' calcolata con modello di markov di ordine 1",secondaprob
    print "analisi primo corpus\n"
    programma2(testo1)
    print "\nanalisi secondo corpus\n"
    programma2(testo2)
main(sys.argv[1],sys.argv[2])
 
