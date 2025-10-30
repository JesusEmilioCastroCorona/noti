📨 Sistema de Notificaciones en Python
Patrones de Diseño: Observer + Factory Method | Principios SOLID

Este proyecto implementa un sistema de notificaciones flexible en Python, aplicando los principios SOLID y los patrones de diseño Observer y Factory Method.

Permite enviar mensajes a múltiples usuarios mediante diferentes canales (Email, SMS, Push), según las preferencias individuales de cada uno.

🧩 Estructura del proyecto

notification_system/
│
├── notification_system.py   # Código principal
├── README.md                # Documentación del proyecto
└── requirements.txt         # (opcional) Dependencias si se agregan librerías externas

⚙️ Funcionamiento del sistema
🔁 1. Patrón Observer
Notificador: actúa como Subject. Mantiene una lista de observadores (usuarios) y les envía notificaciones.
Usuario: actúa como Observer. Se suscribe o se da de baja del notificador y recibe mensajes cuando ocurre un evento.
🏭 2. Patrón Factory Method
INotificacionFactory: define el contrato para crear objetos de notificación.
NotificacionFactory: crea instancias concretas de notificaciones (Email, SMS, Push).
INotificacion: interfaz común que define el método enviar().
Implementaciones concretas:
EmailNotificacion
SMSNotificacion
PushNotificacion
🧱 3. Principios SOLID aplicados
Principio	Descripción
S - Single Responsibility	Cada clase tiene una responsabilidad única.
O - Open/Closed	El sistema está abierto a extensiones sin modificar el código existente.
L - Liskov Substitution	Las clases concretas pueden reemplazar sus abstracciones sin romper el sistema.
I - Interface Segregation	Interfaces pequeñas y específicas (IObservador, INotificacion, etc.).
D - Dependency Inversion	Las clases dependen de abstracciones, no de implementaciones concretas.
🚀 Ejecución del programa
🔧 Requisitos
Python 3.8 o superior.
No requiere librerías externas (usa únicamente la biblioteca estándar).
▶️ Pasos para ejecutar
Clona el repositorio:
git clone https://github.com/tu-usuario/sistema-notificaciones.git
cd sistema-notificaciones

2. Ejecuta el programa:

   ```bash
   python notification_system.py
   ```

### 💻 Ejemplo de salida esperada

```
[INFO] Ana suscrito.
[INFO] Luis suscrito.
[INFO] Carla suscrito.
[NOTIFICADOR] Enviando mensaje a 3 observador(es)...
[EMAIL] Para: ana@example.com | Mensaje: Nueva actualización disponible: versión 1.2.0
[SMS] Para: +5215587654321 | Mensaje: Nueva actualización disponible: versión 1.2.0
[PUSH] Usuario: Luis | Mensaje: Nueva actualización disponible: versión 1.2.0
[PUSH] Usuario: Carla | Mensaje: Nueva actualización disponible: versión 1.2.0
[EMAIL] Para: carla@example.com | Mensaje: Nueva actualización disponible: versión 1.2.0
[INFO] Luis dado de baja.
[NOTIFICADOR] Enviando mensaje a 2 observador(es)...
[EMAIL] Para: ana@example.com | Mensaje: Recordatorio: mantenimiento programado mañana 02:00 AM.
[PUSH] Usuario: Carla | Mensaje: Recordatorio: mantenimiento programado mañana 02:00 AM.
[EMAIL] Para: carla@example.com | Mensaje: Recordatorio: mantenimiento programado mañana 02:00 AM.
```
![alt text](image.png)
---

## 👥 Clases principales

| Clase                                                                       | Rol               | Descripción                                           |
| --------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------- |
| `Usuario`                                                                   | Observer          | Recibe mensajes según sus preferencias.               |
| `Notificador`                                                               | Subject           | Gestiona la lista de usuarios y notifica los eventos. |
| `INotificacion`, `EmailNotificacion`, `SMSNotificacion`, `PushNotificacion` | Strategy de envío | Implementan el envío según el tipo.                   |
| `NotificacionFactory`                                                       | Factory Method    | Crea el tipo de notificación solicitado.              |

---

## 📚 Conceptos clave demostrados

* Aplicación práctica de **Observer Pattern**.
* Uso del **Factory Method Pattern** para crear objetos de notificación.
* Ejemplo de código **SOLID** y fácilmente extensible.
* Buenas prácticas de **diseño orientado a objetos** en Python.

---
Cómo este diseño cumple SOLID y patrones

S (Responsabilidad Única):
Cada clase hace una cosa: Usuariogestiona datos/recepción, Notificadorgestiona lista de observadores, cada INotificaciongestiona sólo el envío por su canal.

O (Abierto/Cerrado):
Para agregar un nuevo canal (por ejemplo WhatsappNotificacion) creas la clase que implemente INotificaciony las registros/añades en la fábrica. El resto del sistema no necesita cambiar (puedes mejorar la fábrica para soportar el registro dinámico y así no tocar su código).

L (Liskov):
Las implementaciones concretas pueden sustituir la abstracción INotificacionsin romper el flujo.

I (Segregación de interfaces):
Las interfaces son pequeñas y específicas ( INotificacion, IObservador).

D (Dependency Inversion):
Componentes de alto nivel (Usuario) depende de abstracciones ( INotificacionFactory), no de implementaciones concretas.
