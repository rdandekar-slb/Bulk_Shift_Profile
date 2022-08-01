
def lin_int(x_arr,y_arr,x):
    if x<=x_arr[0]:
        return y_arr[0]
    if x>=x_arr[-1]:
        return y_arr[-1]

    for i in range(1,len(x_arr)-1):
        if x<=x_arr[i] and x>x_arr[i-1]:
            return y_arr[i-1]+((y_arr[i]-y_arr[i-1])/(x_arr[i]-x_arr[i-1]))*(x-x_arr[i-1])



data=[]
x_values=[1,5,10,12,15,20,25,30,35,40,43,45,46,50,55,60,65,70,72,75,80,85]
y_values=[4.629522618,13.8198704,31.74746885,52.09091239,75.36311178,107.556174,146.1352551,191.7254833,245.8255806,305.3263543,370.828096,439.3841715,508.7734023,583.4365946,665.4387628,755.6863407,851.4450957,956.3404619,1062.86493,1173.622146,1292.043547,1418.416605]
data.append(x_values)
data.append(y_values)



# unknowns=[3,41,19,94,62,62,89,13,20,56,46,30,23,98]
unknowns=[1,5,10,12,15,20,25,30,35,40,43,45,46,50,55,60,65,70,72,75,80,85]
for unknown in unknowns:
    print(unknown, lin_int(x_values,y_values,unknown))
