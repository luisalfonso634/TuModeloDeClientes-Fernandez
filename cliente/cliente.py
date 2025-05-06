class Cliente:
    """
    Clase para representar a un cliente en una tienda online.
    """
    # Atributos de clase (compartidos por todas las instancias)
    num_clientes = 0

    def __init__(self, nombre, apellido, email, telefono):
        """
        Inicializa una nueva instancia de la clase Cliente.

        Args:
            nombre (str): Nombre del cliente.
            apellido (str): Apellido del cliente.
            email (str): Email del cliente.
            telefono (str): Telefono del cliente.
        """
        # Atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

        # Incrementa el número de clientes
        Cliente.num_clientes += 1

    def __str__(self):
        """
        Retorna una representación en cadena del objeto Cliente.
        """
        return f"{self.nombre} {self.apellido}"

    def actualizar_email(self, nuevo_email):
        """
        Actualiza el email del cliente.

        Args:
            nuevo_email (str): El nuevo email del cliente.
        """
        self.email = nuevo_email
        print(f"Email de {self} actualizado a {nuevo_email}")

    def mostrar_informacion(self):
        """
        Muestra la información del cliente.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")


# Ejemplo de uso (esto normalmente estaría en otro archivo o función)
if __name__ == "__main__":
    cliente1 = Cliente("Luis", "Fernandez", "luis.fernandez@gmail.com", "1123456789")
    cliente2 = Cliente("Juana", "De Arco", "juana.dearco@hotmail.com", "11987654321")

    print(cliente1)  # Imprime: Juan Pérez
    cliente1.actualizar_email("luis.fernandez@hotmail.com")
    cliente1.mostrar_informacion()

    print(f"Número total de clientes: {Cliente.num_clientes}")
