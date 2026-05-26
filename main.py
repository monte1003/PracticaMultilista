from File import File
if __name__ == "__main__":
    # 1. Instanciar el lector de archivos y cargar el CSV
    print("--- Cargando archivo DIVIPOLA ---")
    parser = File()
    # Asegúrate de que 'divipola.csv' esté en la misma carpeta
    multilista = parser.read_divipola("divipola.csv")
    print("¡Estructura cargada con éxito!\n")

    # 2. Imprimir la estructura inicial de forma jerárquica
    print("--- Estructura Jerárquica Completa ---")
    multilista.print_multilist()
    print("\n" + "="*50 + "\n")

    