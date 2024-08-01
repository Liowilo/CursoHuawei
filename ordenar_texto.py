import torch

def ordenar_texto(texto, max_longitud=256):
    try:
        # Convertir el texto a un tensor
        tensor_texto = torch.tensor([ord(c) for c in texto])
        print("Tensor de texto creado con éxito.")
        
        # Inicializar la lista para almacenar las líneas ordenadas
        lineas_ordenadas = []
        
        # Inicializar el índice de inicio
        inicio = 0
        
        while inicio < len(tensor_texto):
            # Definir el fin de la línea actual
            fin = min(inicio + max_longitud, len(tensor_texto))
            
            # Ajustar fin para no cortar palabras a la mitad, buscando el último espacio
            if fin < len(tensor_texto) and tensor_texto[fin] != ord(' '):
                # Buscar el último espacio antes del límite de la línea
                sub_tensor = tensor_texto[inicio:fin]
                espacios = (sub_tensor == ord(' ')).nonzero(as_tuple=True)
                if len(espacios[0]) > 0:
                    fin = inicio + espacios[0][-1].item()
            
            # Agregar la línea a la lista
            lineas_ordenadas.append(tensor_texto[inicio:fin].tolist())
            
            # Actualizar el índice de inicio
            inicio = fin + 1
        
        # Convertir los tensores de vuelta a texto
        texto_ordenado = '\n'.join([''.join([chr(c) for c in linea]) for linea in lineas_ordenadas])
        
        return texto_ordenado
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
texto_ejemplo = "Este es un ejemplo de texto largo que necesita ser ordenado con una longitud máxima de 256 caracteres por línea. Vamos a ver cómo funciona el algoritmo con este texto de prueba que es suficientemente largo para necesitar múltiples líneas para que se ajuste correctamente y no corte palabras a la mitad."

texto_ordenado = ordenar_texto(texto_ejemplo)
print(texto_ordenado)
