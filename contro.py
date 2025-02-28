import datetime 
fecha=datetime.datetime.now()
an=datetime.datetime.strftime(fecha, "%Y")
print("Complete los siguientes datos")
p=int(input(" Ingresa   1.-El estudiante entra durante el primer periodo, 2.- El estudiante entra durante el segundo periodo(proceso de admision "))
if p>=1 and p<=2:
    print("Carreras disponibles en el Tecnologico")
    print("1--Ing.Industrial")
    print("2--Tics")
    print("3--Ing.Sistemas")
    print("4--Ing.Quimica")
    print("5--Ing.Civil")
    print("6--Ing.Mecatronica")
    print("7--Ing.Electrica")
    print("8--Ing.Logistica")
    print("9--Lic.Administracion")
    carrera=int(input("Selecciona la carrera  "))
    if carrera <=9 and carrera >=1:
        nuMat={"AIngreso":an,"Periodo":p,"Carrera":carrera}
        nuAlum=int(input("Ingresa el numero del alumno  "))
        if nuAlum<=999 and nuAlum >=100:
            nuMat['NumeroAlumn']=nuAlum
            matricula=str(nuMat['AIngreso']+str(nuMat['Periodo'])+str(nuMat['Carrera'])+str(nuMat['NumeroAlumn']))
            print(matricula)
        elif nuAlum<=99 and nuAlum >=10:
            nuMat['NumeroAlumn'] = f"0{nuAlum}"
            matricula=str(nuMat['AIngreso']+str(nuMat['Periodo'])+str(nuMat['Carrera'])+str(nuMat['NumeroAlumn']))
            print(matricula)
        elif nuAlum <=9 and nuAlum >=1:
            nuMat['NumeroAlumn'] = f"00{nuAlum}"
            matricula=str(nuMat['AIngreso']+str(nuMat['Periodo'])+str(nuMat['Carrera'])+str(nuMat['NumeroAlumn']))
            print(matricula)
        else:
            print("Digite un valor valido")
    else:
        print("Digite un valor valido")
else:
    print("Error verifique los datos")



#print(list(nuMat.values()))