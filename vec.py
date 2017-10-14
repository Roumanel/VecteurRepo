def triBulle(Liste):#trier les elements du vecteur
	n = len(Liste)		
	for i in range(n-1) :
		for j in range(n-1,i,-1) :
			if Liste[j] < Liste[j-1] :
				Liste[j],Liste[j-1] = Liste[j-1],Liste[j]
	return Liste

def sommeElem(Liste1,Liste2):#la somme des touts le elements du tab
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



def inversElem(Liste):#inverser les elements du vacteur
	n=len(Liste)
	list1=[]
	for i in range(n):
		list1.append(Liste[n-i-1])
	return list1


def maxElem(Liste):#retouner le max d'un vecteur
	n=len(Liste)
	max=0
	for i in range(n):
		if Liste[i]>max:
			max=Liste[i]
	return max



def minElem(Liste):#retouner le min d'un vecteur
	n=len(Liste)
	min=Liste[0]
	for i in range(n):
		if Liste[i]<min:
			min=Liste[i]
	return min
	
