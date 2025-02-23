import time
import random

class Semaforo:
    def __init__(self):
        self.estado = "Rojo"
        self.tiempo_verde = 5  
        self.tiempo_amarillo = 2 
        self.tiempo_rojo = 5    
        self.fluxo_trafico = 0  
    
    def detectar_vehiculos(self):
        self.fluxo_trafico = random.randint(0, 20)
        print(f"Vehículos detectados: {self.fluxo_trafico}")
        
    def ajustar_tiempos(self):
        if self.fluxo_trafico > 15:
            self.tiempo_verde = 10 
            self.tiempo_rojo = 5   
        elif self.fluxo_trafico > 8:
            self.tiempo_verde = 7  
            self.tiempo_rojo = 6   
        else:
            self.tiempo_verde = 5  
            self.tiempo_rojo = 7   
    
    def cambiar_estado(self):
        while True:
            self.detectar_vehiculos()
            self.ajustar_tiempos()
            
            self.estado = "Verde"
            print(f"Semaforo: {self.estado} - Duracion: {self.tiempo_verde} segundos")
            time.sleep(self.tiempo_verde)
            
            self.estado = "Amarillo"
            print(f"Semaforo: {self.estado} - Duracion: {self.tiempo_amarillo} segundos")
            time.sleep(self.tiempo_amarillo)
            
            self.estado = "Rojo"
            print(f"Semaforo: {self.estado} - Duracion: {self.tiempo_rojo} segundos")
            time.sleep(self.tiempo_rojo)

semaforo = Semaforo()

semaforo.cambiar_estado()


