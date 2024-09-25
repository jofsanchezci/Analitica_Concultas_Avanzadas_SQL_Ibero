import sqlite3

# Crear una base de datos en memoria y obtener un cursor
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# Crear las tablas necesarias para los ejemplos
cur.execute('''
    CREATE TABLE empleados (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        salario REAL,
        departamento_id INTEGER,
        gerente_id INTEGER
    )
''')

cur.execute('''
    CREATE TABLE departamentos (
        id INTEGER PRIMARY KEY,
        nombre TEXT
    )
''')

# Insertar datos en la tabla departamentos
cur.executemany('''
    INSERT INTO departamentos (id, nombre) 
    VALUES (?, ?)
''', [
    (1, 'Recursos Humanos'),
    (2, 'Ventas'),
    (3, 'Ingeniería')
])

# Insertar datos en la tabla empleados
cur.executemany('''
    INSERT INTO empleados (id, nombre, salario, departamento_id, gerente_id) 
    VALUES (?, ?, ?, ?, ?)
''', [
    (1, 'Carlos', 50000, 1, None),
    (2, 'Ana', 60000, 2, 1),
    (3, 'Luis', 70000, 3, 1),
    (4, 'Maria', 65000, 2, 2),
    (5, 'Juan', 55000, 3, 3)
])

# 1. Subconsulta: Obtener empleados con salario mayor que el salario promedio
print("1. Subconsulta: Empleados con salario mayor que el salario promedio")
subquery_example = cur.execute('''
    SELECT nombre, salario 
    FROM empleados 
    WHERE salario > (SELECT AVG(salario) FROM empleados)
''').fetchall()
print(subquery_example)

# 2. LEFT JOIN: Obtener empleados y sus departamentos, incluyendo empleados sin departamento
print("\n2. LEFT JOIN: Empleados y sus departamentos")
join_example = cur.execute('''
    SELECT e.nombre, d.nombre AS departamento
    FROM empleados e
    LEFT JOIN departamentos d ON e.departamento_id = d.id
''').fetchall()
print(join_example)

# 3. Función de ventana: Obtener el rango de salarios
print("\n3. Función de ventana: Rango de salarios")
window_function_example = cur.execute('''
    SELECT nombre, salario,
    RANK() OVER (ORDER BY salario DESC) AS salario_rango
    FROM empleados
''').fetchall()
print(window_function_example)

# 4. Consulta recursiva: Obtener la jerarquía de empleados y gerentes
print("\n4. Consulta Recursiva: Jerarquía de empleados y gerentes")
cur.execute('''
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
''')
recursive_query_example = cur.fetchall()
print(recursive_query_example)

# 5. UNION ALL: Combinar nombres de empleados de dos selecciones (emulando distintos años)
print("\n5. UNION ALL: Combinación de empleados de distintos años")
union_all_example = cur.execute('''
    SELECT nombre FROM empleados
    UNION ALL
    SELECT nombre FROM empleados
''').fetchall()
print(union_all_example)

# Cerrar la conexión
conn.close()
