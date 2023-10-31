# Cob2

El proyecto cob2 trata de crear un software capaz de detectar las semejanzas de do archivos para posteriormente bloquearlos.

## Uso del archivo main.py

El archivo main.py es el core del proyecto solo te va a devolver sus semejanzas y no va a efectuar ningun labor de bloqueo

** Para ejecutar al archivo **

```bash

[python3 / python] -> foo@bar/> 
python3 main.py archivo-base archivo-a-comparar

```

Se pueden poner mas de un archivo a comparar

** Output **

```bash
[X%, X1%], [X%, X2%]
```

Varias x significan varios porcentajes de semejanza entre los archivos

- La primera metrica analiza el archivo en base al numero de caracteres usados
- La segunda metrica lo analiza en base a la posición de los caracteres usados (Por longitud de archivo más pequeña)
