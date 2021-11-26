def HT_kalimat():
    N=len(kalimat)//2
    if (len(kalimat)%2==0) and ((len(kalimat)/2)%2==0):
        return kalimat[(N)//2 : ((N)//2)*-1]
    elif (len(kalimat)%2==0) and ((len(kalimat)/2)%2!=0):
        return kalimat[((N)//2)+1 : (((N)//2)+1)*-1]
    else:
        return kalimat[(((N)+1)//2) : (((N)+1)//2)*-1]

kalimat= str(input("Masukkan kata :"))
print("Huruf tengah pada kata" ,kalimat ,"adalah" ,HT_kalimat())
