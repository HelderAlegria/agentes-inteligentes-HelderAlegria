def diagnostico(sintomas):
    if "fiebre" in sintomas and "tos" in sintomas and "dificultad para respirar" in sintomas:
        return "Posible diagnóstico: Gripe o COVID-19. Se recomienda acudir a un médico para más pruebas."
    elif "dolor de cabeza" in sintomas and "congestión nasal" in sintomas and "fiebre" in sintomas:
        return "Posible diagnóstico: Resfriado común."
    elif "dolor abdominal" in sintomas and "náuseas" in sintomas and "vómitos" in sintomas:
        return "Posible diagnóstico: Intoxicación alimentaria o Gastroenteritis."
    elif "dolor de garganta" in sintomas and "tos" in sintomas and "fiebre" in sintomas:
        return "Posible diagnóstico: Faringitis o Amigdalitis."
    elif "fatiga" in sintomas and "dolor muscular" in sintomas and "fiebre" in sintomas:
        return "Posible diagnóstico: Enfermedad viral o gripe."
    elif "dolor en las articulaciones" in sintomas and "erupción cutánea" in sintomas:
        return "Posible diagnóstico: Artritis o Lupus. Se recomienda consultar a un médico."
    else:
        return "Síntomas no reconocidos. Se recomienda consultar a un médico para un diagnóstico adecuado."

def obtener_sintomas():
    print("Por favor, ingresa tus síntomas, separados por comas (ejemplo: fiebre, tos, dolor de cabeza):")
    sintomas_input = input().lower().strip()
    sintomas = sintomas_input.split(",")
    sintomas = [sintoma.strip() for sintoma in sintomas]  
    return sintomas

def main():
    sintomas = obtener_sintomas()

    resultado = diagnostico(sintomas)

    print("\nDiagnóstico: " + resultado)

if __name__ == "__main__":
    main()
