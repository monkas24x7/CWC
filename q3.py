num=int(input())
dic={"1000":"M",
	"900":"CM",
	"500":"D",
	"400":"CD",
	"100":"C",
	"90":"XC",
	"50":"L",
	"40":"XL",
	"10":"X",
	"9":"IX",
	"5":"V",
	"4":"IV",
	"1":"I",}
rom=""
for x in dic.keys():
	rom+= int(num/int(x))*dic[x]
	num=num%int(x)
print(rom)
