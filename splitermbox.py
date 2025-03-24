import mailbox
import os

def split_mbox(input_file, output_dir, max_size_mb=200):
    # Abrir el archivo MBOX de entrada
    mbox = mailbox.mbox(input_file)
    
    # Asegurarse de que el directorio de salida exista
    os.makedirs(output_dir, exist_ok=True)
    
    # Variables para dividir el archivo
    total_size = 0
    mbox_counter = 1
    current_mbox = mailbox.mbox(os.path.join(output_dir, f"split_{mbox_counter}.mbox"))
    
    # Establecer el tamaño máximo del archivo (en bytes)
    max_size_bytes = max_size_mb * 1024 * 1024
    
    # Iterar sobre los mensajes en el archivo MBOX
    for message in mbox:
        current_mbox.add(message)
        total_size += len(str(message))  # Tamaño aproximado de cada mensaje en bytes
        
        # Verificar si el tamaño supera el límite
        if total_size > max_size_bytes:
            # Guardar el archivo actual y empezar uno nuevo
            current_mbox.close()
            mbox_counter += 1
            current_mbox = mailbox.mbox(os.path.join(output_dir, f"split_{mbox_counter}.mbox"))
            total_size = 0
            current_mbox.add(message)  # Agregar el primer mensaje al nuevo archivo
    
    # Guardar el último archivo MBOX
    current_mbox.close()
    print(f"Archivo dividido en {mbox_counter} partes y guardado en: {output_dir}")

    print(f"")

    print(f"Script hecho por Adrian Azaola.")

# Usar el script con un archivo de entrada y un directorio de salida
input_file = 'mails.mbox'  # Cambia esto a la ruta de tu archivo MBOX
output_dir = '/Users/TUDIRECCION/Downloads/split_mbox'  # Cambia esto a la ruta donde quieres guardar los archivos divididos

# Llamar a la función para dividir el archivo MBOX y guardar los archivos divididos
split_mbox(input_file, output_dir)
