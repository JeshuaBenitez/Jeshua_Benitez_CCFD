from pathlib import Path
import pandas as pd

# Archivo original (180k filas aprox)
src = Path("data/creditcard.csv")
df = pd.read_csv(src)

# 1) Dataset completo (copia exacta)
df.to_csv("data/creditcard_full.csv", index=False)

# 2) Mitad del dataset (que se convierte en el principal)
df.sample(frac=1.0, random_state=42).to_csv("data/creditcard_half.csv", index=False)

# 3) Mitad de la mitad (25% total) (se convierte en el 50% total)
df.sample(frac=0.50, random_state=42).to_csv("data/creditcard_quarter.csv", index=False)

# 4) Mitad de la mitad (25% total) 
df.sample(frac=0.25, random_state=42).to_csv("data/creditcard_quarter.csv", index=False)

# 🔹 Nuevos datasets reducidos para Cloudinary
df.head(10000).to_csv("data/creditcard_10k.csv", index=False)   # ~5-6 MB
df.head(5000).to_csv("data/creditcard_5k.csv", index=False)     # ~3 MB
df.head(2500).to_csv("data/creditcard_2_5k.csv", index=False)

print("✅ Archivos generados en carpeta data/:")
print("- creditcard_full.csv:", len(df), "filas")
print("- creditcard_half.csv:", int(len(df) * 0.5), "filas aprox")
print("- creditcard_quarter.csv:", int(len(df) * 0.25), "filas aprox")
print("- creditcard_10k.csv: 10000 filas (Cloudinary OK)")
print("- creditcard_5k.csv: 5000 filas (Cloudinary OK)")
