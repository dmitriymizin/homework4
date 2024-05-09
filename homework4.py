immutable_var=(1, "war", False)
print(immutable_var)
# immutable_var[0]=111
# Кортеж не поддерживает изменение элементов

mutable_list=[1,2, "speed", False]
print(mutable_list)
mutable_list[1]=222
mutable_list[2]="brake"
mutable_list[3]=True
print(mutable_list)