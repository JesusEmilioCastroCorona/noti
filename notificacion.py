from abc import ABC, abstractmethod

# ----------------------------------------------------
# 3. Patrón Factory Method: Interfaz y Clases Concretas
# ----------------------------------------------------

# Interfaz INotificacion (para aplicar DIP)
class INotificacion(ABC):
    """Define la interfaz para el envío de notificaciones."""
    @abstractmethod
    def enviar(self, mensaje: str, destino: str):
        """Método para enviar el mensaje al destino específico."""
        pass

# Clases Concretas de Notificación
class EmailNotificacion(INotificacion):
    """Implementación para enviar notificaciones por correo electrónico."""
    def enviar(self, mensaje: str, destino: str):
        print(f"[EMAIL] Enviando a {destino}: '{mensaje}'")

class SMSNotificacion(INotificacion):
    """Implementación para enviar notificaciones por SMS."""
    def enviar(self, mensaje: str, destino: str):
        print(f"[SMS] Enviando a {destino}: '{mensaje}'")

class PushNotificacion(INotificacion):
    """Implementación para enviar notificaciones Push."""
    def enviar(self, mensaje: str, destino: str):
        print(f"[PUSH] Enviando a {destino}: '{mensaje}'")

# Clase Fábrica (Factory Method)
class NotificacionFactory:
    """Clase que crea instancias de INotificacion basándose en el tipo."""
    def crearNotificacion(self, tipo: str) -> INotificacion:
        """
        Método de fábrica para crear el objeto de notificación.
        Aplica OCP: si se agrega un nuevo tipo (e.g., WhatsApp), solo se modifica
        esta clase (el método), no las clases que usan la fábrica.
        """
        tipo = tipo.upper()
        if tipo == "EMAIL":
            return EmailNotificacion()
        elif tipo == "SMS":
            return SMSNotificacion()
        elif tipo == "PUSH":
            return PushNotificacion()
        else:
            raise ValueError(f"Tipo de notificación desconocido: {tipo}")
# ----------------------------------------------------
# 2. Patrón Observer: Interfaz, Observador y Sujeto
# ----------------------------------------------------

# Interfaz IObservador (para aplicar DIP)
class IObservador(ABC):
    """Define la interfaz para los observadores (usuarios)."""
    @abstractmethod
    def actualizar(self, mensaje: str):
        """Método llamado por el sujeto para notificar una actualización."""
        pass

# Clase Usuario (Observador Concreto)
class Usuario(IObservador):
    """
    Representa a un usuario del sistema (Observador Concreto).
    Aplica SRP: su única responsabilidad es gestionar sus datos y recibir/procesar
    la notificación que le llega.
    """
    def __init__(self, nombre: str, email: str, telefono: str, metodo_notif: str):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.metodo_notif = metodo_notif.upper() # EMAIL, SMS, PUSH

    def __str__(self):
        return f"Usuario: {self.nombre} (Tipo: {self.metodo_notif})"

    def actualizar(self, mensaje: str):
        """
        Recibe la notificación del sujeto y usa el Factory Method
        para enviar el mensaje por su método preferido.
        """
        factory = NotificacionFactory()
        try:
            # Crea el objeto de notificación según el método preferido del usuario
            notificacion_obj = factory.crearNotificacion(self.metodo_notif)

            # Determina el destino
            destino = ""
            if self.metodo_notif == "EMAIL":
                destino = self.email
            elif self.metodo_notif == "SMS":
                destino = self.telefono
            elif self.metodo_notif == "PUSH":
                destino = self.nombre # Por simplicidad, usamos el nombre para Push
            
            # Envía la notificación
            notificacion_obj.enviar(f"¡Hola {self.nombre}! {mensaje}", destino)

        except ValueError as e:
            print(f"Error al notificar a {self.nombre}: {e}")


# Clase NotificacionSystem (Sujeto Concreto)
class NotificacionSystem:
    """
    Representa el sistema que mantiene y notifica a los observadores (usuarios).
    Aplica SRP: su única responsabilidad es gestionar la lista de observadores
    y coordinar la notificación.
    """
    def __init__(self):
        self._observadores: list[IObservador] = []

    def agregarObservador(self, observador: IObservador):
        """Suscribe a un usuario a las notificaciones."""
        if observador not in self._observadores:
            self._observadores.append(observador)
            print(f"✔️ Suscripción exitosa: {observador}")

    def eliminarObservador(self, observador: IObservador):
        """Da de baja a un usuario de las notificaciones."""
        try:
            self._observadores.remove(observador)
            print(f"❌ Baja exitosa: {observador}")
        except ValueError:
            print(f"⚠️ El usuario {observador} no estaba suscrito.")

    def notificarObservadores(self, mensaje: str):
        """Notifica a todos los usuarios suscritos sobre el nuevo mensaje."""
        print(f"\n--- INICIANDO NOTIFICACIÓN: '{mensaje}' ---")
        if not self._observadores:
            print("No hay usuarios suscritos para notificar.")
            return

        for observador in self._observadores:
            observador.actualizar(mensaje)
        print("--- FIN DE NOTIFICACIÓN ---\n")
# ----------------------------------------------------
# 5. Simulación y Ejemplo de Uso (Script Principal)
# ----------------------------------------------------

def main():
    print("--- INICIALIZANDO SISTEMA DE NOTIFICACIONES ---")
    sistema_notif = NotificacionSystem()

    # 1. Crear Varios Usuarios (Observadores)
    user1 = Usuario("Alice", "alice@corp.com", "555-1001", "EMAIL")
    user2 = Usuario("Bob", "bob@corp.com", "555-2002", "SMS")
    user3 = Usuario("Charlie", "charlie@corp.com", "555-3003", "PUSH")
    user4 = Usuario("Diana", "diana@corp.com", "555-4004", "EMAIL")

    # 2. Suscribir Usuarios (agregarObservador)
    sistema_notif.agregarObservador(user1)
    sistema_notif.agregarObservador(user2)
    sistema_notif.agregarObservador(user3)
    sistema_notif.agregarObservador(user4)

    # 3. Enviar el Primer Mensaje de Prueba
    mensaje_general = "¡Nueva actualización disponible! Revisa las notas de la versión 2.0."
    sistema_notif.notificarObservadores(mensaje_general)

    # 4. Dar de Baja a un Usuario
    print("\n--- Diana se da de baja ---")
    sistema_notif.eliminarObservador(user4)

    # 5. Enviar el Segundo Mensaje de Prueba
    mensaje_urgente = "¡Alerta de Seguridad! Se requiere cambiar su contraseña inmediatamente."
    sistema_notif.notificarObservadores(mensaje_urgente)


if __name__ == "__main__":
    main()