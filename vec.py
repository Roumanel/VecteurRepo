
def triBulle(Liste):
"""
	Cette fonction tie les éléments d'un vecteur en utilisant le trie à bulles
	@type Liste : Vecteur
	@param Liste : Le vecteur à trier

	@rtype: Vecteur
	@return: Un vecteur trié

"""
	n = len(Liste)		
	for i in range(n-1) :
		for j in range(n-1,i,-1) :
			if Liste[j] < Liste[j-1] :
				Liste[j],Liste[j-1] = Liste[j-1],Liste[j]
	return Liste


def sommeElem(Liste1,Liste2):
"""
	Cette fonction somme les éléments de deux vecteur de meme taille
	@type Liste1 : Vecteur
	@param Liste1 : Le premier vecteur

	@type Liste2 : Vecteur
	@param Liste2 : Le deuxième vecteur

	@rtype: Vecteur
	@return: Un vecteur dont les éléments sont la somme des deux vecteurs en entrée

"""
	Liste=[]
	try:
		n1 = len(Liste1)	
		n2 = len(Liste2)
		assert n1==n2
		for i in range(n1):
			Liste.append(Liste1[i]+Liste2[i])
	except AssertionError:
		print("les deux vecteurs n'ont pas la meme taille")

	return Liste




def inversElem(Liste):
"""
	Cette fonction inverse les éléments d'un vecteur 
	@type Liste : Vecteur
	@param Liste : Le vecteur à inverser

	@rtype: Vecteur
	@return: Un vecteur dont les element sont l'inverse des éléments du vecteur en entrée 

"""
	n=len(Liste)
	list1=[]
	for i in range(n):
		list1.append(Liste[n-i-1])
	return list1



def maxElem(Liste):
"""
	Cette fonction retourne le plus grand élément d'un vecteur
	@type Liste : Vecteur
	@param Liste : Le vecteur à traiter

	@rtype: Nombre
	@return: Le plus grand élément du vecteur en entrée

"""
	n=len(Liste)
	max=0
	for i in range(n):
		if Liste[i]>max:
			max=Liste[i]
	return max





def minElem(Liste):
"""
	Cette fonction retourne le plus petit élément d'un vecteur
	@type Liste : Vecteur
	@param Liste : Le vecteur à traiter

	@rtype: Nombre
	@return: Le plus petit élément du vecteur en entrée

"""
	n=len(Liste)
	min=Liste[0]
	for i in range(n):
		if Liste[i]<min:
			min=Liste[i]
	return min


def formule(Liste):
"""
	Cette fonction applique une formule sous forme de fonction à tous les éléments d’un vecteur.
	@type Liste : Vecteur
	@param Liste : Le vecteur à traiter

	@rtype: Nombre
	@return: Le résultat de la fonction appliquée au vecteur en entrée

"""
	n=len(Liste)
	for i in range(n):
		Liste[i]=Liste[i]*2 
		
	
	return Liste
	
