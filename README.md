# 💱 Sistema de Cambio de Divisas

Aplicación de consola en Python que permite a los usuarios registrarse, iniciar sesión y realizar conversiones de divisas en tiempo real usando una API externa.

---

## 🚀 Funcionalidades

- Registro de usuarios con nombre, correo y contraseña
- Inicio de sesión con validación de credenciales
- Saludo dinámico según la hora del día (buenos días / tardes / noches)
- Conversión de divisas en tiempo real entre cualquier par de monedas
- Manejo de errores para monedas inválidas o problemas de conexión

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **requests** — para consumir la API de tasas de cambio
- **datetime** — para obtener fecha y hora actual
- **[Frankfurter API](https://www.frankfurter.app/)** — API gratuita de tasas de cambio en tiempo real (datos del Banco Central Europeo)

---

## 📦 Instalación

1. Cloná el repositorio:
```bash
git clone https://github.com/SantiVC-06/cambio-de-divisas.git
cd cambio-de-divisas
```

2. Instalá la dependencia necesaria:
```bash
pip install requests
```

3. Ejecutá el programa:
```bash
python Cambio_de_divisas.py
```

---

## 📁 Estructura del proyecto

```
cambio-de-divisas/
│
├── Cambio_de_divisas.py     # Archivo principal con el menú y lógica de conversión
└── ModuRegistroIngreso.py   # Módulo de registro e inicio de sesión
```

---

## 💻 Uso

Al ejecutar el programa verás el siguiente menú:

```
1. Registrar usuario
2. Iniciar sesión
3. Salir
```

Una vez iniciada la sesión, el sistema te pedirá:

```
¿De qué moneda? USD
¿A qué moneda? EUR
¿Cuánto quieres convertir? 100

100.0 USD = 92.00 EUR
Tasa usada: 1 USD = 0.92 EUR
```

### Algunas monedas disponibles

| Código | Moneda |
|--------|--------|
| USD | Dólar estadounidense |
| EUR | Euro |
| GBP | Libra esterlina |
| JPY | Yen japonés |
| BRL | Real brasileño |
| MXN | Peso mexicano |
| CAD | Dólar canadiense |
| CHF | Franco suizo |
| ARS | Peso argentino |

---

## ⚠️ Consideraciones

- Los usuarios registrados se almacenan en memoria, por lo que se pierden al cerrar el programa.
- Las tasas de cambio son obtenidas en tiempo real y pueden variar.
- Se requiere conexión a internet para realizar conversiones.

---

## 👤 Autor

Desarrollado por [@SantiVC-06](https://github.com/SantiVC-06) como proyecto de aprendizaje en Python.
