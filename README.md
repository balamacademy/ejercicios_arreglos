# Ejercicios de arreglos unidimensionales
### El ejercicio
1. Escriba la función mayores_que(x, valores) que cuente cuántos valores en la lista valores son mayores que x:
  ```sh
  > mayores_que(5, [7, 3, 6, 0, 4, 5, 10])
  3
  > mayores_que(2, [-1, 1, 8, 2, 0])
  1
  ```

2. La media aritmética (o promedio) de un conjunto de datos es la suma de los valores dividida por la cantidad de datos.
Escriba la función media_aritmetica(datos), donde datos es una lista de números, que entregue la media aritmética de los datos:
   ```sh
   > media_aritmetica([6, 1, 4, 8])
    4.75
   ```

3. Escriba un programa que pregunte al usuario cuántos datos ingresará, a continuación le pida que ingrese los datos uno por uno, y finalmente entregue como salida cuántos de los datos ingresados son mayores que el promedio.
  ```sh
  Cuantos datos ingresara? 5
  Dato 1: 6.5
  Dato 2: 2.1
  Dato 3: 2.0
  Dato 4: 2.2
  Dato 5: 6.1
  2 datos son mayores que el promedio
   ```

4. La mediana de un conjunto de datos reales es el valor para el que el conjunto tiene tantos datos mayores como menores a él.
  Más rigurosamente, la mediana es definida de la siguiente manera:
  si la cantidad de datos es impar, la mediana es el valor que queda en la mitad al ordenar los datos de menor a mayor;
  si la cantidad de datos es par, la mediana es el promedio de los dos valores que quedan al centro al ordenar los datos de menor a mayor.

  Escriba la función mediana(datos), que entregue la mediana de los datos:

  ```sh
  > mediana([5.0, 1.4, 3.2])
  3.2
  > mediana([5.0, 1.4, 3.2, 0.1])
  2.3
  ```

5. Desarrolle una función llamada desviacion_estandar(valores) cuyo parámetro valores sea una lista de números reales:
  ```sh
  > desviacion_estandar([1.3, 1.3, 1.3])
  0.0
  > desviacion_estandar([4.0, 1.0, 11.0, 13.0, 2.0, 7.0])
  4.88535225615
  > desviacion_estandar([1.5, 9.5])
  5.65685424949
  ```


6. La moda de un conjunto de datos es el valor que más se repite.
  Escriba la función modas(datos), donde datos es una lista, que entregue una lista con las modas de los datos:

  ```sh
  > modas([5, 4, 1, 4, 3, 3, 4, 5, 0])
  [4]
  > modas([5, 4, 1, 4, 3, 3, 4, 5, 3])
  [3, 4]
  > modas([5, 4, 5, 4, 3, 3, 4, 5, 3])
  [3, 4, 5]
  ```
7. Las medias móviles con retardo p de una serie de tiempo son la secuencia de todos los promedios de p valores consecutivos de la serie.

  Por ejemplo, si los valores de la serie son {5,2,2,8,−4,−1,2} entonces las medias móviles con retardo 3 son: (5+2+23)/3, (2+2+83)/3, (2+8−43)/3, (8−4−13)/3 y (−4−1+23)/3.
  Escriba la función medias_moviles(serie, p) que retorne el arreglo de las medias móviles con retardo p de la serie:
  ```sh
  > s = [5, 2, 2, 8, -4, -1, 2]
  >  medias_moviles(s, 3)
  [ 3,  4,  2,  1, -1]
  ```

8. Las diferencias finitas de una serie de tiempo son la secuencia de todas las diferencias entre un valor y el anterior.
  Por ejemplo, si los valores de la serie son {5,2,2,8,−4,−1,2} entonces las diferencias finitas son: (2−5), (2−2), (8−2), (−4−8), (−1+4) y (2+1).
  Escriba la función diferencias_finitas(serie) que retorne el arreglo de las diferencias finitas de la serie:
  ```sh
  > s = [5, 2, 2, 8, -4, -1, 2]
  > diferencias_finitas(s)
  [ -3,   0,   6, -12,   3,   3]
  ```


### Setup command
`sudo -H pip3 install pytest`

### Run command
`pytest`

### Notes
- pip's install path is not included in the PATH var by default, so without installing via `sudo -H`, pytest would be unaccessible.
