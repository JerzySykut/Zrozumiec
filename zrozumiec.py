print("KredyKonsumencki")
print("kwotakredytu")
kwotakredytu = int(input())
print("procentkredytu")
oprocentowanie = float(input())
print("wysokoscraty")
wysokoscraty = float(input())
infStyc1 = 1.59282448436825
zostalo = ("Pozostała kwota")
mniej = ("Mniej niz poprzednim miesiacu")
wzor = (1 + ((infStyc1 + oprocentowanie )/1200)) * kwotakredytu - wysokoscraty
roznica = (kwotakredytu-wzor)
print(wzor)
inf_Lut2 = -0.453509101198007
wzor2 = (1 + ((inf_Lut2 + oprocentowanie )/1200)) * wzor - wysokoscraty
roznica = (wzor-wzor2)
print(wzor2)
inf_mar3 = 2.32467171712441
wzor3 = (1 + ((inf_mar3 + oprocentowanie )/1200)) * wzor2 - wysokoscraty
roznica = (wzor2-wzor3)
print(wzor3)
inf_kwi4 = 1.26125440724877
wzor4 = (1 + ((inf_kwi4 + oprocentowanie )/1200)) * wzor3 - wysokoscraty
roznica = (wzor3-wzor4)
print(wzor4)
inf_maj5 = 1.78252628571251
wzor5 = (1 + ((inf_maj5 + oprocentowanie )/1200)) * wzor4 - wysokoscraty
roznica = (wzor4-wzor5)
print(wzor5)
inf_cze6 = 2.32938454145522
wzor6 = (1 + ((inf_cze6 + oprocentowanie )/1200)) * wzor5 - wysokoscraty
roznica = (wzor5-wzor6)
print(wzor6)
inf_lip7 = 1.50222984223283
wzor7 = (1 + ((inf_lip7 + oprocentowanie )/1200)) * wzor6 - wysokoscraty
roznica = (wzor6-wzor7)
print(wzor7)
inf_sie8 = 1.78252628571251
wzor8 = (1 + ((inf_sie8 + oprocentowanie )/1200)) * wzor7 - wysokoscraty
roznica = (wzor7-wzor8)
print(wzor8)
inf_wrz9 = 2.32884899407637
wzor9 = (1 + ((inf_wrz9 + oprocentowanie )/1200)) * wzor8 - wysokoscraty
roznica = (wzor8-wzor9)
print(wzor9)
inf_paz10 = 0.616921348207244
wzor10 = (1 + ((inf_paz10 + oprocentowanie )/1200)) * wzor9 - wysokoscraty
roznica = (wzor9-wzor10)
print(wzor10)
inf_lis11 = 2.35229588637833
wzor11 = (1 + ((inf_lis11 + oprocentowanie )/1200)) * wzor10 - wysokoscraty
roznica = (wzor10-wzor11)
print(wzor11)
inf_gru12 = 0.337779545187098
wzor12 = (1 + ((inf_gru12 + oprocentowanie )/1200)) * wzor11 - wysokoscraty
roznica = (wzor11-wzor12)
print(wzor12)
inf_sty13 = 1.57703524727525
wzor13 = (1 + ((inf_sty13+ oprocentowanie )/1200)) * wzor12 - wysokoscraty
roznica = (wzor12-wzor13)
print(wzor13)
inf_lut14 = -0.292781442607648
wzor14 = (1 + ((inf_lut14 + oprocentowanie )/1200)) * wzor13 - wysokoscraty
roznica = (wzor13-wzor14)
print(wzor14)
inf_mar15 = 2.48619659017508
wzor15 = (1 + ((inf_mar15 + oprocentowanie )/1200)) * wzor14 - wysokoscraty
roznica = (wzor14-wzor15)
print(wzor15)
inf_kwi16 = 0.267110317834564
wzor16 = (1 + ((inf_kwi16 + oprocentowanie )/1200)) * wzor15 - wysokoscraty
roznica = (wzor15-wzor16)
print(wzor16)
inf_maj17 = 1.41795267229799
wzor17 = (1 + ((inf_maj17 + oprocentowanie )/1200)) * wzor16 - wysokoscraty
roznica = (wzor16-wzor17)
print(wzor17)
inf_czer18 = 1.05424326726375
wzor18 = (1 + ((inf_czer18 + oprocentowanie )/1200)) * wzor17 - wysokoscraty
roznica = (wzor17-wzor18)
print(wzor18)
inf_lip19 = 1.4805201044812
wzor19 = (1 + ((inf_lip19 + oprocentowanie )/1200)) * wzor18 - wysokoscraty
roznica = (wzor18 - wzor19)
print(wzor19)
inf_sie20 = 1.57703524727525
wzor20 = (1 + ((inf_sie20 + oprocentowanie )/1200)) * wzor19 - wysokoscraty
roznica = (wzor19-wzor20)
print(wzor20)
inf_wrz21 = -0.0774206903147018
wzor21 = (1 + ((inf_wrz21 + oprocentowanie )/1200)) * wzor20 - wysokoscraty
roznica = (wzor2-wzor5)
print(wzor21)
inf_paz22 = 1.16573339872354
wzor22 = (1 + ((inf_paz22 + oprocentowanie )/1200)) * wzor21 - wysokoscraty
roznica = (wzor21-wzor22)
print(wzor22)
inf_lis23 = -0.404186717638335
wzor23 = (1 + ((inf_lis23 + oprocentowanie )/1200)) * wzor22 - wysokoscraty
roznica = (wzor22-wzor23)
print(wzor23)
inf_gru24 = 1.499708520831232
wzor24 = (1 + ((inf_gru24 + oprocentowanie )/1200)) * wzor23 - wysokoscraty
roznica = (wzor23-wzor24)
print(wzor24)

