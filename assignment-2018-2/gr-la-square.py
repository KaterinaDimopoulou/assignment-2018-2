import sys

def sameValues(transversals,new_transversal):
    same = 0
    for trans in transversals:      #gia kathe transversal
        for i in range(1,len(trans[0])):
            if(trans[0][i]==new_transversal[i]):   #an exoun koino simeio de theloume na mpei sti lista me transversals
                same=1
                return same
    return same


file = open(sys.argv[1],"r")
array = []
for line in file:
    row = []
    for letter in line :
        if(letter!=" " and letter!=',' and letter!='\n'):
            row.append(int(letter))
    array.append(row)

dimension = len(array)


transversals = {}   #dictionary of transversals
list_transversals = []
#briskoume oles tis pithanes diasxiseis
for row1 in range(dimension):                   #gia kathe grammi tou pinaka
    list_transversals.append([[array[row1][0]],[row1]])
    column = 0
    while len(list_transversals) > 0 :   #oso i lista den einai adeia simainei oti exo kai alles epiloges
        current_trans , visited = list_transversals.pop()
        column = len(current_trans)    #to mikos tou transversal pou eksetazoume mas dinei pia stili koitame
        for row2 in range(dimension):
            #an den exo ksanaparei : auto to stoixeio kai stoixeio apo auti ti grammi
            #tote i to bazo sto dictionary i to bazo sti lista
            if(row2 not in visited):
                if(array[row2][column] not in current_trans):
                #an exei simplirothei to transversal to bazo sto dictionary
                    if( column + 1 == dimension ):
                        if current_trans[0] not in transversals.keys():
                            transversals[current_trans[0]] = [current_trans + [array[row2][column]]]
                        else:
                            transversals[current_trans[0]].append(current_trans + [array[row2][column]])
                    else:
                        list_transversals.append((current_trans + [array[row2][column]],visited + [row2]))
    list_transversals = []


if(len(transversals)==0):   #de brethikan diasxiseis

    print(list_transversals)

else:

    path = []
    first_element = 0 #ksekiname apo to 0
    while(len(path)<dimension):
        flag = 0
        possible_transversals = transversals.get(first_element)
        for i in range(len(possible_transversals)):       #gia kathe transversal me kleidi to first_element
            if(sameValues(path,possible_transversals[i]) == 0):#an mporei na mpei sto path
                path.append([possible_transversals[i],i+1])
                first_element += 1 #an brw paw sto epomeno stoixeio
                flag = 1
                break
        if(flag==0):    #an den einai kanena
            trans , last_trans_checked = path.pop() #an bgei pao sto proigoumeno stoixeio
            first_element -= 1


    #ftiaxnoume ena pinaka me midenika
    orthogonio =[]
    for i in range(dimension):
        list = []
        for j in range(dimension):
            list.append(0)
        orthogonio.append(list)

    #simplironoume to orthogonio tetragono
    #bazoume ta stoixeia opos mas leei to transversal pou brikame
    for trans in path:
        element = trans[0][0]
        for column in range(1,dimension):
            for row in range(dimension):
                if(array[row][column] == trans[0][column]):
                    orthogonio[row][column] = element


    grecolatin = []
    for row in range(dimension):
        row1 = []
        for column in range(dimension):
            row1.append((array[row][column],orthogonio[row][column]))
        grecolatin.append(row1)

    for row in grecolatin:
        print(row)
