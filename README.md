# 🧩 Sistema de Notificaciones con Patrones de Diseño (Observer + Factory Method)

Este proyecto implementa un **sistema de notificaciones** en Python que combina los patrones de diseño **Observer** y **Factory Method** para lograr un código flexible, escalable y orientado a la responsabilidad única (SRP).

---

## 🚀 Descripción General

El programa simula un sistema que envía notificaciones a diferentes usuarios mediante distintos métodos (Email, SMS o Push).  
Cada usuario puede elegir su tipo preferido de notificación, y el sistema se encarga de enviarlas automáticamente.

Se aplican dos patrones de diseño:

1. **Observer (Observador):**
   - Permite que varios objetos (usuarios) estén "suscritos" a un sujeto (sistema de notificaciones).
   - Cuando el sujeto emite un mensaje, todos los observadores son notificados automáticamente.

2. **Factory Method (Método Fábrica):**
   - Permite crear diferentes tipos de notificaciones (Email, SMS, Push) sin modificar el código principal.
   - Facilita la extensión del sistema agregando nuevos tipos (por ejemplo, WhatsApp) sin romper el código existente.

---

## 🧱 Estructura del Código

### 1. Interfaz `INotificacion` y Clases Concretas
Define una interfaz genérica para las notificaciones y las clases concretas que la implementan.

```python
class INotificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str, destino: str):
        pass

class EmailNotificacion(INotificacion):
    def enviar(self, mensaje: str, destino: str):
        print(f"[EMAIL] Enviando a {destino}: '{mensaje}'")
Clases disponibles:

EmailNotificacion

SMSNotificacion

PushNotificacion

2. NotificacionFactory
Implementa el patrón Factory Method.
Crea instancias del tipo de notificación solicitado.

python
Copiar código
class NotificacionFactory:
    def crearNotificacion(self, tipo: str) -> INotificacion:
        if tipo == "EMAIL":
            return EmailNotificacion()
        elif tipo == "SMS":
            return SMSNotificacion()
        elif tipo == "PUSH":
            return PushNotificacion()
        else:
            raise ValueError(f"Tipo de notificación desconocido: {tipo}")
✅ Aplica el principio OCP (Open/Closed Principle):
El sistema está abierto a la extensión (nuevos tipos de notificación), pero cerrado a la modificación.

3. Patrón Observer
Interfaz IObservador
Define el contrato para los observadores (usuarios suscritos).

python
Copiar código
class IObservador(ABC):
    @abstractmethod
    def actualizar(self, mensaje: str):
        pass
Clase Usuario
Cada usuario implementa el método actualizar(), que recibe el mensaje y usa el Factory Method para enviar la notificación por su método preferido.

python
Copiar código
class Usuario(IObservador):
    def __init__(self, nombre, email, telefono, metodo_notif):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.metodo_notif = metodo_notif.upper()

    def actualizar(self, mensaje: str):
        factory = NotificacionFactory()
        notificacion = factory.crearNotificacion(self.metodo_notif)
        # Envía la notificación al destino correspondiente
        notificacion.enviar(f"¡Hola {self.nombre}! {mensaje}", self.email)
4. Clase NotificacionSystem (Sujeto)
Gestiona la lista de observadores y los notifica cuando ocurre un evento.

python
Copiar código
class NotificacionSystem:
    def __init__(self):
        self._observadores = []

    def agregarObservador(self, observador):
        self._observadores.append(observador)

    def eliminarObservador(self, observador):
        self._observadores.remove(observador)

    def notificarObservadores(self, mensaje):
        for obs in self._observadores:
            obs.actualizar(mensaje)
🧠 Principios SOLID aplicados
Principio	Descripción
SRP (Responsabilidad Única)	Cada clase tiene un único propósito.
OCP (Abierto/Cerrado)	Es posible agregar nuevos tipos de notificación sin modificar el código existente.
DIP (Inversión de Dependencias)	El sistema depende de abstracciones (INotificacion, IObservador), no de implementaciones concretas.

🧩 Ejemplo de Ejecución
Código principal (main())
python
Copiar código
if __name__ == "__main__":
    sistema = NotificacionSystem()

    user1 = Usuario("Alice", "alice@corp.com", "555-1001", "EMAIL")
    user2 = Usuario("Bob", "bob@corp.com", "555-2002", "SMS")
    user3 = Usuario("Charlie", "charlie@corp.com", "555-3003", "PUSH")

    sistema.agregarObservador(user1)
    sistema.agregarObservador(user2)
    sistema.agregarObservador(user3)

    sistema.notificarObservadores("¡Nueva actualización disponible!")
💻 Resultado en consola
csharp
Copiar código
✔️ Suscripción exitosa: Usuario: Alice (Tipo: EMAIL)
✔️ Suscripción exitosa: Usuario: Bob (Tipo: SMS)
✔️ Suscripción exitosa: Usuario: Charlie (Tipo: PUSH)

--- INICIANDO NOTIFICACIÓN: '¡Nueva actualización disponible!' ---
[EMAIL] Enviando a alice@corp.com: '¡Hola Alice! ¡Nueva actualización disponible!'
[SMS] Enviando a 555-2002: '¡Hola Bob! ¡Nueva actualización disponible!'
[PUSH] Enviando a Charlie: '¡Hola Charlie! ¡Nueva actualización disponible!'
--- FIN DE NOTIFICACIÓN ---
🧩 Extensión del sistema
Para agregar un nuevo tipo de notificación (por ejemplo, WhatsApp):

Crear una nueva clase que implemente INotificacion:

python
Copiar código
class WhatsAppNotificacion(INotificacion):
    def enviar(self, mensaje, destino):
        print(f"[WHATSAPP] Enviando a {destino}: '{mensaje}'")
Modificar el método crearNotificacion() en NotificacionFactory para incluirlo.

🧾 Requisitos
Python 3.8 o superior

No se requiere ninguna librería externa

📚 Autor
Desarrollado por Jesús Emilio Castro Corona
Ejemplo educativo de patrones de diseño en Python 🧠

📄 Licencia
Este proyecto es de uso libre con fines educativos.

yaml
Copiar código
