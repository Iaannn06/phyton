#1
def convert_temperature (suhu,values) :
    if suhu == 'C' :
        return (values + 32) 
    elif suhu == 'F' :
        return (values - 32) 
    else:
        return "satuan tidak valid, gunakan 'C' untuk Celsius dan 'F' buat Fahrenheit"

unit=input("Masukan satuan suhu yang diinginkan Suhu(C atau F) = ")
value=float(input("Masukan nilai suhu = "))

converted_value = convert_temperature(unit, value)

if isinstance(converted_value, str):
    print(converted_value)
else:
    if unit == "C":
        print(f"{value} nilai derajat Celsius sama dengan {converted_value:.2f} derajat Fahrenheit.")
    elif unit == "F":
        print(f"{value} nilai derajat Fahrenheit sama dengan {converted_value:.2f} derajat Celsius.")


#2 
r = int(input("Masukan jari jari lingkaran = "))
Area = lambda r : 3.14 * r * r
print(Area(r))

