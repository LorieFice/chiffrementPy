lettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "é", "'", "è", '"', "à", "ç", "(", ")", "î", "ù", "!", "?", ".", ",", ";", ":", "-", "+", "/", "*", "@", "=", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Ç", "#", "^", "Â", "Ê", "Î", "Ô", "Û", "Ä", "Ë", "Ï", "Ö", "Ü", "À", "Æ", "æ", "É", "È", "Œ", "œ", "Ù", "ê"]


def codage(phrase, clé):
    if phrase and clé:
        phraseChiffres = toNumber(phrase)
        cléChiffres = toNumber(clé)
        chiffré = somme(phraseChiffres, cléChiffres, True)
        chiffréLettres = toLettres(chiffré)
        chiffréLettres.reverse()
        print("".join(chiffréLettres))
    else:
        print("Ayy il faut mettre des valeurs")

def toNumber(arr):
    liste = []
    for i in range(len(arr)):
        for j in range(len(lettres)):
            if arr[i] == lettres[j]:
                liste.append(j)
    return liste

def somme(phrase, clé, condition):
    result = []
    if condition:
        for i in range(len(phrase)):
            a = (i % len(clé))
            result.append((phrase[i] + clé[a]) % len(lettres))
    elif condition == False:
        for i in range(len(phrase)):
            a = (i % len(clé))
            result.append((phrase[i] - clé[a] + len(lettres)) % len(lettres))
    return result

def toLettres(phrase):
    liste = []
    for i in range(len(phrase)):
        for j in range(len(lettres)):
            if phrase[i] == j:
                liste.append(lettres[j])
    return liste

def décodage(phrase, clé):
    if phrase and clé:
        phraseChiffres = toNumber(phrase)
        phraseChiffres.reverse()
        cléChiffres = toNumber(clé)
        chiffré = somme(phraseChiffres, cléChiffres, False)
        chiffréLettres = toLettres(chiffré)
        print("".join(chiffréLettres))
    else:
        print("Ayy il faut des valeurs")

continuer = True

while(continuer):
    demande = input("Tapez 1 pour chiffrer, 2 pour déchiffrer, ou autre pour quitter... ")
    if demande == 1 or demande == "1":
        codage(input("Entrez un mot : "), input("Entrez une clé : "))
    elif demande == 2 or demande == "2":
        décodage(input("Entrez un mot : "), input("Entrez une clé : "))
    else:
        print("")
        print("Merci d'avoir utilisé ce script !")
        print("Codé par LorieFice le best ! ")
        print("Dédicace à Youyou")
        continuer = False
