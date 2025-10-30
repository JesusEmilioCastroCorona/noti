# notification_system.py
from abc import ABC, abstractmethod
from typing import List

# -----------------------
# Interfaces / Abstracciones
# -----------------------
class IObservador(ABC):
    @abstractmethod
    def actualizar(self, mensaje: str) -> None:
        """Recibe la notificación (Observer)."""
        pass

class INotificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str, usuario: "Usuario") -> None:
        """Envia la notificación concreta (Email/SMS/Push)."""
        pass

class INotificacionFactory(ABC):
    @abstractmethod
    def crear_notificacion(self, tipo: str) -> INotificacion:
        """Factory method: crea un INotificacion según 'tipo'."""
        pass

# -----------------------
# Implementaciones concretas de notificación
# (simuladas con prints para probar localmente)
# -----------------------
class EmailNotificacion(INotificacion):
    def enviar(self, mensaje: str, usuario: "Usuario") -> None:
        # En un sistema real aquí usarías smtplib u otro servicio.
        print(f"[EMAIL] Para: {usuario.email} | Mensaje: {mensaje}")

class SMSNotificacion(INotificacion):
    def enviar(self, mensaje: str, usuario: "Usuario") -> None:
        # En un sistema real aquí llamarías a un gateway SMS (Twilio, etc).
        print(f"[SMS] Para: {usuario.telefono} | Mensaje: {mensaje}")

class PushNotificacion(INotificacion):
    def enviar(self, mensaje: str, usuario: "Usuario") -> None:
        # Aquí se integraría un servicio de push (Firebase, APNs...).
        print(f"[PUSH] Usuario: {usuario.nombre} | Mensaje: {mensaje}")

# -----------------------
# Fábrica (Factory Method)
# -----------------------
class NotificacionFactory(INotificacionFactory):
    def crear_notificacion(self, tipo: str) -> INotificacion:
        tipo = tipo.lower()
        if tipo == "email":
            return EmailNotificacion()
        if tipo == "sms":
            return SMSNotificacion()
        if tipo == "push":
            return PushNotificacion()
        raise ValueError(f"Tipo de notificación desconocido: {tipo}")

# -----------------------
# Usuario (Observer)
# -----------------------
class Usuario(IObservador):
    def __init__(self, nombre: str, email: str, telefono: str,
                 preferencias: List[str], factory: INotificacionFactory):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        # preferencias: lista de strings -> "email", "sms", "push"
        self.preferencias = list(preferencias)
        # Inyección de la fábrica (dependency inversion via abstracción)
        self._factory = factory
        self.ultimo_mensaje = None

    def actualizar(self, mensaje: str) -> None:
        """Cuando el sujeto notifica, el usuario 'actualiza' y envía por sus canales."""
        self.ultimo_mensaje = mensaje
        for tipo in self.preferencias:
            try:
                canal = self._factory.crear_notificacion(tipo)
                canal.enviar(mensaje, self)
            except ValueError as e:
                print(f"[WARN] {e} (usuario: {self.nombre})")

    def suscribirse(self, sujeto: "Notificador") -> None:
        sujeto.agregar_observador(self)

    def darse_de_baja(self, sujeto: "Notificador") -> None:
        sujeto.eliminar_observador(self)

    def __eq__(self, other):
        return isinstance(other, Usuario) and self.email == other.email

    def __hash__(self):
        return hash(self.email)

# -----------------------
# Sujeto/Subject (Notificador) - patrón Observer
# -----------------------
class Notificador:
    def __init__(self):
        # uso un set para evitar duplicados (requiere que Usuario sea hashable)
        self._observadores = set()

    def agregar_observador(self, usuario: Usuario) -> None:
        self._observadores.add(usuario)
        print(f"[INFO] {usuario.nombre} suscrito.")

    def eliminar_observador(self, usuario: Usuario) -> None:
        if usuario in self._observadores:
            self._observadores.remove(usuario)
            print(f"[INFO] {usuario.nombre} dado de baja.")
        else:
            print(f"[INFO] {usuario.nombre} no estaba suscrito.")

    def notificar_observadores(self, mensaje: str) -> None:
        print(f"[NOTIFICADOR] Enviando mensaje a {len(self._observadores)} observador(es)...")
        for obs in self._observadores:
            obs.actualizar(mensaje)

# -----------------------
# Demo / Uso ejemplo (main)
# -----------------------
def main():
    factory = NotificacionFactory()
    gestor = Notificador()

    # Crear usuarios con diferentes preferencias
    itzel = Usuario("itzel", "ana@example.com", "+5215512345678", ["email"], factory)
    luis = Usuario("Luis", "luis@example.com", "+5215587654321", ["sms", "push"], factory)
    Lupito = Usuario("Lupito", "carla@example.com", "+5215591122334", ["push", "email"], factory)

    # Suscribir usuarios
    itzel.suscribirse(gestor)
    luis.suscribirse(gestor)
    gestor.agregar_observador(Lupito)  # se puede hacer desde gestor o desde usuario

    # Enviar una notificación
    gestor.notificar_observadores("Nueva actualización disponible: versión 1.2.0")

    # Dar de baja a alguien y volver a notificar
    luis.darse_de_baja(gestor)
    gestor.notificar_observadores("Recordatorio: mantenimiento programado mañana 02:00 AM.")

if __name__ == "__main__":
    main()
