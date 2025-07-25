def write_to_excel(data, filename):
    import pandas as pd

    # Cria um DataFrame a partir dos dados extraídos
    df = pd.DataFrame(data)

    # Escreve o DataFrame em um arquivo Excel
    df.to_excel(filename, index=False)