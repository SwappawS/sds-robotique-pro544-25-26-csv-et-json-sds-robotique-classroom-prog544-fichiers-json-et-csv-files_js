nouveauFichier = open("08_nouveau.txt", "w")
nouveauFichier.write("J'aime beaucoup les yoshis.")
nouveauFichier.close

modificationFichier = open("08_nouveau.txt", "a")
modificationFichier.write(" surtout le rouge")
modificationFichier.close