arr=[int(x) for x in input().split()]
sum=int(input())
for x in arr:
	for y in arr[arr.index(x)+1:]:
		for z in arr[arr.index(y)+1:]:
			if(x+y+z==sum):print(f"{x},{y},{z}")


