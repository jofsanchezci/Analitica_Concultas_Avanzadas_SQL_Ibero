
# Consultas Avanzadas en SQL usando SQLite y Python

Este proyecto demuestra el uso de consultas avanzadas en SQL utilizando SQLite y Python. A continuación se describen las consultas implementadas en el script:

## 1. Subconsultas (Subqueries)
Las subconsultas permiten ejecutar una consulta dentro de otra. En este caso, se obtiene una lista de empleados cuyo salario es mayor que el salario promedio de todos los empleados.

```sql
SELECT nombre, salario 
FROM empleados 
WHERE salario > (SELECT AVG(salario) FROM empleados);
```

## 2. Joins complejos (LEFT JOIN)
Los `JOINs` permiten combinar filas de dos o más tablas. Se utiliza `LEFT JOIN` para combinar la tabla de empleados con la tabla de departamentos, incluyendo empleados que no tienen departamento asignado.

```sql
SELECT e.nombre, d.nombre AS departamento
FROM empleados e
LEFT JOIN departamentos d ON e.departamento_id = d.id;
```

## 3. Funciones de ventana (Window Functions)
Las funciones de ventana permiten realizar cálculos sobre un conjunto de filas relacionadas sin agruparlas. Aquí se muestra cómo obtener el rango de salarios utilizando `RANK()`.

```sql
SELECT nombre, salario,
RANK() OVER (ORDER BY salario DESC) AS salario_rango
FROM empleados;
```

## 4. Consultas recursivas con CTE (Common Table Expressions)
Las consultas recursivas permiten trabajar con estructuras jerárquicas, como empleados y sus gerentes. Se usa un `WITH RECURSIVE` para obtener una jerarquía de empleados.

```sql
WITH RECURSIVE EmpleadoJerarquia AS (
    SELECT id, nombre, gerente_id 
    FROM empleados
    WHERE gerente_id IS NULL
    UNION ALL
    SELECT e.id, e.nombre, e.gerente_id
    FROM empleados e
    INNER JOIN EmpleadoJerarquia ej ON e.gerente_id = ej.id
)
SELECT * FROM EmpleadoJerarquia;
```

## 5. Operadores de conjunto (Set Operators)
Los operadores de conjunto permiten combinar los resultados de varias consultas. En este caso, se utiliza `UNION ALL` para combinar dos selecciones de empleados.

```sql
SELECT nombre FROM empleados
UNION ALL
SELECT nombre FROM empleados;
```

## Requisitos

- Python 3.x
- SQLite (incluido en Python estándar)
- Paquete sqlite3 (incluido en Python estándar)

## Ejecución

Para ejecutar el script, simplemente corre el archivo Python que contiene las consultas avanzadas. Los resultados de cada consulta se imprimirán en la consola.

```
python consultas_avanzadas_sql.py
```

## Autor

Este ejemplo fue creado para demostrar el uso de consultas avanzadas en SQL utilizando Python y SQLite.
