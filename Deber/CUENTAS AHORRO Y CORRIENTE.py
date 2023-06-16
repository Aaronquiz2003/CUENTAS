from CUENTAS import Cuentas
class CuentaAhorros(Cuentas):
    def __init__(self, numero, nombre_propietario, saldo, interes):
        super().__init__(numero, nombre_propietario, saldo)
        self.interes = interes
    @property
    def interes(self):
        return self._interes
    @interes.setter
    def interes(self, interes):
        self._interes = interes
    def pagar_interes(self):
        interes_generado = self.saldo * self.interes
        self.credito(interes_generado)
    def mostrar_cuenta(self):
        print("Cuenta de Ahorros:")
        print("Número de cuenta:", self.numero)
        print("Propietario:", self.nombre_propietario)
        self.mostrar_saldo()
class CuentaCorriente(Cuentas):
    def __init__(self, numero, nombre_propietario, saldo, tiene_chequera):
        super().__init__(numero, nombre_propietario, saldo)
        self.tiene_chequera = tiene_chequera
    @property
    def tiene_chequera(self):
        return self._tiene_chequera
    @tiene_chequera.setter
    def tiene_chequera(self, tiene_chequera):
        self._tiene_chequera = tiene_chequera
    def pagar_cheque(self, valor):
        if self.tiene_chequera:
            self.debito(valor)
        else:
            print("No se puede pagar el cheque. Cuenta sin chequera.")
    def mostrar_cuenta(self):
        print("Cuenta Corriente:")
        print("Número de cuenta:", self.numero)
        print("Propietario:", self.nombre_propietario)
        self.mostrar_saldo()
print("_______________________________________")
cuenta_ahorros = CuentaAhorros("01111111", "Aaron Quizhpi", 200.0, 0.05)
cuenta_ahorros.mostrar_cuenta()
cuenta_ahorros.credito(60.0)
cuenta_ahorros.debito(60.0)
cuenta_ahorros.mostrar_cuenta()
cuenta_ahorros.pagar_interes()
cuenta_ahorros.mostrar_cuenta()
print("_______________________________________")
print("///////////////////////////////////////")
print("_______________________________________")
cuenta_corriente = CuentaCorriente("01111111", "Aaron Quizhpi", 250.0, True)
cuenta_corriente.mostrar_cuenta()
cuenta_corriente.credito(20.0)
cuenta_corriente.debito(40.0)
cuenta_corriente.mostrar_cuenta()
cuenta_corriente.pagar_cheque(18.0)
cuenta_corriente.mostrar_cuenta()
print("_______________________________________")